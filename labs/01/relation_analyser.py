# Ingrid González A01641116
import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):

    #R = set(eval(val)) # convert the input string to set of tuples
    # R = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) } 

    Reflexive = True # R is reflexive if for all x A, xRx.
    for x in set(i for i, _ in val):
        if (x,x) not in val:
            Reflexive = False
            break


    Symmetric = True # R is symmetric if for all x,y A, if xRy, then yRx.
    for x, y in val:
        if (y,x) not in val:
            Symmetric = False
            break

    Transitive = True # R is transitive if for all x,y, z A, if xRy and 
yRz, then xRz.
    for x, y in val:
        for w, z in val:
            if y == w and (x,z) not in val:
                Transitive = False
                break
        if not Transitive:
            break

    return Reflexive,Symmetric,Transitive

def plot(val):
    g = graphviz.Digraph('G', filename='graph.log')
    g.attr('node', shape='circle')
    g.attr(rankdir='LR')
    for i in val:
        g.edge(str(i[0]),str(i[1]))
    g.view()

def main():
    val = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) } 
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. The set is Reflexive: {Reflexive} \
    2. The set is Symmetric: {Symmetric} \
    3. The set is Transitive: {Transitive}")
    plot(val)


if __name__ == "__main__":
    main()
