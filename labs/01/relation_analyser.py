import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = False
    Symmetric = False
    Transitive = True
    
    for(a,b) in val:
            if a == b: # Symmetric
                Reflexive = True
            for (c,d) in val:
                if b == c: # Statement is useful for  both transitive and symmetric
                    if(a == d): # Symmetric
                        Symmetric = True
                    if(a,d) not in val:  # Transitive
                        Transitive = False
            
    return Reflexive,Symmetric,Transitive

def plot():
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='hello.gv')
    g.edge('Hello', 'World')
    g.view()

def main():
    print("Hello World analyzing input!")
    val = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    # val = input("Enter your set: ") 
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot()

if __name__ == "__main__":
    main()

