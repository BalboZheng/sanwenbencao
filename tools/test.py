def binSearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1


a = binSearch([1, 3, 5, 7, 8, 9], 3)
print(a)
