# Set analysis
# Author: Diego Partida Romero
# ID: A01641113
# Lab 01

import graphviz

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    elements = set()
    for pair in val:
        elements.add(pair[0])
        elements.add(pair[1])
    n = len(elements)
    matrix = [[False] * n for _ in range(n)]
    for pair in val:
        i = list(elements).index(pair[0])
        j = list(elements).index(pair[1])
        matrix[i][j] = True
    Reflexive = all(matrix[i][i] for i in range(n))
    Symmetric = all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    Transitive = all(matrix[i][j] and matrix[j][k] <= matrix[i][k] for i in range(n) for j in range(n) for k in range(n))
    return Reflexive, Symmetric, Transitive

def plot(val):
    g = graphviz.Digraph('G', filename='set.gv')
    for pair in val:
        g.edge(str(pair[0]), str(pair[1]))
    g.view()

def main():
    print("- - - - - - - - - - - - - - - - - - - - - - ")
    print("Author: Diego Partida Romero ID: A01641113\n")
    val = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    print("Set: " , val)
    Reflexive, Symmetric, Transitive = analyze(val)
    if Reflexive and Symmetric and Transitive:
        print("R is an equivalence relation.")
    else:
        if Reflexive:
            print("R is reflexive.")
        if not Reflexive:
            print("R is not reflexive.")
        if Symmetric:
            print("R is symmetric.")
        if not Symmetric:
            print("R is not symmetric.")
        if Transitive:
            print("R is transitive.")
        if not Transitive:
            print("R is not transitive.")
        if not (Reflexive or Symmetric or Transitive):
            print("R is not reflexive, symmetric or transitive.")
        else:
            print("R does not have equivalence relation.")
    plot(val)
    print("- - - - - - - - - - - - - - - - - - - - - - ")

if __name__ == "__main__":
    main()
