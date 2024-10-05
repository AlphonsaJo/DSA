def count_triplets(arr):
    count = 0
    n = len(arr)
    arr.sort()  # Sort the array to make it easier to check for triplets

    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1

        while j < k:
            if arr[j] + arr[k] == arr[i]:
                count += 1
                j += 1
                k -= 1
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1

    return count

# Example usage
arr = [3, 4, 1, 5, 2]
result = count_triplets(arr)
print("Number of triplets:", result)
