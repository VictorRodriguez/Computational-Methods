import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html

countStates = int(0)
tokens = {}
alphabet = ""
regex = ""
stack = []

g = graphviz.Digraph('G', filename='lab2.gv')


class State:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def addBegining():
    for i in range(0, len(g.body)):
        for j in range(0, len(g.body[i])):
            if (g.body[i][j].isdigit()):
                g.body[i] = g.body[i][:j] + \
                    str(int(g.body[i][j]) + 1) + g.body[i][j + 1:]


def checkState(char):
    global countStates
    g.edge(str(countStates), str(int(countStates+1)), label=char)
    state = State(countStates, [countStates+1])
    countStates += 2

    return state


def concatenation(a, b):
    global countStates
    for i in range(0, len(a.end)):
        g.edge(str(int(a.end[i])), str(int(b.start)), label="E")
    state = State(a.start, b.end)

    return state


def union(a, b):
    global countStates
    g.edge(str(countStates), str(int(a.start)), label="E")
    g.edge(str(countStates), str(int(b.start)), label="E")

    state = State(countStates, [a.end[0], b.end[0]])
    countStates += 1

    return state


def star(state):
    global countStates

    g.edge(str(int(countStates)), str(int(state.start)), label="E")

    for i in range(0, len(state.end)):

        g.edge(str(int(state.end[i])),
               str(int(state.start)), label="E")

    state = State(0, state.end)
    countStates += 1

    return state


def orderOperations(regex, alphabet):
    output_queue = []
    operator_stack = []

    # Define the precedence of the operators
    precedence = {'*': 3, '.': 2, 'U': 1}

    # Convert the regex string to a list of tokens
    tokens = list(regex)

    for token in tokens:
        if token in alphabet:
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
        if regex[i] in alphabet and (regex[i+1] in alphabet or regex[i+1] == '('):
            regex[i] = regex[i] + '.'
        elif regex[i] == '*' and (regex[i+1] in alphabet or regex[i+1] == '('):
            regex[i] = regex[i] + '.'
        elif regex[i] == ')' and regex[i+1] in alphabet:
            regex[i] = regex[i] + '.'
    return ''.join(regex)


def createDiagram(regex: str, alphabet: list):
    global stack

    for i in regex:
        if i in alphabet:
            currentState = checkState(char=i)
            stack.append(currentState)
        elif i == '.':
            currentState = concatenation(
                a=stack[len(stack)-1], b=stack[len(stack)-2])
            stack.pop()
            stack.pop()
            stack.append(currentState)
        elif i == 'U':
            currentState = union(
                a=stack[len(stack)-1], b=stack[len(stack)-2])
            stack.pop()
            stack.pop()
            stack.append(currentState)
        elif i == '*':
            currentState = star(state=stack[len(stack)-1])
            stack.pop()
            stack.append(currentState)

    return


def alpha2Array(alphabet):
    tempArray = list(alphabet)
    tempArray.remove("{")
    tempArray.remove(",")
    tempArray.remove("}")

    return tempArray


alphabet = input("Insert Alphabet: ")
alphabet = alpha2Array(alphabet)

regex = input("Insert Regex: ")
regex = addPoints(regex)
regex = orderOperations(regex=regex, alphabet=alphabet)
print(regex)

createDiagram(regex=regex, alphabet=alphabet)
f = open("la2b.txt", "w+")
f.write(g.source)
f.close()

g.view()
