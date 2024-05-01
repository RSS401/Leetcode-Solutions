class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter in "({[":
                stack.append(letter)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if letter == ')' and top != '(':
                    return False
                elif letter == '}' and top != '{':
                    return False
                elif letter == ']' and top != '[':
                    return False

        return len(stack) == 0

