class Solution(object):
    def removeDuplicates(self, nums):
        size = len(nums)
        pointer = 0
        while (pointer < size):
            if nums[pointer] == nums[pointer + 1]:
                nums.pop(pointer)
                pointer-=1

            pointer = pointer + 1
            size = len(nums) - 1

        return len(nums)




