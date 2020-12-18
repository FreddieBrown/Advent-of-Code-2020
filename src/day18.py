import re


def p1(data):
    precedence = {
        "+": 1,
        "*": 1
    }
    outputs = []
    for equation in data:
        equation = equation.replace(" ", "")
        outputs.append(eval(shunting_yard(equation, precedence)))
    return sum(outputs)


def p2(data):
    precedence = {
        "+": 2,
        "*": 1
    }
    outputs = []
    for equation in data:
        equation = equation.replace(" ", "")
        outputs.append(eval(shunting_yard(equation, precedence)))
    return sum(outputs)


def shunting_yard(equation, precedence):
    regex = re.compile(r'^[0-9]+$')
    output_stack = []
    op_stack = []
    equation = list(equation)
    for char in equation:
        if regex.match(char):
            output_stack.append(int(char))
        elif char == "+" or char == "*":
            while (len(op_stack) != 0) and (op_stack[-1] != "(") and (precedence[op_stack[-1]] >= precedence[char]):
                output_stack.append(op_stack.pop())
            op_stack.append(char)
        elif char == "(":
            op_stack.append(char)
        elif char == ")":
            while op_stack[-1] != "(":
                output_stack.append(op_stack.pop())
            op_stack.pop()
    while len(op_stack) != 0:
        output_stack.append(op_stack.pop())

    return output_stack


def eval(input):
    ops = {
        "+": (lambda a, b: a + b),
        "*": (lambda a, b: a * b),
    }

    stack = []
    for token in input:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


data = open('data/day18.txt', 'r').read().split("\n")

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
