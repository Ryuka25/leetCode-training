#include <stdio.h>
#include <stdlib.h>

void question1() {

    puts("Au revoir "); /* Affiche Au revoir */
    getchar ();

    return;
}

void question2() {

    puts ("Salut toi, appuie sur une touche s’il te plaît");
    /* Affiche le message Salut toi, ... s’il te plaît */

    getchar (); /* Attend la frappe d’une touche */

    puts ("Merci d’avoir appuyé sur une touche");
    /* Affiche le message Merci d’avoir appuyé sur une touche */

    return;
}

void question3() {
    /* Commentez les précédentes programmes */
    return;
}

void question4() {

    puts ("Hamlet says To be or not to be, that is the question.");
    
    getchar();
    return;
}

int main() {

    question4();
    /* Appelle la fonction question3() */

    getchar();
    return 0;
}