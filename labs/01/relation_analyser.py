##Javier Eric Hernández Garza A01635392
import graphviz as gv

def show_graph(R):
    dot = gv.Digraph(comment='Set', format='png')
    for i in R:
        dot.node(str(i[0]), str(i[0]))
        dot.node(str(i[1]), str(i[1]))
        dot.edge(str(i[0]), str(i[1]))
    dot.render('Set.gv', view=True)


def is_reflexive(R):
    for i in R:
        if i[0]==i[1]:
            return True
    return False

def is_symmetric(R):
    for i in R:
        if (i[1],i[0]) not in R:
            return False
    return True
    
def is_transitive(R):
    dic=dict()
    for i in R:
        if i[0] in dic:
            dic[i[0]].append(i[1])
        else:
            dic[i[0]]=[i[1]]
    for i in R:
        if i[1] in dic:
            for j in dic[i[1]]:
                if (i[0],j) not in R:
                    return False
    return True


def main():
    # R = {(1, 2), (1, 3), (2, 3), (3, 4)}
    # R={ (0,0), (0,1), (0,3), (1,0), (1,1  ), (2,2), (3,0), (3,3) } 
    R={ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    print(f"R = {R}")
    print(f"R is reflexive? {is_reflexive(R)}")
    print(f"R is symmetric? {is_symmetric(R)}")
    print(f"R is transitive? {is_transitive(R)}")
    show_graph(R)


if __name__ == "__main__":
    main()