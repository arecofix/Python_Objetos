import os
from flask import Flask, jsonify
from models import db, Producto

# Configuración básica de la aplicación Flask
app = Flask(__name__)

# Configuración de SQLite local (Offline-First)
# Se crea el archivo arecofix.sqlite localmente
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'arecofix.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos con SQLAlchemy
db.init_app(app)

@app.route('/')
def home():
    """Ruta raíz de prueba."""
    return jsonify({
        "status": "online",
        "service": "Arecofix Local-Engine API",
        "mode": "Offline-First / Local development"
    })

@app.route('/test-db')
def test_db():
    """Crea la base de datos y un producto de ejemplo si no existe."""
    db.create_all()
    
    # Comprobar si hay productos
    primer_producto = Producto.query.first()
    if not primer_producto:
        # Crear un producto de ejemplo (Ejemplo de POO)
        ejemplo = Producto(
            nombre="Batería iPhone 11 - Original",
            stock=15,
            precio_costo=12000.5,
            precio_venta=25500.0
        )
        db.session.add(ejemplo)
        db.session.commit()
        return jsonify({"message": "Base de datos inicializada con éxito."})
    
    return jsonify({"message": f"Base de datos activa con {Producto.query.count()} productos."})

if __name__ == '__main__':
    # Crear tablas al iniciar (para entorno de desarrollo)
    with app.app_context():
        db.create_all()
        print("Motor de datos local activo.")
    
    app.run(debug=True, port=5000)
