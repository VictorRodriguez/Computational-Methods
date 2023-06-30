import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Graph = {}
    x = val.strip("{}")
    x = x.replace(" ","")
    x = x.replace("(","").replace(")","")
    list = x.split(",")
    
    for i in range(0,len(list),2):
        if list[i] in Graph:
            Graph[list[i]].append(list[i+1])
        else:
            Graph[list[i]] = [list[i+1]]
    
    #check if reflexive
    Reflexive = True
    for node in Graph:
        if not node in Graph[node]:
            Reflexive = False
    
    #check if symetric
    Symmetric = True
    for node in Graph:
        for edge in Graph[node]:
            if node != edge:
                if node not in Graph[edge]:
                    Symmetric = False
                
    #check if transitive
    Transitive = True
    for a in Graph:
        for b in Graph[a]:
            if a != b:
                for c in Graph[b]:
                    if a not in Graph[c]:
                        Transitive = False
    
    return Reflexive,Symmetric,Transitive,Graph

def plot(Graph):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='hello.gv')
    for node in Graph:
        for edge in Graph[node]:
            g.edge(node,edge)
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    Reflexive,Symmetric,Transitive,Graph = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}\
    4. Equivalence relation: {Reflexive and Symmetric and Transitive}")
    plot(Graph)

if __name__ == "__main__":
    main()
