class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k]) 
        max_sum = current_sum 

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum = max(current_sum, max_sum)
        return max_sum / float(k)
sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
        