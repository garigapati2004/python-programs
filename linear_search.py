def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Input and output
data = [10, 25, 30, 45, 50]
target = int(input("Enter the element to search for: "))    # Taking input from the user to search for the element
result = linear_search(data, target)

print(f"Element found at index {result}" if result != -1 else "Element not found.")


# Another way to implement linear search algorithim

data = [10, 25, 30, 45, 50]
target = int(input("Enter the element to search for: "))
result = next((i for i, x in enumerate(data) if x == target), -1)
print(f"Element found at index {result}" if result != -1 else "Element not found.")
