class Fibonacci:
    def __init__(self):
        self.number = int(input("Enter a number: "))
        self.createSequence()

    def createSequence(self):
        a , b = 0, 1
        print(f"Your Fibonacci Series with {self.number} term is: ")
        for i in range(self.number):
            print(a , end=" ")
            a , b = b , a + b

obj = Fibonacci()