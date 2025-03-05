def find_closest_sum_triplet(arr):
    if len(arr) < 3:
        return None

    arr.sort()
    closest_sum = float('inf')
    closest_triplet = (None, None, None)

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                closest_triplet = (arr[i], arr[left], arr[right])

            if current_sum < 0:
                left += 1
            else:
                right -= 1

    return closest_triplet

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
print(find_closest_sum_triplet(arr))
