# Selection sort in Python (Source example adapted for function clarity)
def selection_sort(toSort):
    N = len(toSort)
    
    # Outer loop (controls the number of elements correctly placed)
    for i in range(0, N - 1):
        # Initialize lowestIndex to the start of the unsorted subarray
        lowestIndex = i 
        
        # Inner loop finds the index of the minimum element in the remaining list
        for j in range(i + 1, N): 
            if (toSort[j] < toSort[lowestIndex]): 
                lowestIndex = j 
        
        # Swap the found minimum element with the element at position i
        temp = toSort[lowestIndex] 
        toSort[lowestIndex] = toSort[i] 
        toSort[i] = temp 
    
    return toSort

# Example usage provided in the source material:
toSort = [6,10,56,72,12,4,26,17] 
print(selection_sort(toSort))