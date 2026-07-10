class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in paren:
                if stack and stack[-1] == paren[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        print(stack)
        return True if not stack else False
            