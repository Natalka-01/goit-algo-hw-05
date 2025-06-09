def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]  # кандидат у верхню межу
            high = mid - 1

    return (iterations, upper_bound)

arr = [0.5, 1.2, 2.4, 3.8, 5.0, 6.3]
x = 4.0
print(binary_search(arr, x))  

x = 6.3
print(binary_search(arr, x))  

x = 7.0
print(binary_search(arr, x)) 
