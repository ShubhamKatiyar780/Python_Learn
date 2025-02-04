# If, If-else, If-elif-else, nested if-elif-else

# if_else
'''
a=int(input("Enter your Age: "))
if(a>=18):
    print("You can drive!")
else:
    print("You can not drive!")
print("Your age is",a, "years")
print(f"Your age is {a} years") # Formatting String
'''

# if-elif-else
'''
number=int(input("Enter a Number: "))
if(number<0):
    print(f"Number {number} is negative.")
elif(number==0):
    print("Number is Zero.")
elif(number%100==0):
    print(f"Number {number} is multiple of 100")
else:
    print(f"Number {number} is positive.")
print("I am happy Now!")
'''

# nested if-elif-else
number1=int(input("Enter a Number: "))
if(number1<0):
    print(f"Number {number1} is negative.")
elif(number1>0):
    if(number1<=10):
        print(f"Number {number1} is between 1-10.")
    elif(number1>10 and number1<=20):
        print(f"Number {number1} is between 11-20.")
    else:
        print(f"Number {number1} is greater than 20.")
else:
    print("Number is Zero.")
