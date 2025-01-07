# # Valiables
# a=10
# b=11.5
# c="Shubham"
# d=None
# e=complex(4,5)
# f=True
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print("The Type of a is ", type(a))
# print("The Type of a is ", type(b))
# print("The Type of a is ", type(c))
# print("The Type of a is ", type(d))
# print("The Type of a is ", type(e))
# print("The Type of a is ", type(f),"\n")

# # list ordered collection of data 
# list=[8,2.3,[-4,+5],["Apple",'Banana']]
# print(list)

# # Tuple immutable
# tuple=(("parrot", "sparrow"), ("lion","tiger"))
# print(tuple)

# # Dictionary map data
# dict={"name":"Shubham","age":20,"convote":True}
# print(dict,"\n")

# Operators Arithmetic, Assignment, Comparison, Logical, Bitwise
# Arithmetic
print(15+6)
print(15-6)
print(15*6)
print(13/6) # Fraction value
print(15//6) # integer value
print(15%6)
print(2**6,"\n") # Exponential
# Bitwise
print(15&10) # AND 
print(15|10) # OR
print(15^10) # XOR  same pr 0 aur others pr 1
print(~15) # NOT -(15+1)=-16
print(5<<2) # Left sifting
print(5>>2,"\n") # Right sifting

# Typecasting
# explicit 
string="15"
number=7
string_number=int(string)
sum=number + string_number
print(sum,"\n")
# emplicit
a=1.9 # float
b=7 # int
print(a+b) # automatic typecasting by python    result is float

'''
a=input("Enter first number: ")
b=input("enter secont number: ")
print(a+b) # because input and print function is always string type
print(int(a)+int(b)) # Typecasting method

a=int(input("Enter first number: "))
b=int(input("enter secont number: "))
print(a+b,"\n")
'''

# String and Slicing
name = "SHUBHAM Katiyar" # immutable
print("Lets use a for loop")
for cha in name:
    print(cha)
print(len(name))
print(name[0:5]) # including 0 but not 5
print(name[:-3]) # [0:(len(name))-3)]  automatically
print(name[:]) # [0:15]
print(name[-7:-2],"\n") # [15-7:15-2]

# String Methods
print(name.upper()) #1
print(name.lower()) #2
name1="!!!!@#Shubham Katiyar#@!!!!!!"
print(name1.rstrip("!@")) #3 rstrip() removes any trailing characters from last side
print(name1.replace("Shubham","Rajat")) #4 replace() replace all occurences of a string
print(name.split(" ")) #5 split() convert in to a list, split the string at the whitespace
name2="this IS my Output"
print(name2.capitalize())#6 capitalize() only first character of the string to uppercase and the rest other characters are lower case
print(len(name2))
print(name2.center(50,".")) #7 center() aligns the string to the center as per the parameters given by the users
print(len(name2.center(50))) # 16spaces string(17) 17spaces = 50
print(name2.count("t")) #8 count() no. of times given value has occured within the given string
print(name2.endswith("put")) #9,10 endswith() or startswith() return boolean type
print(name2.endswith("my", 3,10)) # check a value in btw the string by providing start and end index positions
print(name2.find("p")) #11 find() search for the first occurence if not present then show -1
print(name2.index("I")) #12 index() if not present then show the error
name3="WelcomeToTheConsole12345"
print(name3.isalnum()) #13 isalnum() consists only alphanumeric A-Z, a-z, 0-9 return True False
print(name3.isalpha()) #14 isalpha() consists only A-Z, a-z return True False
print(name3.islower(),"\n") #15,16 islower() or isupper() return True False
name4="Shubham\n"
print(name3.isprintable()) #17 isprintable() check string are printable or not return True False
print(name4.isprintable(),"\n") # false because of \n
name5=" "
print(name5.isspace()) #18 isspace() contains white spaces using tab or spacebar return true false
name6=" dg"
print(name6.isspace(),"\n")
print(name1.istitle()) #19 istitle() first letter of each word of the string is capitalized return true false
print(name2.istitle())
name7="my namE is Shubham katiyAR"
print(name7.title(),"\n") #20 title() capitalizes each letter of the word within the string
print(name.swapcase(),"\n") #21 swapcase() changes the character upper to lower and lower to upper



