class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x, token in enumerate(tokens):
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else: 
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                if token == "-":
                    stack.append(-stack.pop() + stack.pop())
                if token == "*":
                    stack.append(stack.pop() * stack.pop())
                if token == "/":
                    temp = stack.pop()
                    stack.append(int(stack.pop() / temp))
            #print(stack)
        return stack[0]