
def insert_concatenation_operator(regex: str) -> str:
    output = []
    for i, token in enumerate(regex):
        output.append(token)
        if i < len(regex) - 1 and token not in {'(', '|', '.'} and regex[i+1] not in {'*', '+', ')', '|', '.'}:
            output.append('.')
    return ''.join(output)


def infix_to_postfix(infix: str) -> str:
    output = []
    stack = []
    precedence = {'*': 100, '+': 10, '.': 1}
    for token in infix:
        if token in {'a', 'b'}:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    postfix = ''.join(output)
    if postfix[-1] == '.':
        postfix = postfix[:-1]
    return postfix


# main function
def main():
    regex = insert_concatenation_operator(input("Enter a regex in infix notation using only 'a', 'b', '(', ')', '+', '.', and '*': "))
    print(regex)
    print(infix_to_postfix(regex))
    
if __name__ == '__main__':
    main()