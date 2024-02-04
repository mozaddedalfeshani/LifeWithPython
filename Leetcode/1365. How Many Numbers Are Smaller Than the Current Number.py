class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        #give me List of numbers [8,1,2,2,3]
        #return me List of numbers [4,0,1,1,3]
        """
        count = 0
        newList = []
        for i in nums:
            for j in nums:
                if i < j:
                    count += 1
            newList.append(count)

        return newList


a = Solution()
print(a.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
