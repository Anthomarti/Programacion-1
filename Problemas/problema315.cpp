#include <stdio.h>
#include <stdbool.h>

// Esta es la primera instancia de la función es_par, la cual se ha comentado

/*
bool es_par(int n) {
   if(n % 2 = 0) {
      return true;
   } else {
      return false;
   }
}
*/

// Esta es la segunda instancia de la función es_par, la cual funciona correctamente
bool es_par(int n) {
   if(n % 2 == 0) {
      return true;
   } else {
      return false;
   }
}

int main() {
   int x;
   printf("Ingrese un número entero: ");
   scanf("%d", &x);
   if(es_par(x)) {
      printf("El número es par\n");
   } else {
      printf("El número es impar\n");
   }
   return 0;
}