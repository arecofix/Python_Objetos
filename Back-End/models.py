from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    """
    Representación de un producto en el sistema (POO).
    Atributos esenciales para la gestión de productos de Arecofix.
    """
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)
    precio_costo = db.Column(db.Float, default=0.0, nullable=False)
    precio_venta = db.Column(db.Float, default=0.0, nullable=False)

    def __init__(self, nombre, stock, precio_costo, precio_venta):
        self.nombre = nombre
        self.stock = stock
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta

    def calcular_margen_ganancia(self):
        """Ejemplo de método orientado a objetos."""
        return self.precio_venta - self.precio_costo

    def __repr__(self):
        return f'<Producto {self.nombre} - Stock: {self.stock}>'
