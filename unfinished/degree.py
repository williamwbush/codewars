def degree(arr):
    degree = 0
    for i in range(len(arr)):
        if arr.count(arr[i]) > degree: 
            degree = arr.count(arr[i])
    for i in range(len(arr)):
        for j in range(i):
            deg = 0
            if 