import time
t = time.strftime('%H:%M:%S')
print(t,"\n")

hour = int(time.strftime('%H'))
# hour = int(input('Enter the Time: '))
print(hour)
if (hour>0 and hour<12):
    print("Good Morning Sir")
elif (hour>=12 and hour<17):
    print("Good Afernoon Sir")
else:
    print("Good Evening/Night Sir")


