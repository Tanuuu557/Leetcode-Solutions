class Solution(object):
    def removeStars(self, s):
        self.stack = []
        for char in s:
            if char == "*":
                if not self.isEmpty():
                    self.pop()
            else:
                self.push(char)
        return ''.join(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

sol = Solution()
print(sol.removeStars("leet**cod*e"))
