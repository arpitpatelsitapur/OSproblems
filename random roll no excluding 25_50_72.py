import random
def rollno():
    randno=random.randint(1,75)
    if randno==25 or randno==50 or randno==72:
        rollno()
    else:
        return randno
n=int(input("Enter how many Roll numbers do you want : "))
for i in range(1,n+1):
    print(rollno(),end=" ")