class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")

        current_vowels = sum(1 for char in s[:k] if char in vowels)
        max_vowels = current_vowels

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowels -= 1

            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(current_vowels, max_vowels)

        return max_vowels

sol = Solution()
print(sol.maxVowels("abciiidef", 3))