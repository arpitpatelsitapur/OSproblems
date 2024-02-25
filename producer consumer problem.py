# producer consumer problem
def up(x):
    x=x+1
    return x
def down(x):
    while x>=0:
        x=x-1
        return x
n=5 #buffer size
buffer=[0]*n
empty=n
full=0
while (True):
    print("--------------------------------------------------")
    print(f"Empty : {empty}  Full : {full}")
    i=int(input("Select one of below:\n1.Produce\n2.Consume\n"))
    if i==1:
        #produce
        if empty!=0:
            buffer[full]=int(input("Enter data : "))
            empty=down(empty)
            full=up(full)
        else:
            print("The Buffer is full. Consume data first.")
    elif i==2:
        #consume
        if full>0:
            full=down(full)
            print(f"The data is {buffer[full]}") 
            empty=up(empty)
        else:
            print("Buffer is empty. Produce data first.")
    else:
        break