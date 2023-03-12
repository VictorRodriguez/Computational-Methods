#Analizador de relaciones
#Israel Vidal Paredes A01750543

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def isReflexive(val):
    for x in val:
        if (x[0] == x[1]):
            return True
    return False

def isSymmetric(val):
    for x in val:
        if (x[1],x[0]) not in val:
            return False
    return True

def isTransitive(val):
    for (a, b) in val:
            for (c, d) in val:
                if b == c and (d, a) not in val:
                    return False
    return True

def analyze(val):
    """
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    
    R = set(eval(val))

    Reflexive = isReflexive(R)
    Symmetric = isSymmetric(R)
    Transitive = isTransitive(R)

    return Reflexive,Symmetric,Transitive

def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    R = set(eval(val))
    g = graphviz.Digraph('G', filename='graph.gv')

    for x in R:
        g.edge(str(x[0]), str(x[1]))
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    # val = "{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }"
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
