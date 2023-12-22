def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return f"Target Found At {midpoint}"
        elif list[midpoint] > target:
            last = midpoint - 1
        elif list[midpoint] < target:
            first = midpoint + 1
    return None


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(numbers, 5)
print(result)
