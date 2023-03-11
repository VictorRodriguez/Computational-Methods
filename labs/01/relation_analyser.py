#Juan Daniel Muñoz Dueñas
#A01641792
#Relation analyzer
#Date: 09/03/2023

from graphviz import Digraph

LOG_FILE_NAME = "graph.log"


def isSymmetric(graph):
    for (node, relation) in graph:
        if(relation, node) not in graph:
            return False
    return True

def isReflexive(graph):
    for node in set(nodes[0] for nodes in graph):
        if (node, node) not in graph:
            return False
    return True

def isTransitive(graph):
    for (node1, relation1) in graph:
        for (node2, relation2) in graph:
            if relation1 == node2:
                if (node1, relation2) not in graph:
                    return False
    return True


def isEquivalence(graph):
    return isReflexive(graph) and isSymmetric(graph) and isTransitive(graph)

def classify(graph):
    print("(a) R is ", end="")
    if isReflexive(graph):
        print("reflexive")
    else:
        print("not reflexive")
    print("(b) R is ", end="")
    if isSymmetric(graph):
        print("symmetric")
    else:
        print("not symmetric")
    print("(c) R is ", end="")
    if isTransitive(graph):
        print("transitive")
    else:
        print("not transitive")
    print("(d) R is ", end="")
    if isEquivalence(graph):
        print("an equivalence relation")
    else:
        print("not an equivalence relation")

def plot(graph):
    # Crear un nuevo grafo dirigido
    dot = Digraph("Grafo", filename=LOG_FILE_NAME)

    # Agregar los nodos y aristas al grafo dirigido
    for edge in graph:
        dot.edge(str(edge[0]), str(edge[1]))

    # Renderizar el grafo dirigido como una imagen PNG
    dot.render()


    # Mostrar la imagen
    dot.view()

def main():
    string = input("Enter a string: ")
    graph = eval(string)
    classify(graph)
    plot(graph)


if __name__ == "__main__":
    main()
    