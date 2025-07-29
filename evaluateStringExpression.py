import re

def splitExpressionIntoArray(expression):
    split_array = re.split(r"([+-/*()\^])", expression)
    result = [s for s in split_array if s.strip()]
    return result

def evaluateAdditionAndSubtraction(input_expression):
    expression = input_expression
    while '-' in expression or '+' in expression:
        for i in range(0, len(expression)):
            if expression[i] == '+':
                expression[i] = int(expression[i - 1]) + int(expression[i + 1])
                expression.pop(i - 1)
                expression.pop(i)
                break
            if expression[i] == '-':
                expression[i] = int(expression[i - 1]) - int(expression[i + 1])
                expression.pop(i - 1)
                expression.pop(i)
                break
    return expression

def evaluateMultiplicationAndDivision(input_expression):
    expression = input_expression
    while '*' in expression or '/' in expression:
        for i in range(0, len(expression)):
            if expression[i] == '/':
                expression[i] = int(expression[i - 1]) / int(expression[i + 1])
                expression.pop(i - 1)
                expression.pop(i)
                break
            if expression[i] == '*':
                expression[i] = int(expression[i - 1]) * int(expression[i + 1])
                expression.pop(i - 1)
                expression.pop(i)
                break
    return expression

def evaluateExponents(input_expression):
    expression = input_expression
    while '^' in expression:
        for i in range(0, len(expression)):
            if expression[i] == '^':
                expression[i] = int(expression[i - 1]) ** int(expression[i + 1])
                expression.pop(i - 1)
                expression.pop(i)
                break
    return expression

def evaluateAll(expression):
    result = expression
    if '(' in expression and ')' in expression:
        for i in range(0, len(expression)):
            if expression[i] == '(':
                start = i
            if expression[i] == ')':
                end = i
                return evaluateAll((evaluateAll(expression[start + 1:end]) + expression[end + 1:]))
    else:
        result = evaluateExponents(result)
        result = evaluateMultiplicationAndDivision(result)
        result = evaluateAdditionAndSubtraction(result)
        return result

def fullEvaluate(string_expression):
    array_expression = splitExpressionIntoArray(string_expression)
    result = evaluateAll(array_expression)
    return int(result[0])

def main():
    my_expression = "(100+30)/5^2*7"
    print(fullEvaluate(my_expression))

if __name__ == '__main__':
    main()