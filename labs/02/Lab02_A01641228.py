"""
Fernando Gomez Martinez A01641228
Lab 02
Alphabet = 'a' 'b' 
"""

import graphviz

totalStates = int(0)
tokens = {}
alphabet = {}
regex = ""
stack = []

graph = graphviz.Digraph(comment= 'Lab 02 Fernando Gomez Martinez')
graph

class State:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def addState(char):
    global totalStates
    graph.edge('q'+str(totalStates), 'q'+str(int(totalStates+1)), label=char)
    state = State(totalStates, [totalStates+1])
    totalStates += 2

    return state

def union(x, y):
    global totalStates
    graph.edge('q'+str(totalStates), 'q'+str(int(x.start)), label="e")
    graph.edge('q'+str(totalStates), 'q'+str(int(y.end)), label="e")

    state = State(totalStates, [x.end[0], y.end[0]])
    totalStates += 1

    return state

def concat(x, y):
    global totalStates
    for i in range(0, len(x.end)):
        graph.edge('q'+str(int(x.end[i])), 'q'+str(int(y.start)), label="e")
    state = State(x.start, y.end)

    return state             

def starOpoerator(myState):
    global totalStates
    graph.edge('q'+str(int(totalStates)), 'q'+str(int(myState.start)), label="e")

    
    for i in range (0, len(myState.end)):
        graph.edge('q'+str(int(myState.end[i])), 'q'+str(int(myState.start)), label="e")
    

    myState = State(0, myState.end)
    totalStates += 1
    return myState

def operatingHierarchy(regex, alphabet):
    outQueue = []
    operatingStack =[]

    hierarchy = {'*':3, '.':2, 'U':1}
    tokens = list(regex)

    for element in tokens:
        if element == '(':
            operatingStack.append(element)
        elif element == ')':
            while operatingStack[-1] != '(':
                outQueue.append(operatingStack.pop())
            operatingStack.pop()
        elif element in alphabet:
            outQueue.append(element)
        elif element in {'*', '.', 'U'}:
            while operatingStack and operatingStack[-1] != '(' and hierarchy[operatingStack[-1]] >= hierarchy[element]:
                outQueue.append(operatingStack.pop())
            operatingStack.append(element)

    while operatingStack:
        outQueue.append(operatingStack.pop())

    return ''.join(outQueue)

def rewriteRegex(regex: str):
    regex = list(regex)
    global alphabet
    alphabet = {'a', 'b', 'A', 'e'}

    for element in range (len(regex)-1):
        if regex[element] in alphabet and (regex[element+1] in alphabet or regex[element+1] == '('):
            regex[element] = regex[element]+'.'
        elif regex[element] == "*" and (regex[element+1] in alphabet or regex[element+1] == '('):
            regex[element] = regex[element]+'.'
        elif regex[element] == ')' and regex[element+1] in alphabet:
            regex[element] = regex[element]+'.'
        
    return ''.join(regex)

def translate(regex: str, alphabet: list):
    global stack

    for element in regex:
        if element in alphabet:
            currentState = addState(char=element)
            stack.append(currentState)

        elif element == '.':
            currentState = concat(x=stack[len(stack)-1], y=stack[len(stack)-2])
            stack.pop()
            stack.pop()
            stack.append(currentState)

        elif element == 'U':
            currentState = union(x=stack[len(stack)-1], y=stack[len(stack)-2])
            stack.pop()
            stack.pop()
            stack.append(currentState)

        elif element == '*':
            currentState = starOpoerator(myState= stack[len(stack)-1])
            stack.pop()
            stack.append(currentState)
    return

def main():
    regex = input("REGEX: ")
    regex = rewriteRegex(regex)
    regex = operatingHierarchy(regex=regex, alphabet=alphabet)

    translate(regex=regex, alphabet=alphabet)
    print(graph.source)
    graph.render("Lab02.pdf", view=True)
    graph.view

main()