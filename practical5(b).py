def function(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

arr = [19, 12, 15, 1, 29]
function(arr)
print("Sorted array is:")
for i in range(len(arr)):
    #print("%d" % arr[i])
    print(f"{arr[i]}")
