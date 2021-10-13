#include <stdio.h>
#include <stdlib.h>

int main() {

    int i;
    /* Variable i de type entier */

    char car;
    /* Variable car de type caractère */

    i = 65;
    /* i vaut 65 */

    car = 'E';
    /* car vaut E */

    printf("i vaut %d.\n",i);
    /* Affiche la valeur de i */

    printf("car vaut %c.\n", car);
    /* Affiche la valeur de car */

    getchar();
    /* Attend l'appuie d'une touche */
    return 0;
}