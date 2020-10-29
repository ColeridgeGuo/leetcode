def removeDuplicates(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def removeDuplicates2(nums):
    if len(nums) == 0: return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    return i+1


print(removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
