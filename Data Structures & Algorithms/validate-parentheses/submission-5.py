class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = [] * (len(s)//2)
        for x, char in enumerate(s):
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if not stack: return False
                pair = stack.pop()
                if char == ')' and pair != '(': return False
                if char == '}' and pair != '{': return False
                if char == ']' and pair != '[': return False
        return not stack

    #didnt consider only open brackets left in stack at end
    #popping from empty
    #think through all cases first

        #after open bracket, expecting some open bracket or corresponding closed bracket

