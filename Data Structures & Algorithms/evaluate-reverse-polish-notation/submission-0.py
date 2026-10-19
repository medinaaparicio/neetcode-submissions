import operator
class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:

        # nums will be our stack of ints
        nums = []
        operators = {"+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv}

        if tokens[0] in operators: return "invalid string"
        for token in tokens:
            result = token
            if token in operators:
                second = nums.pop()
                first = nums.pop()
                result = operators[token](first,second)
    
            nums.append(int(result))
        return nums.pop()


        

        