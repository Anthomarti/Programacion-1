#include <iostream>

int main() {
    // Declarar variables para almacenar los números ingresados por el usuario
    int num1, num2;

    // Solicitar al usuario que ingrese el primer número
    std::cout << "Ingrese el primer número: ";
    std::cin >> num1;

    // Solicitar al usuario que ingrese el segundo número
    std::cout << "Ingrese el segundo número: ";
    std::cin >> num2;

    // Calcular la suma de los dos números
    int suma = num1 + num2;

    // Mostrar el resultado de la suma
    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << "." << std::endl;

    return 0;
}