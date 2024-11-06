"""
# Titulo: Desafío 2 Excepciones y errores
# Autor: Anthony Martinelli
# Fecha: 05/11/2024
# Descripción:
# Crea un programa que tome una lista de valores
# y realice operaciones matemáticas sobre ellos. 
# Implementa el manejo de varias excepciones comunes
# como ZeroDivisionError, TypeError, y ValueError.
"""

# Función para calcular la suma de una lista de números
def suma(lista):
    try:

        # Utiliza la función sum() para calcular la suma de la lista
        return sum(lista)
    except TypeError:

        # Si la lista contiene elementos que no son números, muestra un mensaje de error
        print("Error: La lista debe contener solo números.")
        return None

# Función para calcular la resta de una lista de números
def resta(lista):
    try:

        # Verifica si la lista tiene al menos dos elementos
        if len(lista) < 2:

            # Si no, lanza una excepción ValueError
            raise ValueError("La lista debe contener al menos dos números.")
        
        # Inicializa el resultado con el primer elemento de la lista
        resultado = lista[0]

        # Recorre la lista a partir del segundo elemento
        for num in lista[1:]:

            # Resta cada elemento del resultado
            resultado -= num

        # Retorna el resultado
        return resultado
    except TypeError:

        # Si la lista contiene elementos que no son números, muestra un mensaje de error
        print("Error: La lista debe contener solo números.")
        return None
    except ValueError as error:

        # Si la lista tiene menos de dos elementos, muestra un mensaje de error
        print(f"Error: {error}")
        return None

# Función para calcular la multiplicación de una lista de números
def multiplicacion(lista):
    try:

        # Inicializa el resultado con 1
        resultado = 1

        # Recorre la lista
        for num in lista:

            # Multiplica cada elemento del resultado
            resultado *= num

        # Retorna el resultado
        return resultado
    except TypeError:

        # Si la lista contiene elementos que no son números, muestra un mensaje de error
        print("Error: La lista debe contener solo números.")
        return None

# Función para calcular la división de una lista de números
def division(lista):
    try:

        # Verifica si la lista tiene al menos dos elementos
        if len(lista) < 2:

            # Si no, lanza una excepción ValueError
            raise ValueError("La lista debe contener al menos dos números.")
        
        # Inicializa el resultado con el primer elemento de la lista
        resultado = lista[0]

        # Recorre la lista a partir del segundo elemento
        for num in lista[1:]:

            # Verifica si el divisor es cero
            if num == 0:

                # Si es cero, lanza una excepción ZeroDivisionError
                raise ZeroDivisionError("No se puede dividir por cero.")
            
            # Divide el resultado por cada elemento
            resultado /= num

        # Retorna el resultado
        return resultado
    except TypeError:

        # Si la lista contiene elementos que no son números, muestra un mensaje de error
        print("Error: La lista debe contener solo números.")
        return None
    except ValueError as error:

        # Si la lista tiene menos de dos elementos, muestra un mensaje de error
        print(f"Error: {error}")
        return None
    except ZeroDivisionError as error:

        # Si se intenta dividir por cero, muestra un mensaje de error
        print(f"Error: {error}")
        return None

# Función principal
def main():

    # Ciclo infinito para mostrar el menú
    while True:

        # Muestra el menú
        print("\nOperaciones matemáticas:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        # Pide la opción al usuario
        opcion = input("Ingrese la opción deseada: ")
        
        # Si la opción es 5, sale del programa
        if opcion == "5":
            break
        
        # Pide la lista de números al usuario
        try:

            # Intenta convertir la entrada a una lista de números
            lista = [float(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
        except ValueError:

            # Si la entrada no es válida, muestra un mensaje de error
            print("Error: La lista debe contener solo números.")
            continue
        
        # Realiza la operación seleccionada
        if opcion == "1":

            # Llama a la función suma
            resultado = suma(lista)
            if resultado is not None:

                # Muestra el resultado
                print(f"La suma es: {resultado}")
        elif opcion == "2":

            # Llama a la función resta
            resultado = resta(lista)
            if resultado is not None:

                # Muestra el resultado
                print(f"La resta es: {resultado}")
        elif opcion == "3":

            # Llama a la función multiplicación
            resultado = multiplicacion(lista)
            if resultado is not None:

                # Muestra el resultado
                print(f"La multiplicación es: {resultado}")
        elif opcion == "4":

            # Llama a la función división
            resultado = division(lista)
            if resultado is not None:

                # Muestra el resultado
                print(f"La división es: {resultado}")
        else:

            # Si la opción no es válida, muestra un mensaje de error
            print("Error: Opción inválida.")

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":

    # Llama a la función principal
    main()