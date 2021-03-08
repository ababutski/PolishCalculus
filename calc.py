import sys
# dictionary with operators(keys) and their priority (values)
OPERATORS = {
    '+':0,'-':0,
    '*':1,'/':1,
    'u-': 2,'u+': 2, 
    '(': -1, ')': -1}

# creating Reverse Polish notation
# returns list with tokens. Each token is a string with number or operator.
def to_reverse_polish(str):
    result = []
    stack = []
    # iterate over string characters
    for i,token in enumerate(str):
        # if it's digit
        if token.isdigit():
            # if previous token was a number adding this digit to it
            if i > 0 and str[i-1].isdigit():
                result.append(result.pop() + token)
            # otherwise add as new
            else:
                result.append(token)
        # if it's openening parentheses
        elif token == '(':
            stack.append(token)
        # if it's closing parentheses
        elif token == ')':
            # then moving tokens from stack to result until we meet opening parentheses
            t = stack.pop()
            while t != '(':
                result.append(t)
                t = stack.pop()
        # if it's operator
        elif token in OPERATORS:
            # if prevouse token in input was NOT a digit then current token is unary operator
            if (token == '-' or token == '+') and (i==0 or str[i-1].isdigit() == False):
                # mark as unary
                token = 'u'+token
            # taking priority of current operator
            p0 = OPERATORS[token]
            # moving tokens from stack to result while operators in stack have same or higher priority
            while len(stack) > 0:
                t1 = stack.pop()
                p1 = OPERATORS[t1]
                if p1 >= p0:
                    result.append(t1)
                # returning token back to stack and exiting cycle
                else:
                    stack.append(t1)
                    break
            # finaly adding current token to stack
            stack.append(token)
    # moving tokens left in stack to result
    stack.reverse()
    for token in stack:
        if token == '(' or token == ')':
            result.append('not paired parentheses in expression!')
        result.append(token)
    return result

# Calculates expression in Reverse Polish notation. 
# Returns number
def calc_rpn(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        elif token == '+':
            arg0, arg1 = stack.pop(), stack.pop()
            stack.append(float(arg1) + float(arg0))
        elif token == '-':
            arg0, arg1 = stack.pop(), stack.pop()
            stack.append(float(arg1) - float(arg0))
        elif token == '*':
            arg0, arg1 = stack.pop(), stack.pop()
            stack.append(float(arg1) * float(arg0))
        elif token == '/':
            arg0, arg1 = stack.pop(), stack.pop()
            stack.append(float(arg1) / float(arg0))
        elif token == 'u-':
            arg0 = stack.pop()
            stack.append(-float(arg0))
        # for token == 'u+'  do nothing
    return float(stack.pop())

# reading arguments as single string
line = ''.join(sys.argv[1:])
# removing whitespaces from string
#line = '1+2*3*(2+10)'
line = line.replace(" ", "")
rpn = to_reverse_polish(line)
print(' '.join(rpn))

result = calc_rpn(rpn)
print(result)

