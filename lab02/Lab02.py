# Hugo Alejandro Gomez Herrera 


# References:
# https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/
# https://blog.cernera.me/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm/

import graphviz

alphabet = {'a', 'b', 'A', 'E'} 
id_counter = 0

#NFA CLASS
class State:
    def __init__(self, is_accept=False):
        global id_counter
        self.id = id_counter
        id_counter += 1
        self.is_accept = is_accept

class Transition:
    def __init__(self, symbol, state):
        self.symbol = symbol
        self.state = state

class NFA:
    def __init__(self):
        start_state = State()
        self.start_state = start_state
        self.accept_states = [start_state]
        self.transitions = {
            start_state.id: []
        }

    def add_transition(self, symbol):
        new_state = State(True)
        for state in self.accept_states:
            self.transitions[state.id].append(Transition(symbol, new_state))
            state.is_accept = False
        self.accept_states = [new_state]
        self.transitions[new_state.id] = []

    def union(self, nfa):
        new_state = State()
        self.transitions[new_state.id] = [Transition('E', self.start_state), Transition('E', nfa.start_state)]
        self.accept_states.extend(nfa.accept_states)
        self.transitions.update(nfa.transitions)
        self.start_state = new_state

    def concatenation(self, nfa):
        for state in self.accept_states:
            state.is_accept = False
            self.transitions[state.id].append(Transition('E', nfa.start_state))
        self.accept_states = nfa.accept_states
        self.transitions.update(nfa.transitions)

    def star(self):
        for state in self.accept_states:
            self.transitions[state.id].append(Transition('E', self.start_state))
        new_state = State(True)
        self.transitions[self.start_state.id].append(Transition('E', new_state))
        self.accept_states.append(new_state)
        self.transitions[new_state.id] = []

    def verify_accept_state(self):
        for state in self.accept_states:
            state.is_accept = False
        new_state = State(True)
        for state in self.accept_states:
            self.transitions[state.id].append(Transition('E', new_state))
        self.accept_states = [new_state]
        self.transitions[new_state.id] = []

    def clean_start_state(self):
        new_start_state = State()
        self.transitions[new_start_state.id] = [Transition('E', self.start_state)]
        self.start_state = new_start_state

#REGEX MANIPULATION
def insert_concatenation(regex):
    # Insert explicit concatenation operators "?"
    regex = list(regex)
    global alphabet
    for i in range(len(regex) - 1):
        if regex[i] in alphabet :
            if regex[i+1] in alphabet or regex[i+1] == '(':
                regex[i] = regex[i] + '?'
        elif regex[i] == ')':
            if regex[i+1] in alphabet or regex[i+1] == '(':
                regex[i] = regex[i] + '?'
        elif regex[i] == '*':
            if regex[i+1] in alphabet or regex[i+1] == '(':
                regex[i] = regex[i] + '?'
    return ''.join(regex)

def shunting_yard(regex):
    precedence = {'*': 3, '?': 2, 'U': 1}
    output, ops = [], []
    for token in regex:
        if token in {'a', 'b', 'A', 'E'}:
            output.append(token)
        elif token in {'*', '?', 'U'}:
            while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[token]:
                output.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()
        elif token == '?':
            while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence['U']:
                output.append(ops.pop())
            ops.append('U')
    output.extend(ops[::-1])
    return ''.join(output)

#POSTFIX TO NFA
def post_fix_to_nfa(postfix: str):
    global id_counter
    id_counter = 0
    global alphabet
    nfa_stack = []

    if not postfix:
        return NFA()

    for i in postfix:
        switcher = {
            '?': lambda: nfa_stack[-2].concatenation(nfa_stack.pop()),
            '*': lambda: nfa_stack[-1].star(),
            'U': lambda: nfa_stack[-2].union(nfa_stack.pop())
        }
        if i in alphabet:
            nfa = NFA()
            nfa.add_transition(i)
            nfa_stack.append(nfa)
        else:
            switcher.get(i, lambda: None)()

    good_nfa = nfa_stack.pop()
    good_nfa.verify_accept_state()
    good_nfa.clean_start_state()
    return good_nfa

#DRAWING THE NFA
def draw_nfa(nfa, output_file):
    d = graphviz.Digraph(format='png')
    
    if nfa.accept_states[0].is_accept:
        d.node(str(nfa.accept_states[0].id), shape='doublecircle')
    
    d.node(str(nfa.start_state.id), color='green')
    
    for i in nfa.transitions:
        for j in nfa.transitions[i]:
            d.edge(str(i), str(j.state.id), label=j.symbol)
    
    return d



#MAIN
def main():
    regex = input("Enter the regex: ")
    regex = regex.replace(' ', '')
    regex = insert_concatenation(regex)
    print(regex)
    regex = shunting_yard(regex)
    print(regex)

    nfa = NFA()
    # code to construct the nfa...
    nfa = post_fix_to_nfa(regex)

    d = draw_nfa(nfa, 'test-output/round-table.gv')
    d.render(view=True) 


if __name__ == "__main__":
    main()
