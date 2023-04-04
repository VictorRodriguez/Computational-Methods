'''
LAB 02
Author: Mariana Bustos Hernández - A01641324
Date: april 2023
Description: This program converts a regular expression to an NFA, 
            plots the resulting automata.
'''

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def add_point_operator(regex):
   #add points to make the concatenation explicit
   new_regex = ""
   alphabet = {'a','b', 0,1, 'A', 'E'}

   for i in range(len(regex)-1):
      if regex[i] in alphabet and (regex[i+1] in alphabet or regex[i+1]  == '('):
         new_regex += regex[i] + "."
      elif regex[i] == '*' and (regex[i+1] in alphabet or regex[i+1]  == '(') :
         new_regex += regex[i] + "."
      elif regex[i] == ')' and regex[i+1] in alphabet:
         new_regex += regex[i] + "."
      else:
         new_regex += regex[i] #add current character without modification

   if regex[-1] in alphabet or regex[-1] == ')' or regex[-1] == '*':#last character
       new_regex += regex[-1] 
   return new_regex
      
def parse_regex(regex):
   #define the operator precedence
   precedence = {'*':3,'.':2,'U':1}

   #operator stack and output list
   operator_stack = []
   output = []

   for token in regex:
      if token in 'ab01AE':
         output.append(token)
      elif token == '(':
         operator_stack.append(token)
      elif token == ')':
         while operator_stack[-1] != '(':
            output.append(operator_stack.pop())
         operator_stack.pop()
      elif token in {'*','.','U'}:
         while operator_stack and operator_stack[-1] !='(' and precedence[token]<= precedence[operator_stack[-1]]:
            output.append(operator_stack.pop())
         operator_stack.append(token)
    
   while operator_stack:
      output.append(operator_stack.pop())

   return ''.join(output)

def evaluate_regex(regex):
    print("hello world")
    class NFA:
        def __init__(self, start, end):
            self.start = start
            self.end = end

    def build_fragment(token, state_counter):
      if token == 'U':
         second_fragment = stack.pop()
         first_fragment = stack.pop()
         start = State(state_counter)
         end = State(state_counter + 1)
         state_counter += 2
         start.add_transition(first_fragment.start)
         start.add_transition(second_fragment.start)
         first_fragment.end.add_transition(end)
         second_fragment.end.add_transition(end)
         return Fragment(start, end), state_counter
      elif token == '.':
         second_fragment = stack.pop()
         first_fragment = stack.pop()
         first_fragment.end.add_transition(second_fragment.start)
         return Fragment(first_fragment.start, second_fragment.end), state_counter
      elif token == '*':
         fragment = stack.pop()
         start = State(state_counter)
         end = State(state_counter + 1)
         state_counter += 2
         start.add_transition(fragment.start)
         start.add_transition(end)
         fragment.end.add_transition(fragment.start)
         fragment.end.add_transition(end)
         return Fragment(start, end), state_counter
      else:
         state1 = State(state_counter)
         state2 = State(state_counter + 1)
         state_counter += 2
         state1.add_transition(state2, token)
         return Fragment(state1, state2), state_counter


    class Fragment:
        def __init__(self, start, end):
            self.start = start
            self.end = end

    class State:
        def __init__(self, state_id):
            self.state_id = state_id
            self.transitions = {}

        def add_transition(self, state, symbol=None):
            if symbol in self.transitions:
                self.transitions[symbol].add(state)
            else:
                self.transitions[symbol] = {state}
    
    stack = []
    state_counter = 0
    for token in regex:
        fragment, state_counter = build_fragment(token, state_counter)
        stack.append(fragment)
    nfa_fragment = stack.pop()
    return NFA(nfa_fragment.start, nfa_fragment.end)
       
def view_nfa(nfa):
    g = graphviz.Digraph('NFA')
    states = set()
    queue = [nfa.start]
    while queue:
        state = queue.pop()
        if state not in states:
            states.add(state)
            if state == nfa.start:
                g.node(str(state.state_id), shape='circle', style='bold', label='start')
            elif state == nfa.end:
                g.node(str(state.state_id), shape='doublecircle', style='bold', label='end')
            else:
                g.node(str(state.state_id), shape='circle', label=str(state.state_id))
            for symbol, destinations in state.transitions.items():
                for destination in destinations:
                    queue.append(destination)
                    if symbol is None:
                        g.edge(str(state.state_id), str(destination.state_id), label='E')
                    else:
                        g.edge(str(state.state_id), str(destination.state_id), label=symbol)
    return g

         
#Alphabet: {a, b} or {0,1}
#Alphabet symbol: A
#Empty symbol: E
#operators: *, ., u
#regex examples: (ab)*b, (ab U a)*, a*b*, aba U bab, a(ba)* b, (E  a)b, a* U b*

def main():
   # regex = input("Enter a regular expression: ")
   regex =  "ab U b*"#"aba U bab"#"(ab u a)*" #"a(ba)*b" 
   regex = regex.replace(' ', '')  # remove spaces
   regex = add_point_operator(regex)
   print(regex)
   postfix = parse_regex(regex) #shunting yard algorithm
   nfa = evaluate_regex(postfix)
   g = view_nfa(nfa)
   g.render('nfa.gv', view=True)


   print(postfix)



if __name__ == "__main__":
    main()

