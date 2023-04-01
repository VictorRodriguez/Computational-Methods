# Equivalence of Finite Automata
# Author: Diego Partida Romero
# ID: A01641113
# Lab 02

print("- - - - - - - - - - - - - - - - - - - - - - ")
print("Author: Diego Partida Romero\nID: A01641113\n")

import graphviz

def plot(val):
    g = graphviz.Digraph('G', filename='set.gv')
    start = 0
    final = set()
    for pair in val:
        if pair[0] not in final:
            g.node(str(pair[0]), shape='circle')
        if pair[1] not in final:
            g.node(str(pair[1]), shape='doublecircle')
        if pair[0] == start:
            g.node("start", shape='point')
            g.edge("start", str(pair[0]))
        if pair[1] in final:
            final.add(pair[1])
        g.edge(str(pair[0]), str(pair[1]), label="a" if pair[2] == 0 else "b")
    g.view()




def main():
    # Regex examples:
    # (ab)*b
    # (ab)*
    # (ab U a)*
    # (ab)* U (ab)*

    # Define the regular expression
    regex = "(ab)* U (ab)*"
    print("Regular expression: " + regex)

    alphabet = ["a", "b"]
    empty = "e"
    transitions = []
    start_state = 0
    current_state = start_state

    # Loop over each character in the regular expression
    for char in regex:
        # If the character is an "a"
        if char == "a":
            new_state = current_state + 1

            # Add the transition to the list
            transitions.append((current_state, new_state, 0))
            current_state = new_state

        # If the character is a "b"
        elif char == "b":
            new_state = current_state + 1
            transitions.append((current_state, new_state, 1))
            current_state = new_state

        # If the character is a union symbol
        elif char == "U" or char == "|":
            # Create two new states
            new_state1 = current_state + 1
            new_state2 = current_state + 2

            # Add the transitions to the list
            transitions.append((current_state, new_state1, 2))
            transitions.append((current_state, new_state2, 2))
            transitions.append((new_state1, new_state2, 2))
            transitions.append((new_state2, new_state1, 2))

            current_state = new_state1

        # If the character is a star symbol
        elif char == "*":
            new_state1 = current_state + 1
            new_state2 = current_state + 2
            transitions.append((current_state, new_state1, 2))
            transitions.append((current_state, new_state2, 2))
            transitions.append((new_state1, current_state, 2))
            transitions.append((new_state1, new_state2, 2))
            current_state = new_state1

    # Add the final state to the list of final states
    final_state = current_state
    final_states = set([final_state])
    # Create a list of states
    states = list(range(start_state, final_state + 1))

    # Transitions for each state and symbol in the alphabet
    transition_table = {}
    for state in states:
        transition_table[state] = {}
        for symbol in alphabet:
            next_state = empty
            for transition in transitions:
                if transition[0] == state and (transition[2] == 2 or symbol == 'a' and transition[2] == 0 or symbol == 'b' and transition[2] == 1):
                    next_state = transition[1]
                    break
            transition_table[state][symbol] = next_state

    # Transition table
    for state in states:
        for symbol in alphabet:
            print(f"({state}, {symbol}) -> {transition_table[state][symbol]}")

    plot(transitions)

if __name__ == "__main__":
    main()



    
