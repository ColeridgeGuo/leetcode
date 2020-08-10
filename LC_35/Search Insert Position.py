""" Given a sorted array and a target value,
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    Assume no duplicates in the array
"""


def searchInsert(nums, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    return len(nums)


def searchInsert_2(nums, target) -> int:
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low)//2
        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1
    return low
    
    
print(searchInsert([1, 3, 5, 6], 0))
print(searchInsert_2([1, 3, 5, 6], 7))
