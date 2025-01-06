# for loop
for i in range(1,21,2):
    print(i)

for j in range(21,0,-2):
    print(j)


# while loop increment
a=0
while(a<=10):
    print(a)
    a+=1
print("Done")


# decrement loop
b=20
while(b>=1):
    print(b)
    b-=1

k=0
while True:
    print(i)
    i+=1
    if(i%10==0):
        break
    
    
# Break and Continue
for i in range(15):
    if(i==10):
        continue   #   break=break the loop
    print("5 X",i+1, "=", 5*(i+1))
for i in range(15):
    if(i==10):
        break      #   continue=skip the iteration
    print("7 X",i+1, "=", 7*(i+1))
