class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashy = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in hashy:
                if(stack and hashy[i]==stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0