from modelos.producto import Producto


class Platillo(Producto):
    """
    Clase hija que representa un platillo.
    """

    def __init__(self, nombre, precio, disponible, calorias):
        # Reutiliza los atributos de la clase padre
        super().__init__(nombre, precio, disponible)

        # Atributo propio de Platillo
        self.calorias = calorias

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre.
        """
        print("\n=== PLATILLO ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Disponible: {self.disponible}")
        print(f"Calorías: {self.calorias}")