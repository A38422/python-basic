# VD1
def sum(arr, size):
    if size == 0:
        return 0
    size -= 1
    return arr[size - 1] + sum(arr, size)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(arr)
print(sum(arr, size))

# VD2
def ThapHaNoi(num, c1, c2, c3):
    if num == 1:
        print(c1 + " -> " + c3)
    else:
        ThapHaNoi(num - 1, c1, c3, c2)
        ThapHaNoi(1, c1, c2, c3)
        ThapHaNoi(num - 1, c2, c1, c3)

ThapHaNoi(5, 'A', 'B', 'C')

# tinh de quy day fibonacci
def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))