import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

# By Carlos Alberto Veryan Peña A01641147

def analyze(set):
    """
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = False
    Symmetric = False
    Transitive = False

    dict = {}

    for x in set:
        start = x[0]
        end = x[1]

        if (start == end): 
            Reflexive = True
        else:
            if (start not in dict):
                dict[start] = []
            
            if (x[::-1] in set):
                Symmetric = True
            
            dict[start].append(end)
        

    for val in dict.values():
        if tuple(val) in set: Transitive = True

    return Reflexive,Symmetric,Transitive

def plot(set):

    g = graphviz.Digraph('G', filename='hello.gv')
    g.attr('node', shape='circle')
    g.attr(rankdir='LR')
    for x in set:
        g.edge(str(x[0]), str(x[1]))

    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter a set: ")
    val = set(eval(val))
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
