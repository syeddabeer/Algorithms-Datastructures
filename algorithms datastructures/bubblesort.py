def bubbleSort(arr):
    swapFlag = True
    while swapFlag:
        swapFlag = False
        for num in range(0, len(arr)-1, 1):
            if arr[num] > arr[num+1]:
                swapFlag = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
        print("\niteration of swaps leads to: ", arr)
            
inputArray = [9, 1, 8, 4, 6, 5, 3, 2, 7]
print("inputArray is: ", inputArray)
bubbleSort(inputArray)