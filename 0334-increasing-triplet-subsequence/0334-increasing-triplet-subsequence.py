class Solution(object):
    def increasingTriplet(self, nums):
        j = float('inf')
        k = float('inf')
        for i in nums:
            if i <= j:
                j = i
            elif i <= k:
                k = i
            else:
                return True
        return False
sol = Solution()
print(sol.increasingTriplet([1, 2, 3, 4, 5]))

        