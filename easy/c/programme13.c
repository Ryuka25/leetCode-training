#include <stdio.h>
#include <stdlib.h>

int main() {

    char C;
    char O;
    char U;
    char c;
    char o;
    char u;

    C = 'C';
    O = 'O';
    U = 'U';
    c = 'c';
    o = 'o';
    u = 'u';

    int n1;
    int n2;
    int n3;
    int n4;

    n1 = 1;
    n2 = 2;
    n3 = 3;
    n4 = 456;

    printf("\n%c", C);
    printf("\n%c", O);
    printf("\n%c", U);
    printf("\n%c%c%c", C,o,u);

    printf("\n%d", n1);
    printf("\n%d", n2);
    printf("\n%d", n3);
    printf("\n%d", n4);

    char var;
    var = '\'';
    printf("\nC%cest rigolo", var);

    getchar();
    return 0;
}