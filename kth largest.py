import heapq
def findkthlargest(arr,k):
    arr=[-num for num in arr]
    heapq.heapify(arr)
    for x in range(k):
        d=heapq.heappop(arr)
    return -d
arr=[3,2,1,5,6,4]
print(arr)
k=int(input())
print(f"{k}nd largest is",{findkthlargest(arr,k)})
