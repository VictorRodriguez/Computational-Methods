class State:
    def __init__(self, label=None, edges=None):
        self.label = label
        self.edges = edges if edges else {}

class NFA:
    def __init__(self, start_state=None, accept_states=None):
        self.start_state = start_state if start_state else State()
        self.accept_states = accept_states if accept_states else []

    def concat(self, other_nfa):
        for state in self.accept_states:
            state.edges[''] = other_nfa.start_state
        self.accept_states = other_nfa.accept_states

    def union(self, other_nfa):
        new_start = State()
        new_start.edges[''] = self.start_state
        new_start.edges[''] = other_nfa.start_state

        new_accept = State()
        for state in self.accept_states + other_nfa.accept_states:
            state.edges[''] = new_accept

        self.start_state = new_start
        self.accept_states = [new_accept]

    def star(self):
        new_start = State()
        new_accept = State()

        new_start.edges[''] = self.start_state
        new_start.edges[''] = new_accept

        for state in self.accept_states:
            state.edges[''] = self.start_state
            state.edges[''] = new_accept

        self.start_state = new_start
        self.accept_states = [new_accept]

    def get_states(self):
        seen = set()
        to_visit = [self.start_state]
        while to_visit:
            state = to_visit.pop()
            if state in seen:
                continue
            seen.add(state)
            for edge in state.edges.values():
                to_visit.append(edge)
        return seen

    def get_accept_states(self):
        return set(self.accept_states)

    def match(self, string):
        current_states = {self.start_state}
        for char in string:
            next_states = set()
            for state in current_states:
                if char in state.edges:
                    next_states.add(state.edges[char])
                if '' in state.edges:
                    next_states.add(state.edges[''])
            current_states = next_states
        return bool(current_states & self.accept_states)

def regex_to_nfa(regex):
    stack = []
    for char in regex:
        if char == 'a':
            nfa = NFA(State(), [State()])
            nfa.start_state.edges[char] = nfa.accept_states[0]
            stack.append(nfa)
        elif char == 'b':
            nfa = NFA(State(), [State()])
            nfa.start_state.edges[char] = nfa.accept_states[0]
            stack.append(nfa)
        elif char == '*':
            nfa = stack.pop()
            nfa.star()
            stack.append(nfa)
        elif char == 'U':
            right_nfa = stack.pop()
            left_nfa = stack.pop()
            left_nfa.union(right_nfa)
            stack.append(left_nfa)
    return stack.pop()

if __name__ == '__main__':
    regex = '(abUa)*'
    nfa = regex_to_nfa(regex)
