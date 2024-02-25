# python program for fifo page replacement
pagelist=[7,0,1,2,0,3,0,4,2,3,0,3]
n=3    # number of frames in main memory
main_mem=[]
hit=0
pagefault=0
for i in pagelist:
    if i in main_mem:
        hit=hit+1
    else:
        if len(main_mem)<3:
            main_mem.append(i)
        else:
            main_mem.pop(0)
            main_mem.append(i)
        pagefault+=1
print("At last, Pages in main memory : ",main_mem) 
print("Number of Hits : ",hit)
print("Number of PageFaults or Miss : ",pagefault)