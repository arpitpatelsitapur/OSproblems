'''Round robin scheduling'''
class Process:
    def __init__(self, name, bt):
        self.name = name
        self.bt = bt
        self.rem_t = bt
        self.wt = 0
        self.tat = 0
def round_robin(processes, TQ):
    n = len(processes)
    ready_queue = processes.copy()
    time = 0
    total_wt = 0
    total_tat = 0
    print("The Running Queue is :")
    while ready_queue:
        cp = ready_queue.pop(0)
        if cp.rem_t <= TQ:
            time += cp.rem_t
            cp.rem_t = 0
            cp.tat = time
            cp.wt = cp.tat - cp.bt
            total_wt += cp.wt
            total_tat += cp.tat
            print(f"{cp.name} ",end="")
        else:
            time += TQ
            cp.rem_t -= TQ
            print(f"{cp.name} ",end="")
            ready_queue.append(cp)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print(f"""\n   Average Waiting Time: {avg_wt}\nAverage Turnaround Time: {avg_tat}""")
processes = [
    Process("P1", 10),
    Process("P2", 5),
    Process("P3", 8),
    Process("P4", 3)
]
TQ = 2
round_robin(processes, TQ)
