##Javier Eric Hernández Garza A01635392
import graphviz as gv

def show_graph(R):
    ##Show the graph
    dot = gv.Digraph(comment='Set', format='png')
    for i in R:
        dot.node(str(i[0]), str(i[0]))
        dot.node(str(i[1]), str(i[1]))
        dot.edge(str(i[0]), str(i[1]))
    dot.render('Set.gv', view=True)


def is_reflexive(R):
    ##A set is reflexive if it contains the pair (x,x) for every element x in the set.
    for i in R:
        if i[0]==i[1]:
            return True
    return False

def is_symmetric(R):
    ##A set is symmetric if it contains the pair (x,y) if  it contains the pair (y,x).
    for i in R:
        if (i[1],i[0]) not in R:##Pair (y,x) is not in the set
            return False
    return True
    
def is_transitive(R):
    ##A set is transitive if it contains the pair (x,z) if it contains the pair (x,y) and (y,z) for some y.
    dic=dict()
    for i in R:##Create a dictionary with the pairs (x,y) and (y,x)
        if i[0] in dic:
            dic[i[0]].append(i[1])
        else:
            dic[i[0]]=[i[1]]
    for i in R:##Check if the pair (x,z) is in the set
        if i[1] in dic:
            for j in dic[i[1]]:
                if (i[0],j) not in R:
                    return False
    return True


def main():
    # R = {(1, 2), (1, 3), (2, 3), (3, 4)} #Example 1 (False, False, False)
    # R={ (0,0), (0,1), (0,3), (1,0), (1,1  ), (2,2), (3,0), (3,3) } #Example 2 (True, True, False)
    R={ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) } #Example 3 
    print(f"R = {R}")
    print(f"R is reflexive? {is_reflexive(R)}")
    print(f"R is symmetric? {is_symmetric(R)}")
    print(f"R is transitive? {is_transitive(R)}")
    show_graph(R)


if __name__ == "__main__":
    main()