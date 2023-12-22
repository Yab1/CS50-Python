def linear_search(data, target):
    for i in range(0, len(data)):
        if data[i] == target:
            return f"Target Found at {i}"
    return "Target Not Found"


char_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
result = linear_search(char_list, "E")
print(result)
