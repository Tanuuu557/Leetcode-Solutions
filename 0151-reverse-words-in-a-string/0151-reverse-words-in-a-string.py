class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words = words[::-1]
        return " ".join(words)
sol = Solution()
print(sol.reverseWords("the sky is blue"))
        