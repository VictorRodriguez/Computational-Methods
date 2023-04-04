import graphviz
class NFATransition:
    def __init__(self, input_symbol, next_state):
        self.input_symbol = input_symbol
        self.next_state = next_state
        
    def __repr__(self):
        return f"{self.input_symbol} -> {self.next_state}"
class NFA:
    def __init__(self, states, start_state, accept_states, transitions):
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def single_char(char):
        states = {0, 1}
        start_state = 0
        accept_states = {1}
        transitions = {(0, char, 1)}
        return NFA(states, start_state, accept_states, transitions)
        
    def concatenation(self, other_nfa):
        for state in self.accept_states:
            state.add_transition(NFATransition("", other_nfa.start_state))
        self.accept_states = other_nfa.accept_states
        self.transition_function.update(other_nfa.transition_function)
        self.states |= other_nfa.states
        self.alphabet |= other_nfa.alphabet
        
    def union(self, other_nfa):
        new_start_state = State()
        new_start_state.add_transition("", self.start_state)
        new_start_state.add_transition("", other_nfa.start_state)

        new_accept_state = State()
        for state in (self.accept_states | other_nfa.accept_states):
            state.add_transition("", new_accept_state)

        self.states |= other_nfa.states | {new_start_state, new_accept_state}
        self.alphabet |= other_nfa.alphabet

        self.start_state = new_start_state
        self.accept_states = {new_accept_state}


    def kleene_star(self):
        new_start_state = State()
        self.states.add(new_start_state)
        self.start_state.epsilon_transitions.add(self.start_state)

        for accept_state in self.accept_states:
            accept_state.epsilon_transitions.add(self.start_state)
            accept_state.epsilon_transitions.add(new_start_state)

        self.accept_states = {new_start_state}
        self.start_state = new_start_state

        return self
        
class State:
    def __init__(self):
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        if input_symbol not in self.transitions:
            self.transitions[input_symbol] = set()
        self.transitions[input_symbol].add(next_state)

    def epsilon_closure(self):
        closure = set([self])
        stack = [self]
        while stack:
            state = stack.pop()
            for next_state in state.transitions.get("", []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def __repr__(self):
        return f"State({id(self)})"

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return id(self) == id(other)
class ThompsonNFA:
    def __init__(self, start_state, final_state):
        self.start_state = start_state
        self.final_state = final_state


def add_concatenation(regex: str) -> str:
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

def thompson_construction(postfix: str) -> ThompsonNFA:

    # Stack to keep track of NFAs
    nfa_stack = []

    # Loop through postfix regex
    for char in postfix:
        if char == '+':
            # Pop top two NFAs off the stack and union them
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            new_nfa = NFA.union(nfa1, nfa2)
            nfa_stack.append(new_nfa)

        elif char == '.':
            # Pop top two NFAs off the stack and concatenate them
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            new_nfa = NFA.concatenate(nfa1, nfa2)
            nfa_stack.append(new_nfa)

        elif char == '*':
            # Pop top NFA off the stack and apply Kleene star
            nfa = nfa_stack.pop()
            new_nfa = NFA.kleene_star(nfa)
            nfa_stack.append(new_nfa)
        else:
            # Create new NFA with a single transition for the character
            new_nfa = NFA.single_char(char)
            nfa_stack.append(new_nfa)

    # There should only be one NFA left on the stack, which is the final result
    if len(nfa_stack) != 1:
        raise ValueError("Invalid regex")
    return nfa_stack.pop()

# main function
def main():
    #regex = add_concatenation(input("Enter a regex in infix notation using only 'a', 'b', '(', ')', '+', '.', and '*': "))
    regex = "(a+b)*a"
    print(regex)
    postfix_regex = infix_to_postfix(regex)
    print(postfix_regex)
    nfa = thompson_construction(postfix_regex)
    
if __name__ == '__main__':
    main()