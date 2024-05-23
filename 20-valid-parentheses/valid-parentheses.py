class Solution(object):
    def isValid(self, s):               
        openings = '([{'
        stack = []
        for c in s:
            if c in openings:
                stack.append(c)            
            else:
                if not stack or \
                    (c == ")") and stack[-1] != "(" or \
                    (c == "]") and stack[-1] != "[" or \
                    (c == "}") and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack
            
        