#include <stdio.h>
#include <stdlib.h>

void question1() {

    printf("Au revoir !");
    /* Ecrit au revoir à l'écran */

    return;
}

void question2() {

    printf("Salut toi, appuie sur une touche s'il te plait");
    /* Ecrit le texte sur l'écran */

    getchar();
    /* Attente d'une touche pour continuer */

    printf("Merci d'avoir appuyée sur une touche");
    /* Ecrit le texte de rémerciement */

    return;
}

void question3() {
    /* Commentez les précédentes programmes */
    return;
}

void question4() {
    printf("Hamlet says To be or not to be, that is the question");

    return;
}

int main() {

    question4();
    /* Appelle la fonction question3() */

    getchar();
    return 0;
}