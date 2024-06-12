import math
import re


class CalculatorManager:
    OPERATORS = {'+', '-', '*', 'x', '/', '^', '(', ')'}
    REGEX_INPUT = r'^[\d\+\-\*\/\(\)\s]+$'

    def check_regex_and_parentheses(self, input_str):
        regex = re.compile(self.REGEX_INPUT)
        return regex.match(input_str) and self.check_parentheses_match(input_str)

    def check_parentheses_match(self, input_str):
        stack = []
        for char in input_str:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    def convert_infix_to_postfix(self, input_str):
        values = input_str.split()
        output = []
        stack = []
        precedence = {'(': -1, ')': -1, '+': 2, '-': 2, '*': 3, 'x': 3, '/': 3, '^': 4}

        for item in values:
            if item == "":
                break
            if item in precedence:
                if item == ")":
                    while stack and stack[-1] != "(":
                        output.append(stack.pop())
                    if not stack:
                        raise ValueError("Söz dizilimi hatalı")
                    stack.pop()
                elif item == "(":
                    stack.append(item)
                else:
                    while (stack and stack[-1] in precedence and
                           (precedence[item] < precedence[stack[-1]] or
                            (item == "^" and precedence[item] == precedence[stack[-1]]))):
                        output.append(stack.pop())
                    stack.append(item)
            else:
                try:
                    float(item)
                    output.append(item)
                except ValueError:
                    raise ValueError("Söz dizilimi hatalı")

        while stack:
            if stack[-1] in "()":
                raise ValueError("Söz dizilimi hatalı")
            output.append(stack.pop())

        return ' '.join(output)

    def evaluate_postfix_expression(self, input_str):
        values = input_str.split()
        stack = []

        for token in values:
            try:
                stack.append(float(token))
            except ValueError:
                try:
                    right = stack.pop()
                    left = stack.pop()
                    if token == '+':
                        stack.append(left + right)
                    elif token == '-':
                        stack.append(left - right)
                    elif token == '*':
                        stack.append(left * right)
                    elif token == 'x':
                        stack.append(left * right)
                    elif token == '/':
                        stack.append(left / right)
                    elif token == '^':
                        stack.append(math.pow(left, right))
                except IndexError:
                    raise ValueError("Söz dizilimi hatalı")

        return stack.pop()

    def seperate_the_input(self, input_str):
        result = []
        is_number = False

        for char in input_str:
            if char in self.OPERATORS:
                if is_number:
                    result.append(' ')
                    is_number = False
                result.append(char)
                result.append(' ')
            elif char.strip() == '':
                continue
            else:
                result.append(char)
                is_number = True

        return ''.join(result).strip()
