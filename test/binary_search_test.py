# 二分查找
def binary_search(numbers, search_number):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_number:
            return mid
        elif numbers[mid] > search_number:
            high = mid - 1
        elif numbers[mid] < search_number:
            low = mid + 1
    return None


numbers = [1, 3, 6, 9, 100, 108, 200, 202]
print(binary_search(numbers, 101))
