#Bankers algorithm
n = 5  #number of processes
r = 3  #number of resources
alloc = [[1,1,2],
         [2,1,2],
         [4,0,1],
         [0,2,0],
         [1,1,2]]  
max = [[4,3,3],
       [3,2,2],
       [9,0,2],
       [7,5,3],
       [0,0,0]]  
avail = [2, 1, 0]  
finish = [0] * n #list of size n with value 0(false) 
safe_seq = []  
ind = 0
need = []
work = avail
for i in range(n):
    need.append([])
    for j in range(r):
        need[i].append(max[i][j] - alloc[i][j])
for i in range(5):
    for j in range(n):
        if finish[j] == 0:
            flag = 0
            for k in range(r):
                if need[j][k] > work[k]:
                   flag = 1
                   break
            if flag == 0:
                safe_seq.append(j)  # Add process to safe sequence
                ind += 1
                for l in range(r):
                    work[l] += alloc[j][l]
                finish[j] = 1
print("The SAFE Sequence : ",end="")
print(safe_seq)