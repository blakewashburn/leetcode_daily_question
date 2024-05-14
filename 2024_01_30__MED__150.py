"""
Title: 
150. Evaluate Reverse Polish Notation

Description: 
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
    Evaluate the expression. Return an integer that represents the value of the expression.
    Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

Constraints:
    1 <= tokens.length <= 10^4
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""

import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        # push operands onto stack, pop 2 when we get an operator, and push result back onto stack

        stack = []
        operators = frozenset(["+", "-", "*", "/"])
        for token in tokens:

            # determine operator or operand
            if token not in operators:

                # add the operand to the stack
                stack.append(int(token))

            else:

                # grab the two most recent operands
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                # perform operator and push result back to stack
                if token == "+":
                    stack.append(operand_1 + operand_2)
                elif token == "-":
                    stack.append(operand_1 - operand_2)
                elif token == "*":
                    stack.append(operand_1 * operand_2)
                else:

                    # ensure that we round towards zero 
                    temp = operand_1 / operand_2
                    if temp > 0:
                        stack.append(math.floor(temp))
                    else:
                        stack.append(int(-1 * math.floor(-1 * temp)))

        return stack.pop()


if __name__ == "__main__":
    sol = Solution()
    
    tokens = ["2","1","+","3","*"]          # -> 9
    # tokens = ["4","13","5","/","+"]         # -> 6
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]          # -> 22

    print(sol.evalRPN(tokens=tokens))
