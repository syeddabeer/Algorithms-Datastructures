def selectionSort(arr):
    referencePosition = 0
    while referencePosition < len(arr):
        for number in range(referencePosition+1, len(arr), 1):
            if arr[number] < arr[referencePosition]:
                    arr[referencePosition], arr[number] = arr[number], arr[referencePosition]
        referencePosition += 1
        print("result after each iteration:", arr)
       
inputArray = [9, 1, 8, 4, 6, 5, 3, 2, 7]
print("input Array is: ", inputArray)
selectionSort(inputArray)