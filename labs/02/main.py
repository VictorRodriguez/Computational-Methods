"""
Author: Carlos David Amezcua Canales (A01641742)
Date: April 3, 2023
Description: This program converts a regular expression to a non-deterministic 
    finite automaton.
Input example: A*010
"""

import graphviz

# Constants
ALPHABET = ['0', '1']
ALPHABET_SIMBOL = 'A'
EMPTY_SIMBOL = 'E'
KLEENE_STAR = '*'
CONCATENATION = '.'
UNION = 'U'
LOG_FILE_NAME = "NFA.log"

# Global variables
FOLIO = 0

class NFA:
    def __init__(self, symbol):
        global FOLIO
        self.states = {FOLIO, FOLIO + 1}
        self.transitions = {(FOLIO, symbol, FOLIO + 1)}
        self.start_state = FOLIO
        self.final_states = {FOLIO + 1}
        FOLIO += 2
    
    def render(self):
        graph = graphviz.Digraph(filename=LOG_FILE_NAME)
        graph.attr(rankdir="LR")
        for state in self.states:
            graph.node(str(state), shape="circle", label="<q<SUB>" + str(state) + "</SUB>>")
        for state in self.final_states:
            graph.node(str(state), shape="doublecircle", label="<q<SUB>" + str(state) + "</SUB>>")
        graph.node("", shape="none")
        graph.edge("", str(self.start_state))
        for transition in self.transitions:
            graph.edge(str(transition[0]), str(transition[2]), label=transition[1] if transition[1] != EMPTY_SIMBOL else "ε")
        graph.render(engine="dot", format="pdf", view=True)
    
    def __invert__(self):
        # Kleene star
        global FOLIO
        self.states.add(FOLIO)
        self.final_states.add(FOLIO)
        for state in self.final_states:
            self.transitions.add((state, EMPTY_SIMBOL, self.start_state))
        self.start_state = FOLIO
        FOLIO += 1
        return self

    def __and__(self, other):
        # Concatenation
        self.states = self.states | other.states
        self.transitions = self.transitions | other.transitions
        for state in self.final_states:
            self.transitions.add((state, EMPTY_SIMBOL, other.start_state))
        self.final_states = other.final_states
        return self
    
    def __or__(self, other):
        # Union
        self.states = self.states | other.states
        self.transitions = self.transitions | other.transitions
        global FOLIO
        self.states.add(FOLIO)
        self.transitions.add((FOLIO, EMPTY_SIMBOL, self.start_state))
        self.transitions.add((FOLIO, EMPTY_SIMBOL, other.start_state))
        self.start_state = FOLIO
        self.final_states = self.final_states | other.final_states
        FOLIO += 1
        return self

def add_concatenation_operator(regex):
    ans = regex[0]
    for i in range(1, len(regex)):
        if regex[i - 1] in ALPHABET + [ALPHABET_SIMBOL, EMPTY_SIMBOL, KLEENE_STAR, ')'] and regex[i] in ALPHABET + [ALPHABET_SIMBOL, EMPTY_SIMBOL, '(']:
            ans += CONCATENATION
        ans += regex[i]
    return ans

def normalize_regex(regex):
    regex = regex.replace(' ', '')
    regex = regex.replace(ALPHABET_SIMBOL, "(" + UNION.join(ALPHABET) + ")")
    regex = add_concatenation_operator(regex)
    return regex

def shunting_yard(normalized_regex):
    output_queue = []
    operator_stack = []
    precedence = {KLEENE_STAR: 3, CONCATENATION: 2, UNION: 1}
    for token in normalized_regex:
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        elif token in precedence:
            while operator_stack and operator_stack[-1] != '(' and precedence[token] <= precedence[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            output_queue.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue

def evaluate_regex_in_posfix(regex_in_postfix):
    stack = []
    for token in regex_in_postfix:
        if token in ALPHABET + [EMPTY_SIMBOL]:
            stack.append(NFA(token))
        elif token == KLEENE_STAR:
            stack[-1] = ~stack[-1]
        elif token == CONCATENATION:
            stack[-2] = stack[-2] & stack[-1]
            stack.pop()
        elif token == UNION:
            stack[-2] = stack[-2] | stack[-1]
            stack.pop()
    return stack[0]

def main():
    print(ALPHABET_SIMBOL + " = {" + ", ".join(ALPHABET) + "}")
    regex = input("Enter regex: ")
    normalized_regex = normalize_regex(regex)
    print("Normalized regex: " + normalized_regex)
    regex_in_postfix = shunting_yard(normalized_regex)
    print("Regex in postfix: " + "".join(regex_in_postfix))
    non_deterministic_finite_automaton = evaluate_regex_in_posfix(regex_in_postfix)
    non_deterministic_finite_automaton.render()

if __name__ == "__main__":
    main()
