def binarySearch_recursive(arr, target, low, high):

    if low > high:
        print("Element Not found")
        return False
    else:
        mid = low + high // 2
        if target == arr[mid]:
            print("Element Found")
            return True
        elif target < arr[mid]:
            return binarySearch(arr, target, low, mid-1)
        else:
            return binarySearch(arr, target, mid-1, high)    
        


arr = [5, 8, 10, 12, 16, 18, 26]

binarySearch_recursive(arr, 16, 0, len(arr) -1 )