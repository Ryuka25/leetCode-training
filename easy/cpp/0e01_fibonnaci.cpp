/*
    ! Write an algorithm to produce the first 15 numbers of this series: 1,1,2,3,5,8,13,21…
*/

#include <iostream>

using namespace std;

void fibonnaci(int numberOfInstance) {
    /*  
                                    1, 2, 3, 5
seriesOfFibonnaci:                        ^
                                    1, 2, 3, 5
seriesOfFibonnaci_minus_one:           ^
                                    1, 2, 3, 5
seriesOfFibonnaci_minus_two:        ^

seriesOfFibonnaci = seriesOfFibonnaci_minus_one + seriesOfFibonnaci_minus_two
    */
    int seriesOfFibonnaci(1);               // Initialisation for the first iteration
    int seriesOfFibonnaci_minus_one(1);     // Initialisation for the first iteration
    int seriesOfFibonnaci_minus_two;
    
    for (int i = 1; i < numberOfInstance; i += 1) {
        seriesOfFibonnaci_minus_two = seriesOfFibonnaci_minus_one;              // swip index to the next
        seriesOfFibonnaci_minus_one = seriesOfFibonnaci;                        // swip index to the next

        if (i > 1) {
            seriesOfFibonnaci = seriesOfFibonnaci_minus_one + seriesOfFibonnaci_minus_two;
        } else {
            seriesOfFibonnaci = seriesOfFibonnaci_minus_one + 0;                // only act for the first number
        }
        cout << seriesOfFibonnaci << " ";
    }
}

int main() {
    fibonnaci(15);

    return 0;
}