import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def main():
    # -*- coding: utf-8 -*-
    """
    Created on Sun Feb 19 19:45:20 2023

    @author: Jesus Enrique Diaz Bernal Robinson Bours
    ID: A00227255
    """

    # Graphviz graph
    g = graphviz.Digraph('G', filename='hello.gv')

    # Variables that check what the set is
    reflex = False
    sym = False
    trans = False

    print("Hello World analyzing input!")
    print("--------------------------")
    print("PLEASE ENTER THE VALUES 1 BY 1 AND FINISH BY ENTERING EMPTY")
    print("EXAMPLE:")
    print("0\n1\n0\n2\n")
    print("Is equal to {(0,1), (0,2)}")

    # Variable where the set will be stored
    nodes = []

    # User inputs the set
    line = input("Enter your set:\n") 
    while(line != ''): 
        nodes.append(tuple(line.split())) 
        line = input() 

    # Variables to add edges to the graph
    tail = ""
    head = ""
    x = 0

    # List with all individual nodes, useful later
    ind_nod = []

    # Add all nodes and edges to graphviz by using the list without repeated nodes
    for i in nodes:
        for j in i:
            if j not in ind_nod:
                ind_nod.append(j)
            g.node(str(j))
            if(x == 1):
                head = str(j)
                g.edge(tail, head)
                head = ""
                tail = ""
                x = 0
            else:
                tail = str(j)
                x+=1

    # Creates graph and opens it
    g.view()


    # List of reflexive nodes
    reflex_nodes = []

    # Checks if the set is REFLEXIVE

    # Makes a list with all the nodes that are reflexive
    # Examples: (0,0), (1,1) 
    for i in nodes:
        for j in i:
            if(x == 1):
                head = j
                if(head == tail):
                    reflex_nodes.append(head)
                head = ""
                tail = ""
                x = 0
            else:
                tail = j
                x+=1

    # Checks that the number of reflexive nodes is the same as the number
    # of individual nodes
    if (len(ind_nod) != len(reflex_nodes)):
        reflex = False
    elif(sorted(ind_nod) == sorted(reflex_nodes)):
        reflex = True


    # Variables for symmetric analysis
    sym_nodes = []
    sym_check = []

    # Checks if the set is SYMMETRIC

    # Creates a list with all connections
    x = 0
    for i in nodes:
        for j in i:
            if(x == 1):
                head = str(j)
                ed = tail+head
                if (head != tail):
                    sym_nodes.append(ed)
                head = ""
                tail = ""
                x = 0
            else:
                tail = str(j)
                x+=1

    for i in sym_nodes:
       sym_check.append(False)

    # Checks if edges are symmetric
    a = 0
    b = 0
    for i in sym_nodes:
        x = i[::-1]
        for j in sym_nodes:
            if (j==x):
                sym_check[a] = True
                sym_check[b] = True
            b+=1
        a+=1
        b = 0

    # Checks if all edges are symmetric
    for i in sym_check:
        if (i==False):
            sym = False
            break
        else:
            sym = True

    #Variables for transitive
    trans_nodes = []
    connections = []


    #Checks if the set is TRANSITIVE

    # Creates a list with all connections (Again)
    x = 0
    for i in nodes:
        for j in i:
            if(x == 1):
                head = str(j)
                ed = tail+head
                if (head != tail):
                    trans_nodes.append(ed)
                head = ""
                tail = ""
                x = 0
            else:
                tail = str(j)
                x+=1


    # Creates a list with all the connections that the set must for it to be transitive
    # This is done by checking every connection that is different
    # Once it has detected one, it looks for a connection that starts with the second node
    # If it finds one, it adds a connection from the initial node to this new second node
    for i in trans_nodes:
        x = i[1]
        for j in trans_nodes:
            if j[0] == x:
                if(i[0] != j[1]):
                    connections.append(i[0]+j[1])

    # Checks that all connections needed for transitive are in the set
    trans = all(elem in trans_nodes for elem in connections)


    # Prints the final results
    print(f"\
        1. Reflexive: {reflex} \
        2. Symmetric: {sym} \
        3. Transitive: {trans}")

if __name__ == "__main__":
    main()
