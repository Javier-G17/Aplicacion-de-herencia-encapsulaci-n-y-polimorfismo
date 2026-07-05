from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase hija que representa una bebida.
    """
    def __init__(self, nombre, precio, disponible, volumen_ml):
        # Reutiliza los atributos de la clase padre
        super().__init__(nombre, precio, disponible)

        # Atributo propio de Bebida
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre.
        """
        print("\n=== BEBIDA ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponible: {self.disponible}")
        print(f"Volumen: {self.volumen_ml} ml")