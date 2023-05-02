from collections import deque
import graphviz as pgv

expression = "ba U (ab U (a U (a U b) U (ba U a) U (ba U a))) U (a U b)*"
stack = deque()
temp_nfa = []
current_nfa = []
nivel_nfa = [[]]
niveles_nfa = []
nivel = 0

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


def nfa_to_graphviz(nfa, nivel):
    nivel = nivel + 1
    nivel_nfa.append([])
    cont = 0;
    niveles_nfa.append('1')
    nivelStr = "lvl " + str(nivel) + "." + niveles_nfa[nivel-1]
    if nivelStr  in nivel_nfa[nivel-1]:
        niveles_nfa[nivel-1] = str(int(niveles_nfa[nivel-1])+1)  
    nivel_nfa[nivel-1].append("lvl " + str(nivel) + "." + niveles_nfa[nivel-1])
        
    for i in nfa:
        if isinstance(i, list) == False:
            nivel_nfa[nivel-1].append(i)
        if isinstance(i, list):
                cont = cont + 1
                niveles_nfa[nivel-1] =  str(cont)
                nivel_nfa[nivel-1].append("Nivel " + str(nivel + 1) + "." + str(cont))
    for j in nfa:
        if isinstance(j, list):
            nfa_to_graphviz(j, nivel)


nfa_to_graphviz(current_nfa, nivel)
nivelCont = 0
for i in nivel_nfa:
    nivelCont = nivelCont + 1
    if i != []:
        print("Nivel: " + str(nivelCont))
        print(i)