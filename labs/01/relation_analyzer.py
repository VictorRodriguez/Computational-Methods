#Juan Daniel Muñoz Dueñas
#A01641792
#Relation analyzer
#Date: 09/03/2023

from graphviz import Digraph

LOG_FILE_NAME = "graph.log"


def parse(string):
    adj_list = {}
    flag = True
    for char in string:
        if char.isnumeric():
            if flag:
                if char not in adj_list:
                    adj_list[char] = []
                flag = False
                node = char
            else:
                adj_list[node].append(char)
                flag = True
                node = ''   
    return adj_list

def print_graph(adj_list):
    print(adj_list)

def isReflexive(adj_list):
    for node in adj_list:
        if node not in adj_list[node]:
            return False
    return True

def isSymmetric(adj_list):
    for v in adj_list:
        adyacent = adj_list[v]
        for a in adyacent:
            if v not in adj_list[a]:
                return False
    return True


def isTransitive(adj_list):
    for node in adj_list:
        for adyacent in adj_list[node]:
            if(adyacent != node):
                for adyacent2 in adj_list[adyacent]:
                    if(adyacent2 != node and adyacent2 not in adj_list[node]):
                        return False
                    

def isEquivalence(adj_list):
    if(isReflexive(adj_list) and isSymmetric(adj_list) and isTransitive(adj_list)):
        return True
    return False

def classify(adj_list):
    print("(a) R is ", end="")
    if isReflexive(adj_list):
        print("reflexive,")
    else:
        print("not reflexive,")
    print("(b) R is ", end="")
    if isSymmetric(adj_list):
        print("symmetric,")
    else:
        print("not symmetric,")
    print("(c) R is ", end="")
    if isTransitive(adj_list):
        print("transitive,")
    else:
        print("not transitive,")
    print("(d) R ", end="")
    if isEquivalence(adj_list):
        print("have equivalence relation-")
    else:
        print("does not have equivalence relation")

def plot (adj_list):
    dot = Digraph(comment='Graph', filename = LOG_FILE_NAME)
    for node in adj_list:
        for relation in adj_list[node]:
            dot.edge(node, relation)
    dot.render(engine='dot', view=True, format='pdf')

def main():
    string = input("Enter a string: ")
    adj_list = parse(string)
    plot(adj_list)
    classify(adj_list)
    print_graph(adj_list)

if __name__ == "__main__":
    main()
    