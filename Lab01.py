#A01640856
#Hugo Alejandro Gomez Herrera

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """

    #Reflexive ------------------------------------>

    elements = set() # Set of all elements in our set
    for pair in val:
        for element in pair:
            elements.add(element)

    Reflexive = True  # We say its reflexive
    for x in elements:
        if (x,x) not in val:
            Reflexive = False  # is not reflexive
            break  # Jump out of the loop
    #---------------------------------------------->


    #Symmetric ------------------------------------>

    Symmetric = True  # We say its symmetric
    for x,y in val:
        if (y,x) not in val: # Check if the symmetric pair is in the set
            Symmetric = False  # is not symmetric
            break  # Jump out of the loop
    #---------------------------------------------->


    #Transitive ------------------------------------>

    Transitive = True  # We say its transitive
    for x,y in val:
        for z,w in val:
            if y == z:  # Check if (x, y) and (y, z) are in R
                if (x,w) not in val:
                    Transitive = False  # is not transitive
                    break  # Jump out of the loop
        if not Transitive:
            break # Jump out of the loop
    #---------------------------------------------->
    

    return Reflexive,Symmetric,Transitive

def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph()

    # Add nodes for each element in R
    for element in set.union(*[set(pair) for pair in val]):
        g.node(str(element))

    # Add edges for each pair in R
    for pair in val:
        g.edge(str(pair[0]), str(pair[1]))

    # Render the graph to a PDF file
    g.render('graph')
    g.view()


def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    #Input looks like this:
    # { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    val = val.replace(" ", "")
    #Converting the user input to a set
    val = eval(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    if(Reflexive and Symmetric and Transitive):
        print("The relation is an equivalence relation")
    else:
        print("The relation is not an equivalence relation")
    plot(val)

if __name__ == "__main__":
    main()