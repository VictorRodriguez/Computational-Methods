from collections import deque
import graphviz as pgv

expression = "ba U (ab U (a U b)) U (a U b)*"
stack = deque()
temp_nfa = []
current_nfa = []

for i in expression:
    if i == "(":
        stack.append(i)
        temp_nfa.append(current_nfa)
        current_nfa = []
    elif i == ")":
        stack.pop()
        temp_nfa[-1].append(current_nfa)
        current_nfa = temp_nfa.pop()
    elif not i.isspace():
        current_nfa.append(i)

cont = 0;
for j in current_nfa:
    for k in range(len(j)):
        if(j[k]== "a" or j[k] == "b"):
            cont += 1

        
    print(j)
    
# Falta terminar el parsing de matriz de listas al formato de NFA de graphviz
# Planeo terminarlo mañana a primera hora