class Solution(object):
    def uniqueOccurrences(self, arr):
        seen = {}
        for a in arr:
            if a in seen:
                seen[a] += 1
            else:
                seen[a] = 1

        if len(set(seen.values())) != len(set(arr)):
                return False
        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
        