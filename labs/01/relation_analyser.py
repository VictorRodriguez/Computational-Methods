import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    adj_list = {}

    num1 = None
    num2 = None
    curr_s = ""
    in_el = False;

    for c in val:
        if c == '(':
            in_el = True
            continue

        if c == ')':
            in_el = False
            num2 = int(curr_s)
            curr_s = ""

            print(f"{num1} - {num2}")

            if not adj_list.get(num1):
                adj_list[num1] = [num2]
                if not adj_list.get(num2):
                    adj_list[num2] = []
            else: adj_list[num1].append(num2)

            continue

        if in_el:
            if c == ',':
                num1 = int(curr_s)
                curr_s = ""
                continue

            curr_s += c

    print(adj_list)

    Reflexive = True
    Symmetric = True
    Transitive = True

    for e in adj_list:
        print(f"{e} - ")
        if not e in adj_list[e]:
            Reflexive = False

        for e2 in adj_list[e]:
            print(e2)
            if not e in adj_list[e2]:
                Symmetric = False

            if e2 != e:
                for e3 in adj_list[e2]:
                    if e3 != e and e3 != e2:
                        if not e3 in adj_list[e]:
                            Transitive = False

    return Reflexive,Symmetric,Transitive, adj_list

def makeFileFormat(list):
    f = open("graph.log", "w")
    f.write("digraph example {\n\n\trankdir=LR;\n\tnode [shape = circle];\n")
    
    for e in list:
        if len(list[e]) > 0:
            for e2 in list[e]:
                f.write(f"\t{str(e)} -> {str(e2)} ;\n")

    f.write("\n}")

def plot(list):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graph')
    g.attr(rankdir='LR')
    g.attr('node', shape='circle')
    for e in list:
        if len(list[e]) > 0:
            for e2 in list[e]:
                g.edge(str(e), str(e2))
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    Reflexive,Symmetric,Transitive, adj_list = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    makeFileFormat(adj_list)
    plot(adj_list)

if __name__ == "__main__":
    main()
