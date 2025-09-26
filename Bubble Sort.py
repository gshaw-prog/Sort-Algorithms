# Bubble sort in Python (Source example adapted for function clarity)
def bubble_sort(toSort):
    # Length of the list
    N = len(toSort)
    
    # Outer loop (controls passes)
    for i in range(0, N):
        # Inner loop (compares adjacent elements)
        # N-i-1 optimizes by excluding elements already sorted at the end
        for j in range(0, N - i - 1):
            # Check if current element is greater than the next element
            if toSort[j] > toSort[j+1]: 
                temp = toSort[j]
                toSort[j] = toSort[j+1]
                toSort[j+1] = temp
    
    return toSort

# Example usage provided in the source material:
toSort = [6,10,12,1,45,12,27]
print(bubble_sort(toSort))