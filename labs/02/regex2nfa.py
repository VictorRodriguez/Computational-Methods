# Jorge German Wolburg Trujillo - A01640826
#Lab 02

# Shunting Yard algorithm implementation
# Creates a NFA from regex in postfix form
import graphviz

class State:    
    def __init__(self, is_accepted = False) -> None:
        global g_counter
        self.label = g_counter
        g_counter += 1
        self.is_accepted = is_accepted

class Transition:
    def __init__(self, transition: str, state) -> None:
        self.transition = transition
        self.state = state

class NFA:
    def __init__(self) -> None:
        begin_state = State()
        self.begin_state = begin_state
        self.end_state = [begin_state]
        self.transitions = {
            begin_state.label: []
        }

# Connects two NFA in series, if the current end states are connected to the next beginning states, it results in a new NFA  
    def Concatenation(self, nfa):
        for i in self.end_state:
            i.is_accepted = False
            self.transitions[i.label].append(Transition("E", nfa.begin_state))
        self.end_state = nfa.end_state
        self.transitions.update(nfa.transitions)

# Adds a new state and transition from the current end state
    def basicTrans(self, transition: str):
        new_state = State(True)
        for i in self.end_state:
            self.transitions[i.label].append(Transition(transition, new_state))
            i.is_accepted = False
        self.end_state = [new_state]
        self.transitions[new_state.label] = []

# Connects two NFAs in parallel, where a new state is added that connects to the two original beginning states with empty transitions, having a new NFA
    def Union(self, nfa):
        new_state = State()
        self.transitions[new_state.label] = [Transition("E", self.begin_state), Transition("E", nfa.begin_state)]
        self.end_state.extend(nfa.end_state)
        self.transitions.update(nfa.transitions)
        self.begin_state = new_state

# Add a new state that connects to the beginning state with empty. The current state ends, and also connects to the new state with empty. Getting a new NFA
    def starOperator(self):
        for i in self.end_state:
            self.transitions[i.label].append(Transition("E", self.begin_state))
        new_state = State(True)
        self.transitions[self.begin_state.label].append(Transition("E", new_state))
        self.end_state.append(new_state)
        self.transitions[new_state.label] = []

# Adds a new accepting state to the corrent NFA. Connects al previous accepting states with empty.
    def stateChecker(self):
        for i in self.end_state:
            i.is_accepted = False
        new_state = State(True)
        for i in self.end_state:
            self.transitions[i.label].append(Transition("E", new_state))
        self.end_state = [new_state]
        self.transitions[new_state.label] = []

# Creates a new beginning state that connects to the previous beginning stete with empty
    def stateCleaner(self): 
        newbegin_state = State()
        self.transitions[newbegin_state.label] = [Transition("E", self.begin_state)]
        self.begin_state = newbegin_state
        
# Use the graphviz package to create a png to visuzalize the current NFA
    def Artist(self):
        d = graphviz.Digraph(format="png")
        if self.end_state[0].is_accepted:
            d.node(str(self.end_state[0].label), shape="doublecircle")

        d.node(str(self.begin_state.label), color="red")

        for i in self.transitions:
            for j in self.transitions[i]:
                d.edge(str(i), str(j.state.label), label=j.transition)
        d.render("test-output/round-table.gv", view=True)

# This function adds the concatenation operator "." to the regex string 
# when two adjacent characters or expressions are separated by whitespace or are enclosed in parentheses, 
# which is required for the Shunting Yard algorithm to work correctly.
def addPoints(regex: str):
    regex = list(regex)
    alphabet = {"a", "b", "A", "E"} 
    for i in range(len(regex)-1):
        if regex[i] in alphabet and (regex[i + 1] in alphabet or regex[i + 1] == "("):
            regex[i] = regex[i] + "."
        elif regex[i] == "*" and (regex[i + 1] in alphabet or regex[i + 1] == "("):
            regex[i] = regex[i] + "."
        elif regex[i] == ")" and regex[i + 1] in alphabet:
            regex[i] = regex[i] + "."
    return "".join(regex)

# Exctracted from https://en.wikipedia.org/wiki/Shunting_yard_algorithm
def shunting_yard(regex):
    oQueue = []
    oStack = []

    precedence = {"*": 3, ".": 2, "+": 1}
    tokens = list(regex)

    for token in tokens:
        if token in {"a", "b", "A", "E"}:
            oQueue.append(token)
        elif token == "(":
            oStack.append(token)
        elif token == ")":
            while oStack[-1] != "(":
                oQueue.append(oStack.pop())
                if not oStack:
                    raise ValueError("Parenthesis error")
            oStack.pop()
        elif token in {"U", "*", "."}:
            while oStack and oStack[-1] != "(" and precedence[oStack[-1]] >= precedence[token]:
                oQueue.append(oStack.pop())
            oStack.append(token)

    while oStack:
        popped = oStack.pop()
        if popped == "(":
            raise ValueError("Parenthesis error")
        oQueue.append(popped)

    return "".join(oQueue)

# Takes a postfix regex and returns an NFA object built from that expression 
# by applying the methods of the NFA class using a stack data structure.
def postNFA(postfix: str):
    global g_counter
    nfa_stack = []
    g_counter = 0

    if len(postfix) == 0:
        return NFA()

    for i in postfix:
        if i in {"a", "b", "A", "E"}:
            nfa = NFA()
            nfa.basicTrans(i)
            nfa_stack.append(nfa)
        elif i == ".":
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            nfa1.Concatenation(nfa2)
            nfa_stack.append(nfa1)
        elif i == "+":
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            nfa1.Union(nfa2)
            nfa_stack.append(nfa1)
        elif i == "*":
            nfa = nfa_stack.pop()
            nfa.starOperator()
            nfa_stack.append(nfa)
    finalNFA = nfa_stack.pop()
    finalNFA.stateChecker() 
    finalNFA.stateCleaner()
    return finalNFA

def main():
    regex = input("Enter the regex: ")
    regex = regex.replace(" ", "")
    # Add points for shunting yard to work
    regex = addPoints(regex)
    regex = shunting_yard(regex)  

    nfa = postNFA(regex)
    nfa.Artist()

if __name__ == "__main__":
    main()