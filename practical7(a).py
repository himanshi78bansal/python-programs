def function(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[0:mid]
        function(left)
        right = arr[mid:]
        function(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
function(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(f"{arr[i]}")
