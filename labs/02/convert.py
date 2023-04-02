import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

class State:
    def __init__(self, tag, accept=False):
        """
        Initializes a new instance of the State class.

        Args:
            tag (str): A string representing the name or label of the state.
            accept (bool): A boolean indicating whether the state is an accepting state.
        """
        self.tag = tag
        self.transitions = []
        self.accept = accept

    def add_transition(self, character, target_state):
        """
        Adds an outgoing transition from the state to the target state, triggered by the given character.

        Args:
            character (str or None): The character that triggers the transition.
                                     If None, the transition is considered an epsilon transition.
            target_state (State): The target state of the transition.
        """
        self.transitions.append((character, target_state))

class DFA:
    def __init__(self, char):
        """
        Initializes a new instance of the DFA class with a single character transition.

        Args:
            char (str): The character that triggers the transition from the start state to an accepting state.
        """
        self.start = State(0, False)
        accept = State(1, True)
        self.start.add_transition(char, accept)
        self.states = {0: self.start, 1: accept}
        self.accept_states = [1]

    def concatenate(self, target_dfa):
        """
        Concatenates the DFA with another DFA, modifying this DFA in place.
        The resulting DFA recognizes the language that is the concatenation of the languages recognized by the two input DFAs.

        Args:
            target_dfa (DFA): The DFA to concatenate with this DFA.

        Returns:
            The modified DFA object.
        """
        for s in self.accept_states:
            self.states[s].add_transition('E', target_dfa.start)
            self.states[s].accept = False
        self.accept_states.clear()

        curr_state = len(self.states)

        for s in target_dfa.states:
            self.states[curr_state + s] = target_dfa.states[s]
            self.states[curr_state + s].tag += curr_state

            if self.states[curr_state + s].accept:
                self.accept_states.append(self.states[curr_state + s].tag)

        return self
    
    def unite(self, target_dfa):
        """
        Unites the DFA with another DFA, modifying this DFA in place.
        The resulting DFA recognizes the language that is the union of the languages recognized by the two input DFAs.

        Args:
            target_dfa (DFA): The DFA to unite with this DFA.

        Returns:
            The modified DFA object.
        """
        l_start = self.start
        self.start = State(0)
        self.start.add_transition('E', l_start)

        self.accept_states.clear()
        c_states = self.states.copy()
        for s in c_states:
            self.states[s + 1] = c_states[s]
            self.states[s + 1].tag += 1

            if self.states[s + 1].accept:
                self.accept_states.append(self.states[s + 1].tag)

        self.states[0] = self.start

        self.start.add_transition('E', target_dfa.start)
        curr_state = len(self.states)
        for s in target_dfa.states:
            self.states[curr_state + s] = target_dfa.states[s]
            self.states[curr_state + s].tag += curr_state

            if self.states[curr_state + s].accept:
                self.accept_states.append(self.states[curr_state + s].tag)

        return self
    
    def star(self):
        """
        Applies the Kleene star operation to the current DFA by adding a new start state
        that is also an accept state, adding an epsilon transition from the new start state
        to the old start state, and adding epsilon transitions from each old accept state
        to the old start state.
        
        Returns:
        - self (DFA): the modified DFA object
        """
        l_start = self.start
        self.start = State(0, True)
        self.start.add_transition('E', l_start)

        self.accept_states.clear()
        c_states = self.states.copy()
        for s in c_states:
            self.states[s + 1] = c_states[s]
            self.states[s + 1].tag += 1

            if self.states[s + 1].accept:
                self.accept_states.append(self.states[s + 1].tag)
                self.states[s + 1].add_transition('E', l_start)
        
        self.states[0] = self.start

        self.accept_states.insert(0, 0)

        return self

    def print(self):
        """
        This method performs a breadth-first search traversal of the DFA and prints each state along with its transitions.

        :return: None
        """
        bfs(self.start)

def bfs(root_state):
    """
    Perform a breadth-first search traversal of the DFA starting from the root state and print each state along with its transitions.

    :param root_state: the starting state for the traversal
    :return: None
    """
    visited = set()
    queue = [root_state]
    while queue:
        state = queue.pop(0)
        if state in visited:
            continue
        visited.add(state)
        print(f'State {state.tag} {"(accept)" if state.accept else ""}:')
        for char, target_state in state.transitions:
            print(f' - on {char} go to {target_state.tag}')
            if target_state not in visited:
                queue.append(target_state)

