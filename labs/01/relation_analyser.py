""" XIMENA CANTERA RESÉNDIZ
            08/01/2024     """

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = all((a, a) in val for a, _ in val)
    Symmetric = all((b, a) in val for a, b in val)
    Transitive = all((a, c) in val for a, b in val for _, c in val)

    return Reflexive, Symmetric, Transitive


def plot(val):
    #Create a graphic using graphviz
    g = graphviz.Digraph('G', filename='hello.gv')
    #Add arcs to the graph
    for pair in val:
        g.edge(str(pair[0]), str(pair[1]))
    #Save and view the graph
    g.view()


def main():
    print("Hello World analyzing input!")
    #convert "input" to a "set"
    val_str = input("Enter your set: ")
    print(val_str)
    val = set(eval(val_str))
    
    #Analyze the properties of the set
    Reflexive, Symmetric, Transitive = analyze(val)
    #Print the results
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    #Create and display the graph
    plot(val)


if __name__ == "__main__":
    main()
