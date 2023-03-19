import graphviz

# globalCounter = 0

# class State:
#     def __init__(self):
#         self.label = globalCounter
#         globalCounter += 1
#         self.isAccepted = False
#         self.left = None
#         self.right = None
    
#     def __init__(self, isAccepted) -> None:
#         self.label = globalCounter
#         globalCounter += 1
#         self.isAccepted = isAccepted
#         self.left = None
#         self.right = None

    
# class NFATree:
#     def __init__(self, transition):
#         self.root = (State(), transition)
#         self.isVisited = False


#     def addState(self, transition, isAccepted):
#         if self.root == None:
#             self.root = State(isAccepted)
#             return
#         else:
#             self.addStateRec(self.root, transition, isAccepted)
    
def shunting_yard(regex):
    output_queue = []
    operator_stack = []

    # Define the precedence of the operators
    precedence = {'*': 3, '.': 2, 'U': 1}

    # Convert the regex string to a list of tokens
    tokens = list(regex)

    for token in tokens:
        if token in {'a', 'b', 'A', 'E'}:
            # If the token is a character, add it to the output queue
            output_queue.append(token)
        elif token == '(':
            # If the token is a left parenthesis, push it onto the operator stack
            operator_stack.append(token)
        elif token == ')':
            # If the token is a right parenthesis, pop operators off the stack until a left parenthesis is found
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Pop the left parenthesis off the stack
        elif token in {'U', '*', '.'}:
            # If the token is an operator, pop operators off the stack until an operator with lower precedence is found
            while operator_stack and operator_stack[-1] != '(' and precedence[operator_stack[-1]] >= precedence[token]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)

    # Pop any remaining operators off the stack and add them to the output queue
    while operator_stack:
        output_queue.append(operator_stack.pop())

    return ''.join(output_queue)

def addPoints(regex: str):
    regex = list(regex)
    alphabet = {'a', 'b', 'A', 'E'}
    for i in range(len(regex)-1):
        if regex[i] in alphabet and regex[i+1] in alphabet:
            regex[i] = regex[i] + '.'
        elif regex[i] == '*' and regex[i+1] in alphabet:
            regex[i] = regex[i] + '.'
    return ''.join(regex)

regex = 'a*aUba'
regex = addPoints(regex)
print(regex)
regex = shunting_yard(regex)
stack = []
d = graphviz.Digraph(format='png')


    