def inreg_2_posreg(input):
    """
    This function takes an infix regular expression as input and returns its postfix representation.
    The input string must consist of characters in the set {U, *, ., (, )}.
    The function implements the shunting-yard algorithm to convert the infix expression to postfix.

    Args:
        input (str): An infix regular expression consisting of characters in the set {U, *, ., (, )}.

    Returns:
        list: A postfix representation of the input regular expression.

    Raises:
        None
    """
    operators = "U*.()"
    pe = {'U': 2, '.': 3, '*': 4, '(': 5}
    ps = {'U': 1, '.': 2, '*': 3, '(': 0}
    stack = []
    res = []
    for id, c in enumerate(input):
        if c in operators:
            
            if len(stack) < 1:
                stack.insert(0, c)
                continue
            if c == ')':
                while stack[0] != '(':
                    res.insert(0, stack.pop(0))
                stack.pop(0)
                continue
            if pe[c] > ps[stack[0]]:
                stack.insert(0, c)
                continue
            
            flag = False
            while not flag:
                if len(stack) < 1: break
                if pe[c] <= ps[stack[0]]:
                    flag = True
                res.insert(0, stack.pop(0))
            stack.insert(0, c)
            continue
        
        res.insert(0, c)

    while stack:
        res.insert(0, stack.pop(0))

    res.reverse()

    return res

def solve_postreg(input):
    """
    Takes a postfix regular expression and returns a DFA that accepts the same language.
    
    Args:
        input (str): A string representing the postfix regular expression.
        
    Returns:
        DFA: A DFA that accepts the language described by the postfix regular expression.
    """
    stack = []
    for e in input:
        if e == '*':
            a = stack.pop(0)

            stack.insert(0, a.star())
            continue
        if e == '.':
            b = stack.pop(0)
            a = stack.pop(0)

            stack.insert(0, a.concatenate(b))
            continue
        if e == 'U':
            a = stack.pop(0)
            b = stack.pop(0)

            stack.insert(0, a.unite(b))
            continue

        stack.insert(0, DFA(e))

    return stack[0]

def makeFileFormat(graph):
    """
    Writes the DFA represented by the given graph object to a file in DOT format.
    
    Parameters:
        graph (DFA): The DFA object to be written to the file.
        
    Returns:
        None
    """
    # Open the file for writing
    f = open("graph.log", "w")
    
    # Write the header information
    f.write("digraph finite_state_machine {\n\tfontname=\"Helvetica,Arial,sans-serif\"\n\tnode [fontname=\"Helvetica,Arial,sans-serif\"]\n\tedge [fontname=\"Helvetica,Arial,sans-serif\"]\n\trankdir=LR;\n\tnode [shape = doublecircle];")
    
    # Write the accepting states
    doublecircle_nodes = graph.accept_states
    for node in doublecircle_nodes:
        f.write(f" {node}")
    f.write(";\n\tnode [shape = circle];\n")

    # Write the transitions
    for e in graph.states:
        for t in graph.states[e].transitions:
            f.write(f"\t{e} -> {str(t[1].tag)} [label = \"{str(t[0])}\"];\n")

    # Write the footer and close the file
    f.write("}")
    f.close()

def plot(graph):
    """
    Visualizes the graph using Graphviz library.

    Args:
        graph: An instance of Graph class representing the graph to be visualized.

    Returns:
        None.
    """
    # Initialize a new graph
    g = graphviz.Digraph('G', filename='graph')

    # Set font for the graph
    g.attr('graph', fontname="Helvetica,Arial,sans-serif")
    g.attr('node', fontname="Helvetica,Arial,sans-serif")
    g.attr('edge', fontname="Helvetica,Arial,sans-serif")

    # Set the rank direction of the graph
    g.attr(rankdir='LR')

    # Set the shape of accept states to doublecircle and add them to the graph
    doublecircle_nodes = graph.accept_states
    for node in doublecircle_nodes:
        g.node(str(node), shape='doublecircle')
    
    # Set the shape of non-accept states to circle and add them to the graph
    for e in graph.states:
        if not graph.states[e].accept:
            g.node(str(graph.states[e].tag), shape='circle')

    # Add edges to the graph
    for e in graph.states:
        for t in graph.states[e].transitions:
            g.edge(str(e), str(t[1].tag), label=str(t[0]))

    # View the graph
    g.view()

print(inreg_2_posreg("(a.bUa)*"))
var = solve_postreg(inreg_2_posreg("(a.bUa)*"))
var.print()
plot(var)
makeFileFormat(var)