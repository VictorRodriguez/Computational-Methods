import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

#Alan Antonio Ruelas Robles A01641426

# Union symbol is U, not +

alphabet = ['a', 'b']
epsilon = 'E'
start_state = "start"
end_state = "end"
states = set()
final_states = []
current_state = 0
union_state = 0
star_state = 0


def is_valid(regex):
    stack = []
    parenthesis = {')' : '('}
    for character in regex:
        if character == '(':
            stack.append(character)
        if character == ')' and not stack:
            return False
        if character == ')' and parenthesis[character] != stack.pop():
            return False
    if stack:
        return False
    return True


def add_state(symbol):
    global current_state
    new_state = current_state + 1
    states.add((current_state, new_state, symbol))
    current_state = new_state


def add_state_in_open_parenthesis():
    global union_state, star_state
    union_state = star_state = current_state
    add_state(epsilon)


def add_state_in_letter(character):
    global star_state, current_state
    star_state = current_state
    add_state(character)

def add_states_in_union():
    global final_states, current_state, states
    final_states.append(current_state)
    new_state = current_state + 1
    current_state = union_state
    states.add((current_state, new_state, epsilon))
    current_state = new_state


def add_states_in_star():
    global states
    states.add((current_state, star_state, epsilon))
    states.add((star_state, current_state, epsilon))


def add_state_in_plus():
    global states
    states.add((current_state, star_state, epsilon))


def add_states_in_close_parenthesis():
    global final_states, current_state, states, star_state
    final_states.append(current_state)
    new_state = current_state + 1
    for state in final_states[::-1]:
        states.add((state, new_state, epsilon))
        final_states.pop()
    current_state = new_state
    star_state = union_state


def connect_aceptance_states():
    global final_states, current_state, states
    final_states.append(current_state)
    for state in final_states[::-1]:
        states.add((state, end_state, epsilon))


def make_nfa(regex):
    for character in regex:
        if character == '(':
            add_state_in_open_parenthesis()
        if character in alphabet:
            add_state_in_letter(character)
        if character == 'U':
            add_states_in_union()
        if character == '*':
            add_states_in_star()
        if character == '+':
            add_state_in_plus()
        if character == ')':
            add_states_in_close_parenthesis()
    connect_aceptance_states()
    return states

def analyze(regex):
    global states
    states.add((start_state, current_state, epsilon))
    if is_valid(regex):
        nfa = make_nfa(regex)
        print(nfa)
        return nfa
    print("The regex is not valid")
    return states


def plot(set):
    g = graphviz.Digraph('G', filename='nfa.gv')
    g.attr('node', shape='doublecircle')
    g.node(end_state)
    g.attr('node', shape='circle')
    g.attr(rankdir='LR')
    for pair in set:
        g.edge(f"{pair[0]}", f"{pair[1]}", label=f"{pair[2]}")
    g.view()

def main():
    #regex = input("Eneter the regular expression: ")
    regex = "(ab U b)*"
    dfa = analyze(regex)
    plot(dfa)

if __name__ == "__main__":
    main()