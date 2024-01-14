import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    Reflexive = True
    for a in set(x[0] for x in val):
        if (a, a) not in val:
            Reflexive = False
            break

    Symmetric = True
    for (a, b) in val:
        if (b, a) not in val:
            Symmetric = False
            break

    Transitive = True
    for (a, b1) in val:
        for (b2, c) in val:
            if b1 == b2 and (a, c) not in val:
                Transitive = False
                break

    return Reflexive, Symmetric, Transitive

def imprime(Reflexive, Symmetric, Transitive):
    if (Reflexive):
        print("- (a) R is Reflexive")
    else:
        print("- (a) R is not Reflexive")

    if (Symmetric):
        print("- (b) R is Symmetric")
    else:
        print("- (b) R is not Symmetric")

    if (Transitive):
        print("- (c) R is Transitive")
    else:
        print("- (c) R is not Transitive")
    
def plot(val):
    g = graphviz.Digraph('G', filename = 'graph.log')
    g.attr(rankdir = 'LR')
    g.attr('node', shape = 'circle')

    for (a, b) in val:
        g.edge(str(a), str(b))

    g.view()

def main():
    print("Hello World analyzing input!")

    # { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    # True, True, False
    inpstr = input("Enter your set: ")
    val = eval(inpstr)
    print(val)

    Reflexive, Symmetric, Transitive = analyze(val)
    imprime(Reflexive, Symmetric, Transitive)

    plot(val)

if __name__ == "__main__":
    main()