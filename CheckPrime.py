class Prime:
    def __init__(self):
        try:
            self.number = int(input("Enter a Number: "))
            if self.number == 0 or self.number == 1:
                print(f"Please provide the number should be greater than 2.")
            elif self.number == 2:
                print(f"{self.number} is a smallest Prime Number.")
            else:
                if self.checkPrime():
                    print(f"{self.number} is not a Prime Number.")
                else:
                    print(f"{self.number} is a Prime Number.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    def checkPrime(self):
        for i in range(2, self.number):
            if self.number % i == 0:
                return True
        return False
            
obj = Prime()