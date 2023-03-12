'''
Author: Mariana Bustos Hernández - A01641324
Date: March 09, 2023
Description: This program analysez a set and determines 
            if it is reflexive, symmetric or transitive.
            It also plots the set.
'''

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def adjacency(val):
    #adjacency dictionary
    adj_dict = {i: set() for i in range(len(val))} 

    #add edge from the set
    for i,j in val:
        adj_dict[i].add(j)
        adj_dict[j].add(i)

    #print(adj_dict)

    for i in range(len(adj_dict)):
        if adj_dict[i] == set():
            adj_dict.pop(i)
    
   # print(adj_dict)
    return adj_dict

def analyze(val):
    adj_dict = adjacency(val)

    Reflexive = True # 1. Reflexive: aRa for all a in X,
    for i in adj_dict:
        if i not in adj_dict[i]:
            Reflexive = False
            break

    Symmetric = True  #2. Symmetric: aRb implies bRa for all a,b in X
    for i in adj_dict:
        for j in adj_dict[i]:
            if i != j and i not in adj_dict[j]:
                Symmetric = False
                break
        if not Symmetric:
            break

    Transitive = True #3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    for i in adj_dict:
        for j in adj_dict[i]:
            for k in adj_dict[j]:
                if i != j and i != k and j != k and i not in adj_dict[k]:
                    Transitive = False
                    break
            if not Transitive:
                break
        if not Transitive:
            break

    return Reflexive,Symmetric,Transitive, adj_dict

def isEquivalence(val):
    Reflexive,Symmetric,Transitive,adj_dict = analyze(val)

    print("(a) R is{} reflexive".format("" if Reflexive else " not"))
    print("(b) R is{} symmetric".format("" if Symmetric else "  not"))
    print("(c) R is{} transitive".format("" if Transitive else " not"))

    equivalence = Reflexive and Symmetric and Transitive

    print("(d) R does{} have equivalence relation".format("" if equivalence else " not"))

    plot(adj_dict)


def plot(val):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='Lab 01.gv')
    g.attr(rankdir='LR')
    g.attr('node', shape='circle')
    for i in val:
        g.node(str(i))
        for j in val[i]:
            g.edge(str(i), str(j))

    g.view()

def main():
   # print("Hello World analyzing input!")
    #val = input("Enter your set: ")
   # print(val)

    #val =  { (0,1), (0,3), (1,0), (1,1), (3,0), (3,3)} # not reflexive, symmetric, not transitive
    #val = {(0,0), (0,1), (0,3), (1,0), (1,1), (3,0), (3,3), (3,1), (1,3)} #reflexive, symmetric, transitive
    val = {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)}

    isEquivalence(val)

    #plot()

if __name__ == "__main__":
    main()
