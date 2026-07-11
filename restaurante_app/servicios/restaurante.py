class Restaurante:
    """
    Clase encargada de administrar los productos registrados.
    """

    def __init__(self):
        # Lista donde se almacenarán platillos y bebidas
        self.productos = []

    def registrar_producto(self, producto):
        """
        Agrega un producto a la lista.
        """
        self.productos.append(producto)
        print("\nProducto registrado correctamente.")

    def registrar_platillo(self, platillo):
        self.productos.append(platillo)
        print("\nPlatillo registrado correctamente.")

    def registrar_bebida(self, bebida):
        self.productos.append(bebida)
        print("\nBebida registrada correctamente.")

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.
        Aquí se demuestra el polimorfismo, ya que cada objeto ejecuta su propia versión de mostrar_informacion().
        """
        print("\n========== PRODUCTOS ==========")

        if not self.productos:
            print("No existen productos registrados.")
            return

        for producto in self.productos:
                producto.mostrar_informacion()

    def mostrar_platillo(self):
        print("\n==========PLATILLOS==========")
        if not self.platillos:
            print("No existen platillos registrados")
            for platillo in self.platillos:
                platillo.mostrar_informacion() 
            
    def mostrar_bebida(self):
        print("\n==========BEBIDAS==========")
        if not self.bebidas:
            print("No existen bebidas registrados")
            for bebida in self.bebidas:
                bebida.mostrar_informacion() 

    