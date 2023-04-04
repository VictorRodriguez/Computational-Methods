# Lab 2: Regular Expressions and Nondeterministic Finite Automata
# Author: Israel Vidal Paredes
import graphviz

class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transition_function = {}
        self.start_state = None
        self.accept_states = set()

def infix_to_postfix(regex: str) -> str:
    # TODO: Implement the Shunting Yard algorithm to convert infix to postfix

def thompson_construction(postfix_regex: str) -> NFA:
    # TODO: Implement Thompson's Construction Algorithm for NFAs

def to_dot(nfa: NFA) -> str:
    # TODO: Generate DOT language string for Graphviz

def main():
    regex = input("Enter a regex in infix notation using only 'a', 'b', '(', ')', '|', '.', and '*': ")
    postfix_regex = infix_to_postfix(regex)
    nfa = thompson_construction(postfix_regex)
    dot_graph = to_dot(nfa)
    graph = graphviz.Source(dot_graph)
    graph.view()

if __name__ == '__main__':
    main()
