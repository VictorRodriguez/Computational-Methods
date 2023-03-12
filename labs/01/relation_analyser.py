import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    Reflexive = False
    Symmetric = False
    Transitive = False
    Equivalence = False

    for x,y in val:
        if(x,x) in val:
            Reflexive = True
        else: 
            Reflexive = False
            break

    for x,y in val:
        if(y,x) in val:
            Symmetric = True
        else:
            Symmetric = False
            break

    for x,y in val:
        for w,z in val:
            if y == w and (x,z) in val:
                Transitive = True
            else: 
                Transitive = False
                break

    if(Reflexive == True & Symmetric == True & Transitive == True):
      Equivalence = True
    else:
      Equivalence = False

    return Reflexive,Symmetric,Transitive,Equivalence

def plot(val):
  g = graphviz.Digraph('G', filename='graph.log')
  g.attr('node', shape='circle')
  g.attr(rankdir='LR')
  for i in val:
    g.edge(str(i[0]),str(i[1]))
  g.view()

def main():
    print("Hello World analyzing input!\n")
    val = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), 
(3, 1)}
    print(val)
    Reflexive,Symmetric,Transitive,Equivalence = analyze(val)
    print(f"\
    \n1. Reflexive: {Reflexive} \
    \n2. Symmetric: {Symmetric} \
    \n3. Transitive: {Transitive}\
    \n4. Equivalence Relation: {Equivalence}")
    plot(val)

if __name__ == "__main__":
    main()
