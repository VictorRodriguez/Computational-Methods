# Ingrid González A01641116

# code not working properly
import graphviz

class NFA:
    def __init__(self):
        self.states = set()
        self.transitions = {}
        self.alphabet = set()
        self.start_state = None
        self.accept_states = set()

    def state(self, state):
        self.states.add(state)

    def transition(self, src_state, symbol, dst_states):
        if (src_state, symbol) not in self.transitions:
            self.transitions[(src_state, symbol)] = set()
        self.transitions[(src_state, symbol)].update(dst_states)

    def epsilon_transition(self, src_state, dst_state):
        self.transition(src_state, 'e', {dst_state})

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

def regexNFA(regex):
    nfa = NFA()
    start_state = 0
    nfa.state(start_state)
    nfa.set_start_state(start_state)

    current_state = start_state
    for c in regex:
        if c == 'a' or c == 'b':
            nfa.alphabet.add(c)
            next_state = current_state + 1
            nfa.state(next_state)
            nfa.transition(current_state, c, {next_state})
            current_state = next_state
        elif c == 'U':
            nfa.alphabet.add('e')
            left_nfa = nfa
            nfa = NFA()
            start_state = current_state + 1
            nfa.state(start_state)
            nfa.set_start_state(start_state)
            nfa.epsilon_transition(start_state, left_nfa.start_state)
            nfa.states.update(left_nfa.states)
            nfa.transitions.update(left_nfa.transitions)
            nfa.accept_states.update(left_nfa.accept_states)
            current_state = start_state
        elif c == '*':
            nfa.alphabet.add('e')
            prev_state = current_state
            next_state = current_state + 1
            nfa.state(next_state)
            nfa.epsilon_transition(prev_state, next_state)
            nfa.epsilon_transition(next_state, prev_state)
            nfa.set_start_state(prev_state)
            nfa.add_accept_state(prev_state)
            nfa.add_accept_state(next_state)
            current_state = next_state

    return nfa

def plot(nfa):
    g = graphviz.Digraph('G', filename='nfa.log')
    g.attr('node', shape='circle')
    for state in nfa.states:
        g.node(str(state), shape='doublecircle' if state in nfa.accept_states else 'circle')
    g.node('start', shape='point')
    g.edge('start', str(nfa.start_state))
    for (src_state, symbol), dst_states in nfa.transitions.items():
        for dst_state in dst_states:
            g.edge(str(src_state), str(dst_state), label=symbol)
    return g

nfa = regexNFA('(ab)*')
g = plot(nfa)
g.view()

def main():
    plot(nfa)

if __name__ == "__main__":
    main()
