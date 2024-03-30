def is_min_heap(arr):
    n=len(arr)
    for i in range(n//2):
        left_child=2*i+1
        right_child=2*i+2

        if left_child < n and arr[left_child]<arr[i]:
            return False
        if right_child < n and arr[right_child]<arr[i]:
            return False
    return True
min_heap_list=[16,15,14,13,12]
if is_min_heap(min_heap_list):
    print(min_heap_list)
    print('min heap =',is_min_heap(min_heap_list))
else:
    print(min_heap_list)
    print('no heap')


def is_max_heap(arr):
    n=len(arr)
    for i in range(n//2):
        left_child=2*i+1
        right_child=2*i+2

        if left_child < n and arr[left_child]>arr[i]:
            return False
        if right_child < n and arr[right_child]>arr[i]:
            return False
    return True

max_heap_list=[16,15,14,13,12]
if is_max_heap(max_heap_list):
    print(max_heap_list)
    print('max heap =',is_max_heap(max_heap_list))
else:
    print(max_heap_list)
    print('no heap')
