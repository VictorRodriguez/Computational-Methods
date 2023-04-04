#Stefano Herrejon A00571720
#Lab 02
#a,b

#Codigo para convertir una expresion regular en una grafica

import re
import graphviz

#Clase para alamacenar info, inicio, transiciones, estados iniciales y finales
class NFA:
    def _init_(self, start, accept, transitions):
        self.start = start
        self.accept = accept
        self.transitions = transitions


#Funcion para convertir la expresion regular en un automata, usando una pila para conbatir los ()

def reNfa(regex):
    stack = []
    i = 0
    while i < len(regex):
        if regex[i] == "(":
            stack.append("(")
        elif regex[i] == ")":
            subexpr = ""
            while stack[-1] != "(":
                subexpr = stack.pop() + subexpr
            stack.pop()
            if i < len(regex) - 1 and regex[i+1] == "*":
                i += 1
                subnfa = reNfa(subexpr)
                newstart = object()
                newaccept = object()
                subnfa.transitions.append((newstart, None, subnfa.start))
                subnfa.transitions.append((subnfa.accept, None, newaccept))
                subnfa.transitions.append((newstart, None, newaccept))
                subnfa.start = newstart
                subnfa.accept = newaccept
                stack.append(subnfa)
            else:
                stack.append(reNfa(subexpr))
        elif regex[i] == "u":
            stack[-2:] = [NFA(object(), object(), [(stack[-2].start, None, object()), (stack[-1].start, None, object())]) for _ in range(2)]
            stack[-1].transitions += stack[-2].transitions
            stack[-1].transitions += [(object(), None, stack[-2].start), (object(), None, stack[-1].start)]
            stack[-1].accept, stack[-2].start = object(), object()
            stack[-2:] = [stack[-1]]
        elif regex[i] == "*":
            subnfa = stack.pop()
            newstart = object()
            newaccept = object()
            subnfa.transitions.append((newstart, None, subnfa.start))
            subnfa.transitions.append((subnfa.accept, None, newaccept))
            subnfa.transitions.append((newstart, None, newaccept))
            subnfa.start = newstart
            subnfa.accept = newaccept
            stack.append(subnfa)
        else:
            stack.append(NFA(object(), object(), [(object(), regex[i], object())]))
        i += 1
    nfa = stack[0]
    return nfa

#Funcion para usar el automata y convertirlo en una grafica usando la libreria

def nfaDot(nfa):
    dot = graphviz.Digraph()
    dot.attr(rankdir="LR")
    dot.attr("node", shape="circle")
    dot.node(str(nfa.start), shape="doublecircle")
    dot.node(str(nfa.accept), shape="doublecircle")
    dot.attr("node", shape="circle")
    for start, symbol, end in nfa.transitions:
        if symbol is not None:
            dot.edge(str(start), str(end), label=symbol)
        else:
            dot.edge(str(start), str(end), label="e")
    return dot

#Llamada de las funciones
regex = input("Input : ")
#Ejemplo de expresion (abub)*
nfa = reNfa(regex)
dot = nfaDot(nfa)
dot.render("result.gv", view=True)