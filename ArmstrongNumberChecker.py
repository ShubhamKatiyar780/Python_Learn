a = input("Enter a number: ")
b = 0
for i in a:
    b += int(i)**3
    # c = int(i)**3
    # print(f" {i} X ^3= {c}")
if (a == str(b)):
    print(f"{a} is an Armstrong Number.")
else:
    print(f"{a} is not an Armstrong Number.")