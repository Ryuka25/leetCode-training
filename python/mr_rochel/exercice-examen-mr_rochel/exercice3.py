class Exo1:

    def __init__(self):
        # What Program are use for
        print("Calcult the fact of a number!")
        # Get number to calculate
        while True:
            number = input("Enter a number : ")
            try:
                number = int(number)
                if number >= 0:
                    break
                else:
                    raise Exception()
            except:
                print("Choose a positive number")
                pass
        # Show fact on the screen
        print(f"{number}! = {self.fact_non_recurs(number)}")

    def fact_recurs(self,number):
        "Calculate fact with recurs methods"
        if (number == 0 or number == 1):
            return 1
        return (number * self.fact_recurs(number-1))

    def fact_non_recurs(self,number):
        "Caculate fact without recurs methods"
        if (number == 0):
            return 1
        else:
            prod = 1
            for i in range(1,number+1):
                prod *= i
        return prod

Exo1()