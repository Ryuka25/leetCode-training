#include <stdio.h>
#include <math.h>

float addition(float, float, float);
float addition(float a,float b, float c) {

    float s = a + b + c;

    return s;
}

float soustraction(float, float, float);
float soustraction(float a,float b, float c) {

    float s = a - b - c;

    return s;
}

float multiplication(float, float, float);
float multiplication(float a,float b, float c) {

    float p = a * b * c;

    return p;
}

float division(float, float, float);
float division(float a, float b, float c) {
    float r;
    
    if (b == 0) printf("Erreur de division par 0");
    else r = a / b / c;

    return r;
}

/* int valeurAbs(int,int);
int valeurAbs(int a, int b) {

    int r = abs(a-b);

    return r;
}

float arrondiEntierSuperieur(float, float);
float arrondiEntierSuperieur(float a, float b) {

    float r = ceil( a / b);

    return r;
} */

int main() {

    // DECLARATION VARIABLE
    float a,b,c;
    float r;

    // DISPLAY  
    printf("Calculatrice\n");

    printf("\nValeur de a: ");
    scanf("%f", &a);
    printf("a vaut %.3f", a);
    getchar();

    printf("\nValeur de b: ");
    scanf("%f", &b);
    printf("b vaut %f", b);
    getchar();

    printf("\nValeur de c: ");
    scanf("%f", &c);
    printf("c vaut %.3f", c);
    getchar();

    r = addition(a,b,c);

    printf("\nLe resultat est : %.3f", r);

    getchar();
    return 0;
}