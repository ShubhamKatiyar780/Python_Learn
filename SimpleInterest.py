class SI:
    def __init__(self):
        try:
            self.principle_amount = int(input("Enter your principle amount(in Rs.): "))
            self.rate_of_interest = int(input("Enter rate of interest: "))
            self.year = int(input("Enter year: "))
            self.display()
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    def calculateSI(self):
        return (self.principle_amount * self.rate_of_interest * self.year) / 100
    
    def total_amount(self):
        return (self.calculateSI() + self.principle_amount)
    
    def display(self):
        print(f"Your simple interest is: {self.calculateSI()} rupees.")
        print(f"Your total amount with interest is: {self.total_amount()} rupees.")

obj = SI()