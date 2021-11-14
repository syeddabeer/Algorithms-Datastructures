# Function to do insertion sort
def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for main_index in range(1, len(arr)):
  
        reference_value = arr[main_index]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        working_index = main_index-1
        while working_index >=0:
            if arr[working_index+1]<arr[working_index]:
                arr[working_index+1], arr[working_index] = arr[working_index], arr[working_index+1]
            working_index -= 1

  
  
# Driver code to test above
arr = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
insertionSort(arr)
print ("Sorted array is:")
print(arr)


