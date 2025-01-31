class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} + {self.img}i")

# create simple method for add two complex number
    # def addComplex(self, num1, num2):
    #     new_real = num1.real + num2.real
    #     new_img = num1.img + num2.img
    #     return Complex(new_real, new_img)

# using dunder function() 
    def __add__(num1, num2):
        new_real = num1.real + num2.real
        new_img = num1.img + num2.img
        return Complex(new_real, new_img) 
    def __sub__(num1, num2):
        new_real = num1.real - num2.real
        new_img = num1.img - num2.img
        return Complex(new_real, new_img)
    def __mul__(num1, num2):
        new_real = num1.real * num2.real
        new_img = num1.img * num2.img
        return Complex(new_real, new_img)
    

num1 = Complex(4, 5)
num1.showNumber()
num2 = Complex(2, 3)
num2.showNumber()

# sum = num1.addComplex(num1, num2)
sum = num1 + num2
sum.showNumber()
subtract = num1 - num2
subtract.showNumber()
multi = num1 * num2
multi.showNumber()