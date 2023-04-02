import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

class State:
    def __init__(self, tag, accept=False):
        self.tag = tag
        self.transitions = []
        self.accept = accept

    def add_transition(self, character, target_state):
        self.transitions.append((character, target_state))

class DFA:
    def __init__(self, char):
        self.start = State(0, False)
        accept = State(1, True)
        self.start.add_transition(char, accept)
        self.states = {0: self.start, 1: accept}
        self.accept_states = [1]

    def concatenate(self, target_dfa):
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
        bfs(self.start)

def bfs(root_state):
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
    stack = []
    for e in input:
        if e == '*':
            """
            for e in stack:
                e.print()
                print()
            """
            for e in stack:
                e.print()
                print()
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
    f = open("graph.log", "w")
    f.write("digraph finite_state_machine {\n\tfontname=\"Helvetica,Arial,sans-serif\"\n\tnode [fontname=\"Helvetica,Arial,sans-serif\"]\n\tedge [fontname=\"Helvetica,Arial,sans-serif\"]\n\trankdir=LR;\n\tnode [shape = doublecircle];")
    
    doublecircle_nodes = graph.accept_states
    for node in doublecircle_nodes:
        f.write(f" {node}")
    f.write(";\n\tnode [shape = circle];\n")

    for e in graph.states:
        for t in graph.states[e].transitions:
            f.write(f"\t{e} -> {str(t[1].tag)} [label = \"{str(t[0])}\"];\n")

    f.write("}")

def plot(graph):
    g = graphviz.Digraph('G', filename='graph')
    g.attr('graph', fontname="Helvetica,Arial,sans-serif")
    g.attr('node', fontname="Helvetica,Arial,sans-serif")
    g.attr('edge', fontname="Helvetica,Arial,sans-serif")
    g.attr(rankdir='LR')
    
    doublecircle_nodes = graph.accept_states
    for node in doublecircle_nodes:
        g.node(str(node), shape='doublecircle')
    
    for e in graph.states:
        if not graph.states[e].accept:
            g.node(str(graph.states[e].tag), shape='circle')

    for e in graph.states:
        for t in graph.states[e].transitions:
            g.edge(str(e), str(t[1].tag), label=str(t[0]))

    g.view()

print(inreg_2_posreg("(a.bUa)*"))
var = solve_postreg(inreg_2_posreg("(a.bUa)*"))
var.print()
plot(var)
makeFileFormat(var)