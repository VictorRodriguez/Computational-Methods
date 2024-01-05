# Práctica 1: Encontrar si un conjunto es reflexivo, simétrico o transitivo e imprimir el grafo correspondiente usando graphviz.
# Jorge Emiliano Pomar Mendoza A01709338

import os
import graphviz


def es_reflexivo(R):
    for element in R:
        if (element, element) not in R:
            return False
    return True


def es_simetrico(R):
    for element in R:
        if (element[1], element[0]) not in R:
            return False
    return True


def es_transitivo(R):
    for element1 in R:
        for element2 in R:
            if element1[1] == element2[0] and (element1[0], element2[1]) not in R:
                return False
    return True


def main():
    input_R = input("Introduce el conjunto R:")
    R = eval(input_R)

    if es_reflexivo(R):
        print("El conjunto es reflexivo.")
    else:
        print("El conjunto no es reflexivo.")

    if es_simetrico(R):
        print("El conjunto es simétrico.")
    else:
        print("El conjunto no es simétrico.")

    if es_transitivo(R):
        print("El conjunto es transitivo.")
    else:
        print("El conjunto no es transitivo.")

    dot = graphviz.Digraph(comment="Práctica 1")
    for element in R:
        dot.edge(str(element[0]), str(element[1]))
    dot.render(os.path.join(os.path.dirname(__file__), "graph"), view=True)


main()