"""
Juan Daniel Muñoz Dueñas A01641792 03/04/2023

This program converts a regex to a NFA and then plots it

Alphabet: {a, b}, Alphabet symbol: {A}, Empty string: {E}

Operators: {*, U}

"""

import graphviz

CONT = 0

class NFA:
    def __init__(self, symbol):
        global CONT
        self.states = {CONT, CONT + 1}
        self.transitions = {(CONT, symbol, CONT + 1)}
        self.start_state = CONT
        self.final_states = {CONT + 1}
        CONT += 2

    def concatenation(self, nfa):
        self.states = self.states | nfa.states
        self.transitions = self.transitions | nfa.transitions
        for state in self.final_states:
            self.transitions.add((state, 'E', nfa.start_state))
        self.final_states = nfa.final_states
        return self
    
    
    def union(self, nfa):
        self.states = self.states | nfa.states
        self.transitions = self.transitions | nfa.transitions
        global CONT
        self.states.add(CONT)
        self.transitions.add((CONT, 'E', self.start_state))
        self.transitions.add((CONT, 'E', nfa.start_state))   
        self.start_state = CONT
        self.final_states = self.final_states | nfa.final_states
        CONT += 1
        return self
    
    def star(self):
        global CONT
        self.states.add(CONT)
        self.final_states.add(CONT)
        for state in self.final_states:
            self.transitions.add((state, 'E', self.start_state))
        self.start_state = CONT
        CONT += 1
        return self
    
    def plot_nfa(nfa):
        g = graphviz.Digraph(filename= "nfa.log")
        
        for state in nfa.states:
            g.node(str(state), shape="circle", label=str(state))
        for state in nfa.final_states:
            g.node(str(state), shape="doublecircle", label=str(state))
        g.node("", shape="none")
        g.edge("", str(nfa.start_state))
        for transition in nfa.transitions:
            g.edge(str(transition[0]), str(transition[2]), label=transition[1])
        g.view()
        g.render(engine='dot', format='png')

def shunt(regex):
    output = []
    stack = []
    priority = {'*':3, '.': 2, 'U': 1}
    for token in regex:
        if token in {'a', 'b', 'A', 'E'}:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
                if not stack:
                    raise Exception("Mismatched parentheses")
            stack.pop()
        elif token in priority:
            while stack and stack[-1] != '(' and priority[token] <= priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)
    while stack:
        popped = stack.pop()
        if popped == '(':
            raise Exception("Mismatched parentheses")
        output.append(popped)
        
    return output

def points(regex):
    regex = list(regex)
    alphabet = ['a', 'b', 'A', 'E']
    for i in range(len(regex)-1):
        if regex[i] in alphabet and (regex[i+1] in alphabet or regex[i] == '('):
            regex[i] = regex[i] + '.'
        elif regex[i] == '*' and  (regex[i+1] in alphabet or regex[i+1] == '('):
            regex[i] = regex[i] + '.'
        elif regex[i] == ')' and regex[i+1] in alphabet:
            regex[i] = regex[i] + '.'
    return ''.join(regex)

def normalize(regex):
    regex = regex.replace(' ', '')
    regex = regex.replace('A', "(" + "U".join(['a', 'b']) + ")")
    regex = points(regex)
    return regex

def regex_postfix(regex_postfix):
    stack = []
    for token in regex_postfix:
        if token in ['a', 'b', 'A', 'E']:
            stack.append(NFA(token))
        elif token == '*':
            stack[-1] = stack[-1].star()
        elif token == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.concatenation(nfa2)
            stack.append(nfa1)
        elif token == 'U':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.union(nfa2)
            stack.append(nfa1)
    return stack[0]

def main():
    print("Alphabet: {a, b}, Alphabet symbol: {A}, Empty string: {E}")
    print("Operators: {*, U}")
    regex = input("Enter a regex: ")
    normalized = normalize(regex)
    postfix = shunt(normalized)
    nfa = regex_postfix(postfix)
    nfa.plot_nfa()

if __name__ == "__main__":
    main()
