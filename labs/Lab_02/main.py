"""
    Implementation of Computational Methods (TC2037.601)
    Professor Victor Rodriguez
    Lab 02
    Juan Pablo Zambrano Barajas A01636420
    Created 27/03/2023, Last modification 04/04/2023
    Code created and compiled in replit.com
"""
import graphviz
import re

#Class state, creates a node
class State:
  def __init__(self, is_accepted=False) -> None:
    global g_counter
    self.label = g_counter
    g_counter += 1
    self.is_accepted = is_accepted

#Class transition, creates the value of the node
class Transition:
  def __init__(self, transition: str, state) -> None:
    self.transition = transition
    self.state = state

class NFA:
  def __init__(self) -> None:
    begin_state = State()
    self.begin_state = begin_state
    self.end_state = [begin_state]
    self.transitions = {begin_state.label: []}

  def concatenate(self, nfa):
    for i in self.end_state:
      i.is_accepted = False
      self.transitions[i.label].append(Transition("E", nfa.begin_state))
    self.end_state = nfa.end_state
    self.transitions.update(nfa.transitions)

  def union(self, nfa):
    new_state = State()
    self.transitions[new_state.label] = [
      Transition("E", self.begin_state),
      Transition("E", nfa.begin_state)
    ]
    self.end_state.extend(nfa.end_state)
    self.transitions.update(nfa.transitions)
    self.begin_state = new_state

  def transition(self, transition: str):
    new_state = State(True)
    for i in self.end_state:
      self.transitions[i.label].append(Transition(transition, new_state))
      i.is_accepted = False
    self.end_state = [new_state]
    self.transitions[new_state.label] = []

  def asterisk(self):
    for i in self.end_state:
      self.transitions[i.label].append(Transition("E", self.begin_state))
    new_state = State(True)
    self.transitions[self.begin_state.label].append(Transition("E", new_state))
    self.end_state.append(new_state)
    self.transitions[new_state.label] = []

  def stateFixer(self):
    #We add a new beginning state E that connects to the next state
    newbegin_state = State()
    self.transitions[newbegin_state.label] = [Transition("E", self.begin_state)]
    self.begin_state = newbegin_state
    #We append E states to the other states
    for i in self.end_state:
      i.is_accepted = False
    new_state = State(True)
    for i in self.end_state:
      self.transitions[i.label].append(Transition("E", new_state))
    self.end_state = [new_state]
    self.transitions[new_state.label] = []

  def createGraph(self):
    d = graphviz.Digraph()
    if self.end_state[0].is_accepted:
      d.node(str(self.end_state[0].label), shape="doublecircle")
    d.node(str(self.begin_state.label), color="red")
    for i in self.transitions:
      for j in self.transitions[i]:
        d.edge(str(i), str(j.state.label), label=j.transition)
    d.render("log.txt", view=True)

#We will use reverse polish notation to solve the problem
def reversePolishNotation(regex):
  #We add "." to the string regex
  regex = list(regex)
  alphabet = {"a", "b", "A", "E"}
  for i in range(len(regex) - 1):
    if regex[i] in alphabet and (regex[i + 1] in alphabet or regex[i + 1] == "("):
      regex[i] = regex[i] + "."
    elif regex[i] == "*" and (regex[i + 1] in alphabet or regex[i + 1] == "("):
      regex[i] = regex[i] + "."
    elif regex[i] == ")" and regex[i + 1] in alphabet:
      regex[i] = regex[i] + "."
  regex = "".join(regex)
  queue = []
  stack = []
  precedence = {"*": 3, ".": 2, "+": 1}
  tokens = list(regex)
  for token in tokens:
    if token in {"a", "b", "A", "E"}:
      queue.append(token)
    elif token == "(":
      stack.append(token)
    elif token == ")":
      while stack[-1] != "(":
        queue.append(stack.pop())
        if not stack:
          raise ValueError("Parenthesis error")
      stack.pop()
    elif token in {"U", "*", "."}:
      while stack and stack[-1] != "(" and precedence[
          stack[-1]] >= precedence[token]:
        queue.append(stack.pop())
      stack.append(token)
  while stack:
    popped = stack.pop()
    queue.append(popped)
  regex = "".join(queue)
  possibleStates = {"a", "b", "A", "E"}
  global g_counter
  nfa_stack = []
  g_counter = 0
  if len(regex) == 0:
    return NFA()
  for i in regex:
    if i in possibleStates:
      nfa = NFA()
      nfa.transition(i)
      nfa_stack.append(nfa)
    elif i == ".":
      nfa2 = nfa_stack.pop()
      nfa1 = nfa_stack.pop()
      nfa1.concatenate(nfa2)
      nfa_stack.append(nfa1)
    elif i == "+":
      nfa2 = nfa_stack.pop()
      nfa1 = nfa_stack.pop()
      nfa1.union(nfa2)
      nfa_stack.append(nfa1)
    elif i == "*":
      nfa = nfa_stack.pop()
      nfa.asterisk()
      nfa_stack.append(nfa)
  finalNFA = nfa_stack.pop()
  finalNFA.stateFixer()
  return finalNFA

def postNFA(postfix: str):
  possibleStates = {"a", "b", "A", "E"}
  global g_counter 
  g_counter = 0
  nfa_stack = []
  if len(postfix) == 0:
    return NFA()
  for i in postfix:
    if i in possibleStates:
      nfa = NFA()
      nfa.transition(i)
      nfa_stack.append(nfa)
    elif i == "*":
      nfa = nfa_stack.pop()
      nfa.asterisk()
      nfa_stack.append(nfa)
    elif i == ".":
      nfa2 = nfa_stack.pop()
      nfa1 = nfa_stack.pop()
      nfa1.concatenate(nfa2)
      nfa_stack.append(nfa1)
    elif i == "+":
      nfa2 = nfa_stack.pop()
      nfa1 = nfa_stack.pop()
      nfa1.union(nfa2)
      nfa_stack.append(nfa1)
  finalNFA = nfa_stack.pop()
  finalNFA.stateFixer()
  return finalNFA

def main():
  #It accepts the following inputs:
  #a,b,.,+,*
  
  #regex = '(a+ab)*'
  #regex = 'ab*'
  regex = input("Enter the regex: ")
  regex = regex.replace(" ", "").replace("{","(").replace("}",")")
  try:
    regex = reversePolishNotation(regex)
    regex.createGraph()
  except re.error as e:
    #Catches an invalid regular expression "(ab" for example
    print(f"Invalid regular expression: {e}")

if __name__ == "__main__":
  main()