# memory allocation algorithms
def firstfit(mem_arr,proc_size):
    for i in mem_arr:
        if proc_size<=i:
            print(f"Process allocated to partitioned memeory of size {i}")
            break
def bestfit(mem_arr,proc_size):
    mem_arr.append(0)
    for i in range(len(mem_arr)):
        if abs(mem_arr[i]-proc_size)<abs(mem_arr[i+1]-proc_size):
            print(f"Process allocated to partitioned memeory of size {mem_arr[i]}")
            break
def worstfit(mem_arr,proc_size):
    max=proc_size
    for i in mem_arr:
        if i > max:
            temp=i
    temp=i
    print(f"Process allocated to partitioned memeory of size {temp}")
mem_arr=[200,400,600,700,800,1250] #memory blocks are sorted in increasing order
print(f"Size of Memory Blocks available : {mem_arr}")
a=int(input("Enter which operation you want to perform :\n1.First Fit memeory allocation\n2.Best Fit memeory allocation\n3.Worst Fit memeory allocation\nYour choice : "))
proc_size=550
if a==1:
    firstfit(mem_arr,proc_size)
elif a==2:
    bestfit(mem_arr,proc_size)
else:
    worstfit(mem_arr,proc_size)