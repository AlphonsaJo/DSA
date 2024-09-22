def bucket_sort(arr):
  
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

