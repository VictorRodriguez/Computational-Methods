import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def parse(val):
    """
    Here goes your code to parse the input
    input will be a string of the form `R = {(a,b),(b,c),(c,a)}`
    """
    #Turn val into a list of tuples
    val = list(val)
    final_val = []
    for i in range(len(val)):
        if val[i] not in ["{","}","(",")", " ", "R", "=", "\n", ","]:
            final_val.append(val[i])
    
    final_val = [(final_val[i], final_val[i+1]) for i in range(0, len(final_val)-1, 2)]
    return final_val


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

    #Check for reflexive
    reflexiveCheck = []
    #Add the single values to check
    for tup in val:
        if tup[0] not in reflexiveCheck:
            reflexiveCheck.append(tup[0])
        if tup[1] not in reflexiveCheck:
            reflexiveCheck.append(tup[1])
    #Check if the tuple is in the set
    for element in reflexiveCheck:
        if (element, element) in val:
            Reflexive = True
        else:
            Reflexive = False
            break

    #Check for symmetric
    for tup in val:
        #Check if the opposite combination is in the set
        if (tup[1], tup[0]) in val:
            Symmetric = True
        else:
            Symmetric = False
            break

    #Check for transitive
    for i in range(len(val)):
        #Skip if the tuple is a loop
        if val[i][0] == val[i][1]:
            continue 
        for j in range(len(val)):
            #Skip if the tuple is a loop or the same tuple
            if val[j][0] == val[j][1] or i == j:
                continue
            #Check if the tuple is transitive
            if val[i][1] == val[j][0] and val[i][0] != val[j][1]:
                if (val[i][0], val[j][1]) in val:
                    Transitive = True
                else:
                    Transitive = False
                    break

    return Reflexive,Symmetric,Transitive

def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='hello.gv')
    for tup in val:
        g.edge(tup[0], tup[1])
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    parsed_val = parse(val)
    Reflexive,Symmetric,Transitive = analyze(parsed_val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(parsed_val)
    #R={(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)}
    
if __name__ == "__main__":
    main()
