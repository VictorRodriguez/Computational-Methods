import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

#Nolberto Castro Sánchez
#A01641501
#Reflexivity, Symmetry and Transitivity
#11 de Marzo del 2023

def translate(val):
    array = []
    empty = []
    openbrackets = []

    for n in val:
        if (n == "("):
            openbrackets.append("(")
        elif (n == ")"):
            openbrackets.pop()
            array.append(empty)
            empty = []

        if (len(openbrackets) > 0 and n != "," and n != "("):
            empty.append(n)
    return array

def analyze(val):
    #Reflexive Analisis
    nodes = []
    reflex = []

    for n in val:
        if (n[0] not in nodes):
            nodes.append(n[0])
            reflex.append(n[0])
        
        if (n[0] in nodes):
            if (n[0] == n[1]):
                value = reflex.index(n[0])
                reflex.pop(value)

    #Symmetric Analisis

    sym = []
    for n in val:
        if (n[0] != n[1]):
            pb1 = n[0] + n[1]
            pb2 = n[1] + n[0]
            if (pb1 in sym and pb2 in sym):
                value1 = sym.index(pb1)
                value2 = sym.index(pb2)
                sym.pop(value1)
                sym.pop(value2)
            else:
                sym.append(pb1)
                sym.append(pb2)

    #Transitive Analisis

    nodesTotal = []
    posibilities = []

    for n in val:
        if (n[0] not in nodesTotal):
            nodesTotal.append(n[0])
        if (n[1] not in nodesTotal):
            nodesTotal.append(n[1])

    for n in val:
        for i in val:
            if (n != i):
                pos1 = n+i
                pos2 = i+n
                if (pos1 not in posibilities and pos2 not in posibilities):
                    posibilities.append(pos1)
                    posibilities.append(pos2)
    
    for n in val:
        if (n[0] != n[1]):
            pb1 = n[0] + n[1]
            pb2 = n[1] + n[0]
            if (pb1 in posibilities and pb2 in posibilities):
                value1 = posibilities.index(pb1)
                value2 = posibilities.index(pb2)
                posibilities.pop(value1)
                posibilities.pop(value2)

    
    if (len(reflex) == 0):
        Reflexive = True
    else:
        Reflexive = False

    if (len(sym) == 0):
        Symmetric = True
    else:
        Symmetric = False

    if (len(posibilities) == 0):
        Transitive = True
    else:
        Transitive = False

    return Reflexive,Symmetric,Transitive

def plot(graph):
    g = graphviz.Digraph('G', filename='hello.gv')
    for n in graph:
        start = n[0]
        end = n[1]
        g.edge(start, end)
    g.view()

def graphScript(graph):
    f = open("graph.log", "x")
    f.write("""digraph example {\n
	rankdir=LR;
	node [shape = circle];\n""")
    for n in graph:
        start = n[0]
        end = n[1]
        f.write("\t" + start +  " -> " +  end + ";\n")
    f.write("\n}")
    f.close()

def main():
    print("Hello World analyzing input!")
    val = translate(input("Enter your set: "))
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")

    if (Reflexive and Symmetric and Transitive):
        print("The set does have equivalence relation")
    else:
        print("The set does not have equivalence relation")
        
    plot(val)
    graphScript(val)

if __name__ == "__main__":
    main()
