#quick sort algorithm
# select divide and conquer algorithm
def quicksort(arr):
    """
    this is not an inplace implementation
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot=arr[-1]
        lesser, equal, greater = [], [], []
        for iter in arr:
            if iter < pivot:
                lesser.append(iter)
            elif iter == pivot:
                equal.append(iter)
            else:
                greater.append(iter)
        
        return quicksort(lesser) + equal + quicksort(greater)
                
    return arr

list=[8,1,4,10,7,6,7,9,3,2,5]
print(quicksort(list))