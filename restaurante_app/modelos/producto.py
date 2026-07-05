class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    """

    def __init__(self, nombre, precio, disponible):
        # Validación para evitar nombres vacíos
        if nombre.strip():
            self.nombre = nombre.strip()
        else:
            self.nombre = "Sin nombre"

        # Atributo encapsulado
        self.__precio = precio

        # Indica si el producto está disponible
        self.disponible = disponible

    def obtener_precio(self):
        """
        Devuelve el precio del producto.
        """
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """
        Permite modificar el precio validando que sea mayor que cero.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        """
        Método que será sobrescrito por las clases hijas.
        """
        print("\n=== PRODUCTO ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Disponible: {self.disponible}")