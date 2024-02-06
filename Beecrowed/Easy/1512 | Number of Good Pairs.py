# Formula is nums[i]==nums[j] and i<j
# so easy step to solve
class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count = count + 1
