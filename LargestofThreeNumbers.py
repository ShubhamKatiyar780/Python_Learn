class CheckLargestNumber:
    def __init__(self):
        try:
            self.a = int(input("Enter first number: "))
            self.b = int(input("Enter second number: "))
            self.c = int(input("Enter third number: "))
            self.checkNumber()
        except ValueError:
            print("Invalid input! Please enter an integer")

    def checkNumber(self):
        if (self.a > self.b and self.a > self.c):
            print(f"{self.a} is largest number.")
        elif (self.b > self.a and self.b > self.c):
            print(f"{self.b} is largest number.")
        else:
            print(f"{self.c} is largest number.")

    def sumOfDigits(self):
        try:
            self.number = input("Enter a number: ")
            sum_of_digits = 0
            for i in self.number:
                sum_of_digits +=  int(i)  # i convert from string in to the Integer
            print(f"Sum of digits is: {sum_of_digits} ")
        except ValueError:
            print("Invalid input! Please enter an integer")


obj = CheckLargestNumber()
print(obj.sumOfDigits())