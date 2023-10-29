nums = [1, 2, 2, 1, 5, 3, 2, 3]

nums.sort()
print()
print(nums)
cought = nums[0]
nums[0] = -1
size = len(nums)
for i in range(1, size):
    if cought == nums[i]:
        nums[i] = -1
        nums[i-1]= -1

    else:
        cought = nums[i]
        nums[i] = -1


print(nums)
print()
print()
