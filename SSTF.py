'''SSTF disk scheduling'''
def sstf(arr, head):
    seek_seq = []  
    dist = 0  
    curr_tr = head  
    tracks = arr.copy()
    while tracks:
        shortest_seek = float('inf')
        next_tr = None
        for track in tracks:
            seek = abs(track - curr_tr)
            if seek < shortest_seek:
                shortest_seek = seek
                next_tr = track
        dist += shortest_seek
        curr_tr = next_tr
        seek_seq.append(curr_tr)
        tracks.remove(curr_tr)
    return seek_seq, dist
requests = [176, 79, 34, 60, 92, 11, 41, 114]
starting_track = 50
sequence, total_dist = sstf(requests, starting_track)
print("Sequence of disk access:", sequence)
print("Total seek dist:", total_dist)