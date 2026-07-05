from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def mostrar_menu():
    """
    Muestra el menú principal.
    """
    print("\n===================================")
    print("    SISTEMA DE RESTAURANTE")
    print("===================================")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar productos")
    print("4. Salir")
    print("===================================")


def registrar_platillo(restaurante):
    """
    Solicita los datos de un platillo y lo registra.
    """

def registrar_platillo(restaurante):
    """
    Solicita los datos de un platillo y lo registra.
    """

    print("\n=== REGISTRAR PLATILLO ===")

    while True:
        nombre = input("Nombre: ").strip()

        if nombre:
            break

        print("Error: Debe ingresar un nombre.")

    while True:
        precio = float(input("Precio: "))

        if precio > 0:
            break

        print("Error: El precio debe ser mayor que cero.")

    try:
       
        calorias = int(input("Calorías: "))
        disponible = (input("¿Disponible? (si/no): ").strip().lower()) == "si" 
        platillo = Platillo(nombre, precio,  disponible, calorias)
            
        restaurante.registrar_producto(platillo)

    except ValueError:
        print("\nError: Ingrese valores numéricos válidos.")

def registrar_bebida(restaurante):
    """
    Solicita los datos de una bebida y la registra.
    """

    print("\n=== REGISTRAR BEBIDA ===")

    while True:
        nombre = input("Nombre: ").strip()

        if nombre:
            break

        print("Error: Debe ingresar un nombre.")

    while True:
            precio = float(input("Precio: "))

            if precio > 0:
                break

            print("Error: El precio debe ser mayor que cero.")

    try:
        
        volumen_ml = int(input("Volumen en ml: "))
        disponible = (input("¿Disponible? (si/no): ").strip().lower()) == "si"
        bebida = Bebida(nombre, precio, disponible, volumen_ml)
            
        restaurante.registrar_producto(bebida)

    except ValueError:
        print("\nError: Ingrese valores numéricos válidos.")

def main():
    """
    Punto de entrada del programa.
    """
    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            registrar_platillo(restaurante)

        elif opcion == "2":

            registrar_bebida(restaurante)

        elif opcion == "3":

            restaurante.mostrar_productos()

        elif opcion == "4":

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()