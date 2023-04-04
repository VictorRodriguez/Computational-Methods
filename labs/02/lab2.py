import graphviz

#Jorge Madrigal
#A01641409

class State:
    def __init__(self):
        self.transitions = {}

class Automaton:
    def __init__(self, regex):
        self.ss = State()
        self.ac = set()
        self.build_automaton(regex)

    def build_automaton(self, regex):
        cs = [self.ss]
        i = 0
        while i < len(regex):
            char = regex[i]
            if char == "0":
                ns = [State()]
                cs = [state for state in cs for _ in state.transitions.setdefault("0", ns)]
            elif char == "1":
                ns = [State()]
                cs = [state for state in cs for _ in state.transitions.setdefault("1", ns)]
            elif char == "|":
                ns = State()
                ns.transitions["E"] = [self.ss]
                ns.transitions["E"] += cs
                self.ss = ns
            elif char == "*":
                ns = State()
                ns.transitions["E"] = [self.ss]
                self.ss.transitions["E"] = [ns]
                cs = [ns]
            elif char == "U":
                ns = State()
                cs = [state for state in cs for _ in state.transitions.setdefault("E", [ns])]
                cs = [ns]
            i += 1


    def to_dot(self):
        dot = graphviz.Digraph()
        dot.node(str(id(self.ss)), shape='circle')
        dot.edge("", str(id(self.ss)))
        for state in self.ac:
            dot.node(str(id(state)), shape='doublecircle')
        for state in self.ac:
            dot.edge(str(id(state)), "")
        visited = set()
        stack = [self.ss]
        while stack:
            state = stack.pop()
            visited.add(state)
            for symbol, transitions in state.transitions.items():
                for transition_state in transitions:
                    dot.edge(str(id(state)), str(id(transition_state)), label=symbol)
                    if transition_state not in visited:
                        stack.append(transition_state)
        return dot

regex = "(ab)*"
automaton = Automaton(regex)
dot = automaton.to_dot()
dot.render("automaton.gv", view=True)
