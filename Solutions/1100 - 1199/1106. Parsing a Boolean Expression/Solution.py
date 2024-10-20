class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char in ('!', '&', '|'):
                stack.append(char)
            elif char == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  
                operator = stack.pop()
                
                if operator == '!':
                    stack.append(not sub_expr[0])
                elif operator == '&':
                    stack.append(all(sub_expr))
                elif operator == '|':
                    stack.append(any(sub_expr))
            elif char == '(':
                stack.append('(')
        
        return stack[-1]
