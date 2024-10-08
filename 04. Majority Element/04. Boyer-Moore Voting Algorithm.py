def boyer_moore_voting_algorithm(arr):
    candidate = None
    count = 0
    

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return None


arr = [2, 2, 1, 1, 1, 2, 2]
majority_element = boyer_moore_voting_algorithm(arr)
print(f"The majority element is: {majority_element}")
