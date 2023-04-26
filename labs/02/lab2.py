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

# Falta la logica que conecta los niveles con las flechas de los nodos
# graphviz sigue sin funcionar, entonces no sé que tan inecesariamente complicado lo estoy haciendo

# falta tomar mi output, y recorrer nivel por nivel


# si encuentra una U o más en cualquier nivel, agrega un nodo vació del cual se desglosan las dos opciones de la union

# 0->1 [label= SS(E)] 'esto es para el "ba" '
# 0->2 [label= SS(E)] 'esto es para el Nivel 2.1'
# 0->3 [label= SS(E)] 'esto es para el Nivel 2.2'

# si encuentra un * en cualquier nivel, agrega una flecha del ultimo elemennto al primero, entre en parentesis de ser necesario

# de ahí en más, conecta los nodos con flechas, llevando un contador global

# 0->1 [label= SS(E)] 'esto es para el "ba" '

# 1->4 [label= S(b)] 'esto es para el "b" del "ba" '
# 4->5 [label= S(#end a)] 'esto es para el "a" del "ba" '

# 0->2 [label= SS(E)] 'esto es para el Nivel 2.1 (ab U Nivel 3.1)'
# 2->6 [label= S(E)] 'esto es para el ab de la union' del Nivel 2.1'
# 6->7 [label= S(a)] 'esto es para el "a" del "ab" '
# 7->8 [label= S(b)] 'esto es para el "b" del "ab" '

# 2->9 [label= S(E)] 'esto es para el Nivel3.1 en la union' del Nivel 2.1'
# hacemos el degloce del Nivel 3.1, esto es recursivo

# pero ya llevo bastante tiempo atorado, entonces lo voy a dejar así por el momento
# voy a volver a intentarlo desde mi laptop linux, pero sí creo que lo estoy haciendo
# incesariamente complicado, y que hay una forma más sencilla de hacerlo

# sé que esta lógica funciona, pero voy a tener que refactorizar

