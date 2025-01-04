str1 = "one way"
str2 = 'another way'
str3 =  """"this is third way"""
str4="hey this is shubham.\nwe are using escape sequence character"
print(str4)
#basic operatons

#concatenation
str5="hello"+" world"
print(str5)
#length of str  len(str)
print(len(str5))
#indexing
str6="radharani"
print(str6[0],str6[1],str6[2]) #through indexing access of character is allowed but modificatioin is not allowed
# str[1]='p'  modification not allowed 
#slicing ==accessing parts of string
# str[strating index:ending index]  ending indexing is not included
str7="this is katiyar ,you friend"
str8=str7[0:22]
print(str8)
str9=str7[0:]   #same as str[0:len(str)]
print(str9)