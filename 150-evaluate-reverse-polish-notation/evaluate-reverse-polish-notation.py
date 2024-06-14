class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        stack = []

        for el in tokens:
            if el in ops:
                stack.append(self.calc(stack.pop(), stack.pop(), el))
            else:
                stack.append(int(el))
        
        return stack[0]


    def calc(self, b, a ,op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return int(a/b)
