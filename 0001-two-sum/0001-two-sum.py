class Solution(object):
    def twoSum(self, nums, target):
        seen= {}
        for i,num in enumerate(nums):
            temp = target - num

            if temp in seen:
                return [seen[temp],i]

            seen[num]=i
        return []
nums=[2, 7, 11, 15]
sol = Solution()
print(sol.twoSum(nums,9))


        