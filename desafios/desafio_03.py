# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python
# Nao vale usar o .sort()

def solution(*nums):
    nums = nums[0]
    
    if not nums or None in nums:
        return []
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
    return nums
