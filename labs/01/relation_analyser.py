import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html d
"""
Name: Juan José Salazar Cortés
ID: A01642126
Date: Saturday March 11 2023
"""
# Input:
# # A = { 0,1,2,3 }
# # R = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
# Output:
# 1. Reflexive: True     2. Symmetric: True     3. Transitive: False


# Input:
# A = {1,2,3,4}
# R = {(1,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,2), (4,4)}
# Output:
# 1. Reflexive: False     2. Symmetric: False     3. Transitive: True


def analyze(set, relations):

    #Initial States of the Answers
    Reflexive = True
    Symmetric = True
    Transitive = False

    # Cleaning the inputs to make them usable
    symbols = '}{)(,'
    relationsCleaned = relations.translate(str.maketrans('', '', symbols))
    relations = relationsCleaned.split()

    setCleaned = set.translate(str.maketrans('', '', symbols))
    set = setCleaned

    # Checks if is Reflexive
    for num in set:
        reflexiveRelation = num + num
        if (reflexiveRelation not in relations):
            Reflexive = False
            break
    
    # Checks if is Symmetric
    for num in relations:
        if (num[::-1] not in relations):
            Symmetric = False
            break

    # Checks if is Transitive
    for i in range(len(relations)):
        x = relations[i][0]
        y = relations[i][1]
        if (x != y):
            for j in range(len(relations)):
                if (y == relations[j][0] and x != relations[j][1]):
                    k = relations[j][1]
                    for z in range(len(relations)):
                        if (x == relations[z][0] and relations[z][1] == k and y != k):
                            Transitive = True
                            break

    return Reflexive, Symmetric, Transitive

# Creates the graph with the relations given
def plot(relations):
    
    # Cleaning the inputs to make them usable
    symbols = '}{)(,'
    relationsCleaned = relations.translate(str.maketrans('', '', symbols))
    relations = relationsCleaned.split()
    g = graphviz.Digraph('G', filename='graph.log')
    g.edges(relations)
    g.view()


def main():

    set = input("Enter your set: ")
    relations = input("Enter your relations: ")

    Reflexive, Symmetric, Transitive = analyze(set, relations)

    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")

    plot(relations)


if __name__ == "__main__":
    main()
