import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Producto, Cliente, ServicioTecnico, Admin

# 1. Configuración de Rutas Seguras y Compatibles (Windows/Linux)
BASE_DIR = Path(__file__).resolve().parent

# Cargar variables de entorno (Supabase etc)
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:4200")

app = Flask(__name__)

# 2. Habilitar CORS de manera robusta
CORS(app, resources={r"/api/*": {"origins": [FRONTEND_URL, "http://localhost:4200", "http://localhost:1420"]}})

# --- SQLite LOCAL Configuration ---
# Usamos pathlib para asegurar compatibilidad de barras
db_path = BASE_DIR / 'arecofix_local.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ----------------- Rutas de la API -----------------

@app.route('/', methods=['GET'])
def home():
    """Ruta raíz para verificar desde el navegador sin recibir 404."""
    return jsonify({
        "message": "¡Motor Local de Arecofix funcionando! Para verificar el estado de la API, visita /api/health"
    })

@app.route('/api/health', methods=['GET'])
def get_health():

    """Endpoint para verificar que el backend está vivo y accesible (Health Check)."""
    data_folder = BASE_DIR / "data" / "uploads"
    return jsonify({
        "status": "ok",
        "message": "Backend Flask funcionando correctamente",
        "os_path_example": str(data_folder),
        "server": "Arecofix Engine",
        "version": "1.0.0",
        "mode": "Offline-First"
    })

# --- AUTHENTICATION (ADMIN OFFLINE LOGIN) ---

@app.route('/api/login', methods=['POST'])
def offline_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    admin = Admin.query.filter_by(username=username).first()
    
    if admin and check_password_hash(admin.password_hash, password):
        return jsonify({
            "message": "Login offline exitoso",
            "admin": {"id": admin.id, "username": admin.username}
        }), 200
        
    return jsonify({"error": "Credenciales inválidas"}), 401


# --- INVENTARIO (PRODUCTOS) ---

@app.route('/api/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])

@app.route('/api/productos', methods=['POST'])
def add_producto():
    data = request.json
    nuevo = Producto(
        nombre=data.get('nombre'),
        stock=data.get('stock', 0),
        precio_costo=data.get('precio_costo', 0.0),
        precio_venta=data.get('precio_venta', 0.0),
        categoria=data.get('categoria', 'Repuesto')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

# --- CLIENTES ---

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([c.to_dict() for c in clientes])

@app.route('/api/clientes', methods=['POST'])
def add_cliente():
    data = request.json
    nuevo = Cliente(
        nombre=data.get('nombre'),
        telefono=data.get('telefono'),
        dni=data.get('dni'),
        email=data.get('email')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

# --- SERVICIOS TÉCNICOS ---

@app.route('/api/servicios', methods=['GET'])
def get_servicios():
    servicios = ServicioTecnico.query.all()
    return jsonify([s.to_dict() for s in servicios])

# --- INICIALIZACIÓN ---

if __name__ == '__main__':
    from sync_engine import start_sync_thread
    with app.app_context():
        # Crear la base de datos local al iniciar si no existe
        db.create_all()
        
        # Semilla inicial para Administrador (Offline Login)
        if not Admin.query.first():
            hashed_pw = generate_password_hash("admin123")
            db.session.add(Admin(username="admin", password_hash=hashed_pw))
            db.session.commit()
            print("Usuario Admin (offline) creado. User: admin | Pass: admin123")

        # Semilla inicial para testing si está vacío
        if not Producto.query.first():
            db.session.add(Producto(nombre="Display iPhone 12 Pro", stock=5, precio_venta=75000))
            db.session.commit()
            print("Base de datos local inicializada con semilla básica.")
            
    # Iniciar Hilo de Sincronización en Segundo Plano
    start_sync_thread(app)
            
    # Servidor local en el puerto 5000
    app.run(debug=True, port=5000, use_reloader=False)
