import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def is_reflexive(val):
    for pair in val:
        if pair[0] == pair[1]:
            return True
    return False


def is_symmetric(val):
    for pair in val:
        if pair[::-1] in val:
            return True
    return False


def is_transitive(val):
    for pair in val:
        if pair[0] == pair[1]:
            continue
        for pair2 in val:
            a_c = (pair[0], pair2[1])
            if pair == pair2 or pair2[0] == pair2[1]:
                continue
            elif pair[1] == pair2[0] and a_c[0] != a_c[1] and a_c in val:
                return True
    return False


def analyze(val):
    """
    Here goes your code to do the analysis
    1. reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    reflexive = is_reflexive(val)
    symmetric = is_symmetric(val)
    transitive = is_transitive(val)


    return reflexive, symmetric, transitive


def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graph.gv')
    g.attr('node', shape='circle')
    g.attr(rankdir='LR')
    for pair in val:
        g.edge(f"{pair[0]}", f"{pair[1]}")
    g.view()


def main():
    print("Hello World analyzing input!")
    graph = set(eval(input("Enter your set: ")))
    print(graph)
    #graph = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    reflexive, symmetric, transitive = analyze(graph)
    
    if reflexive and symmetric and transitive:
        equivalence = True
    else:
        equivalence = False

    print(f"\
    1. Reflexive: {reflexive} \
    2. Symmetric: {symmetric} \
    3. Transitive: {transitive}\
    4. Equivalence relation: {equivalence}")        
    plot(graph)

if __name__ == "__main__":
    main()