import heapq
def golden_wire(arr):
    heapq.heapify(arr)
    tot_cost=0
    while len(arr)>1:
        w1=heapq.heappop(arr)
        w2=heapq.heappop(arr)
        tot_cost+=(w1+w2)
        heapq.heappush(arr,(w1+w2))
    return tot_cost
arr=list(map(int,input("enter all wires length").split()))
tot_cost=golden_wire(arr)
print("Total cost:",tot_cost)
