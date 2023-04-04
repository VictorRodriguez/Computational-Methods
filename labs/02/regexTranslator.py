# Lab 2: Regular Expressions and Nondeterministic Finite Automata
# Author: Israel Vidal Paredes

import graphviz

# define the alphabet
alphabet = ['a', 'b']

# define the regular expression
regex = '(a.b+a)*'

# define a stack for building the NFA
stack = []

# define a counter for generating unique state names
state_counter = 0

# function to generate a new state name
def new_state():
    global state_counter
    state_counter += 1
    return f'q{state_counter}'

# function to create a new NFA with one transition
def create_nfa(symbol):
    start_state = new_state()
    end_state = new_state()
    nfa = {
        'start': start_state,
        'end': end_state,
        'transitions': [(start_state, symbol, end_state)]
    }
    return nfa

# function to concatenate two NFAs
def concatenate_nfas(nfa1, nfa2):
    new_nfa = {
        'start': nfa1['start'],
        'end': nfa2['end'],
        'transitions': nfa1['transitions'] + nfa2['transitions']
    }
    return new_nfa

# function to union two NFAs
def union_nfas(nfa1, nfa2):
    start_state = new_state()
    end_state = new_state()
    transitions = [(start_state, 'E', nfa1['start']), (start_state, 'E', nfa2['start']), 
                   (nfa1['end'], 'E', end_state), (nfa2['end'], 'E', end_state)]
    new_nfa = {
        'start': start_state,
        'end': end_state,
        'transitions': transitions + nfa1['transitions'] + nfa2['transitions']
    }
    return new_nfa

# function to apply the Kleene star to an NFA
def kleene_star_nfa(nfa):
    start_state = new_state()
    end_state = new_state()
    transitions = [(start_state, 'E', nfa['start']), (start_state, 'E', end_state), 
                   (nfa['end'], 'E', nfa['start']), (nfa['end'], 'E', end_state)]
    new_nfa = {
        'start': start_state,
        'end': end_state,
        'transitions': transitions + nfa['transitions']
    }
    return new_nfa

# iterate over the regular expression and build the NFA
for symbol in regex:
    if symbol in alphabet:
        stack.append(create_nfa(symbol))
    elif symbol == '.':
        nfa2 = stack.pop()
        nfa1 = stack.pop()
        stack.append(concatenate_nfas(nfa1, nfa2))
    elif symbol == '+':
        nfa2 = stack.pop()
        nfa1 = stack.pop()
        stack.append(union_nfas(nfa1, nfa2))
    elif symbol == '*':
        nfa = stack.pop()
        stack.append(kleene_star_nfa(nfa))

# the final NFA is the top element of the stack
nfa = stack.pop()

# create a graphviz graph for the NFA
dot = graphviz.Digraph('G', filename='nfa.gv')

# add the states
dot.node(nfa['start'], shape='circle')
dot.node(nfa['end'], shape='doublecircle')
for transition in nfa['transitions']:
    dot.node(transition[0], shape='circle')
    dot.node(transition[2], shape='circle')

# add the transitions
for transition in nfa['transitions']:
    dot.edge(transition[0], transition[2], label=transition[1])

# render the graph
dot.render('nfa', view=True)