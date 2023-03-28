def infix_2_postfix(input):
    operators = "^*/+-()"
    pe = {'^': 4, '*': 2, '/': 2, '+': 1, '-': 1, '(': 5}
    ps = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    stack = []
    res = []
    for id, c in enumerate(input):
        if c in operators:
            
            if len(stack) < 1:
                stack.insert(0, c)
                continue
            if c == ')':
                while stack[0] != '(':
                    res.insert(0, stack.pop(0))
                stack.pop(0)
                continue
            if pe[c] > ps[stack[0]]:
                stack.insert(0, c)
                continue
            
            flag = False
            while not flag:
                if len(stack) < 1: break
                if pe[c] <= ps[stack[0]]:
                    flag = True
                res.insert(0, stack.pop(0))
            stack.insert(0, c)
            continue
        
        if id >=1 and input[id-1].isnumeric():
            res[0] += c
        else:
            res.insert(0, c)

    while stack:
        res.insert(0, stack.pop(0))

    res.reverse()

    return res

def solve_postfix(input):
    stack = []
    for e in input:
        if e == '^':
            b = int(stack.pop(0))
            a = int(stack.pop(0))

            stack.insert(0, a**b)
            continue
        if e == '*':
            b = int(stack.pop(0))
            a = int(stack.pop(0))

            stack.insert(0, a*b)
            continue
        if e == '/':
            b = int(stack.pop(0))
            a = int(stack.pop(0))

            stack.insert(0, a/b)
            continue
        if e == '+':
            b = int(stack.pop(0))
            a = int(stack.pop(0))

            stack.insert(0, a+b)
            continue
        if e == '-':
            b = int(stack.pop(0))
            a = int(stack.pop(0))

            stack.insert(0, a-b)
            continue
    
        stack.insert(0, e)
    
    return int(stack[0])

def calculate(input):
    return solve_postfix(infix_2_postfix(input))

input = "(5*1+4+1/2)^3"
print(infix_2_postfix(input))
print(calculate(input))


    