#include <stdio.h>

int main(){

    int var1,var2,temp;

    printf("Enter two number : ");
    scanf("%d %d", &var1,&var2);
    printf("\nNormal : \tVar 1 = %d \t Var 2 = %d", var1,var2);
    temp = var1;
    var1 = var2;
    var2 = temp;
    printf("\nSwaped : \tVar 1 = %d \t Var 2 = %d", var1,var2);

    return 0;
}