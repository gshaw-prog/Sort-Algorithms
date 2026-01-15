arr = [12,3,45,6,1,22,16]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr [0]
    less = [x for x in arr[1:] if x <= pivot]
    print(arr)
    greater = [x for x in arr[1:] if x > pivot]
    print(arr)
    return quicksort(less) + [pivot] + quicksort(greater)

sorted = quicksort(arr)

print (sorted) 