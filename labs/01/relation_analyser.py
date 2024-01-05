"""
 @Miguel Angel Cabrera Victoria <A01782982@tec.mx>
 Input : {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)} 
"""
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
    Transitive = False

    return Reflexive,Symmetric,Transitive

def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graph.gv')

    pairs = [pair.replace("{", "").replace("}", "").replace("(", "").replace(")", "").strip(',') for pair in val.split(" ")]
    #print(pairs)
    pair_lists = [[int(element) for element in pair.split(',')] for pair in pairs]
    print(pair_lists)
    #print(pairs)

    for pair in pair_lists:
        #print(pair[0], " ", pair[1])
        g.edge(str(pair[0]), str(pair[1]))
    g.view()

def main():
    print("Miguel Angel Cabrera Victoria - A01782982")
    val = input("Enter your set: ")
    # Reflexive,Symmetric,Transitive = analyze(val)
    # print(f"\
    # 1. Reflexive: {Reflexive} \
    # 2. Symmetric: {Symmetric} \
    # 3. Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
