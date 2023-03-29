"""
Author: Armando Terrazas Gómez
ID: A01640924
Date: 27/03/2023

Converts a Regex to a NFA and then plots it

Alphabet: {a, b}, Alphabet symbol: {A}, Empty string: {E}
Operators: {*, U}
Accepts parenthesis
"""

import graphviz

class State:    
    def __init__(self, isAccepted = False) -> None:
        global globalCounter
        self.label = globalCounter
        globalCounter += 1
        self.isAccepted = isAccepted
    
class Transition:
    def __init__(self, transition: str, state) -> None:
        self.transition = transition
        self.state = state
    
class NFA:
    def __init__(self) -> None:
        startState = State()
        self.startState = startState
        self.endStates = [startState]
        self.transitions = {
            startState.label: []
        }

    def addBasicTransition(self, transition: str):
        newState = State(True)
        for i in self.endStates:
            self.transitions[i.label].append(Transition(transition, newState))
            i.isAccepted = False # The end state is no longer an end state
        self.endStates = [newState]
        self.transitions[newState.label] = []
    
    def concat(self, nfa):
        for i in self.endStates:
            i.isAccepted = False
            self.transitions[i.label].append(Transition('E', nfa.startState))
        self.endStates = nfa.endStates
        self.transitions.update(nfa.transitions)

    def union(self, nfa):
        newState = State()
        self.transitions[newState.label] = [Transition('E', self.startState), Transition('E', nfa.startState)]
        # The end states should be merged
        self.endStates.extend(nfa.endStates)
        self.transitions.update(nfa.transitions)
        self.startState = newState

    def starOperation(self):
        for i in self.endStates:
            self.transitions[i.label].append(Transition('E', self.startState))
        newState = State(True)
        self.transitions[self.startState.label].append(Transition('E', newState))
        self.endStates.append(newState)
        self.transitions[newState.label] = []

    def oneFinalState(self):
        for i in self.endStates:
            i.isAccepted = False
        newState = State(True)
        for i in self.endStates:
            self.transitions[i.label].append(Transition('E', newState))
        self.endStates = [newState]
        self.transitions[newState.label] = []

    def cleanStartState(self): # The Start state should recieve any transitions from any other state
        newStartState = State()
        self.transitions[newStartState.label] = [Transition('E', self.startState)]
        self.startState = newStartState

    def draw(self):
        d = graphviz.Digraph(format='png')
        #add the double circle for the end states
        for i in self.endStates:
            if i.isAccepted:
                d.node(str(i.label), shape='doublecircle')

        # Color the start state
        d.node(str(self.startState.label), color='blue')
        
        for i in self.transitions:
            for j in self.transitions[i]:
                d.edge(str(i), str(j.state.label), label=j.transition)
        d.render('test-output/round-table.gv', view=True)

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
                if not operator_stack:
                    raise ValueError('Mismatched parentheses')
            operator_stack.pop()  # Pop the left parenthesis off the stack
        elif token in {'U', '*', '.'}:
            # If the token is an operator, pop operators off the stack until an operator with lower precedence is found
            while operator_stack and operator_stack[-1] != '(' and precedence[operator_stack[-1]] >= precedence[token]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)

    # Pop any remaining operators off the stack and add them to the output queue
    while operator_stack:
        popped = operator_stack.pop()
        if popped == '(':
            raise ValueError('Mismatched parentheses')
        output_queue.append(popped)

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

def postFixToNFA(postfix: str):
    global globalCounter
    nfaStack = []
    globalCounter = 0

    if len(postfix) == 0:
        return NFA()
    
    for i in postfix:
        if i in {'a', 'b', 'A', 'E'}:
            nfa = NFA()
            nfa.addBasicTransition(i)
            nfaStack.append(nfa)
        elif i == '.':
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            nfa1.concat(nfa2)
            nfaStack.append(nfa1)
        elif i == 'U':
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            nfa1.union(nfa2)
            nfaStack.append(nfa1)
        elif i == '*':
            nfa = nfaStack.pop()
            nfa.starOperation()
            nfaStack.append(nfa)
    finalNFA = nfaStack.pop()
    finalNFA.oneFinalState() # Make sure there is only one final state
    finalNFA.cleanStartState() # Make sure the start state doesn't recieve any transitions
    return finalNFA

def main():
    regex = input("Enter the regex: ")
    regex = regex.replace(' ', '')
    regex = addPoints(regex)
    try:
        regex = shunting_yard(regex)
    except ValueError as e:
        print(e)
        return
    print(regex)
    nfa = postFixToNFA(regex)
    nfa.draw()

if __name__ == "__main__":
    main()




    





