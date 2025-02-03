# def checkFormatOfPassword():
#     while True:
#         a,b,c,d = 0,0,0,0
#         password = input("Enter Your pass: ")
#         capital_lettar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         small_letter = "abcdefghijklmnopqrstuvwxyz"
#         special_letter = "!@#$%^&*"
#         digits = "0123456789"

#         if (len(password) >= 8):
#             for i in password:
#                 if (i in capital_lettar):
#                     a += 1
#                 if (i in small_letter):
#                     b += 1
#                 if (i in digits):
#                     c += 1
#                 if (i in special_letter):
#                     d += 1
#             if (a>=1 and b>=1 and c>=1 and d>=1):
#                 print("valid password")
#                 break
#             else:
#                 print("Password must include: ")
#                 if a == 0:
#                     print("- At least one Capital Letter (A-Z)")
#                 if b == 0:
#                     print("- At least one Small Letter (a-z)")
#                 if c == 0:
#                     print("- At least one Numeric Digit (0-9)")
#                 if d == 0:
#                     print("- At least one Special Character (!@#$%^&*)")
#         else:
#             print("Password must be at least 8 characters long.")

        
# def checkFormatOfEmail():
#     while True:
#         email = input("Enter Your Email-Id: ")
        
#         if "@" in email and "." in email:
#             at_index = email.index("@")
#             dot_index = email.rindex(".")  
#             domain = email[at_index :]
#             if at_index < dot_index and domain == "@gmail.com":
#                 print("Your Email-id is valid")
#                 break
#             else:
#                 print("Please provide a valid Gmail ID ending with '@gmail.com'")
#         else:
#             print("Please provide a valid Email-ID")

# checkFormatOfEmail()
# checkFormatOfPassword()

import getpass
import pwinput
def register():
    print("User Registrain")
    name=input("Enter your name: ")
    email=input("Enter your Email:")
    # password=getpass.getpass("Enter your password: ")
    password=pwinput.pwinput("Enter your password: ", mask='*')
    file=open("login.csv",'a')
    file.write(f"{name},{email},{password}\n")
    file.close()
    print("Registration Done")


def login(email,password):
    file=open("login.csv",'r')
    for line in file:
        details=line.strip().split(",")
        stored_email=details[1]
        stored_password=details[2]
    if email==stored_email and password==stored_password:
        return True
    return False


def countAtt():
    maxatt=2
    att=0
    while att < maxatt:
        email=input("Enter your email: ")
        # password=input("Enter your password: ")
        password=pwinput.pwinput("Enter your password: ", mask='*')
        if login(email, password):
            print("login successful")
            break
        else:
            att += 1
            print(f"login failed. {maxatt - att} attempts left!")
    if maxatt == att:
        print("try after 24 hours")



# def login():
#     print("User Login")
#     email=input("Enter your email: ")
#     password=input("Enter your password: ")
#     file=open("login.csv",'r')
#     for line in file:
#         details=line.strip().split(",")
#         stored_email=details[1]
#         stored_password=details[2]
#     if email==stored_email and password==stored_password:
#         print("Login successeful!")
#         # getAPI()
#         return
#     print("User credentials not correct")

register()
# login()
countAtt()