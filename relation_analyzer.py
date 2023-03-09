# Jorge German Wolburg Trujillo - a01640826
# Relation Analyzer
# Resources: Geek for Geeks

# The set is reflexive if every element in (j, j) in the sT, (j, j) is also present
def isReflexive(sT):
    for x in set([i[0] for i in sT]):
        if (x, x) not in sT:
            return False
    return True

# The set is symmetric when for every element (j, k) in the set, (k, j) is also present
def isSymmetric(sT):
    for x, y in sT:
        if (y, x) not in sT:
            return False
    return True

# The set is transitive when (j, k) and (l, m) are in the set, (j, m) must also be there
def isTransitive(sT):
    for x, y in sT:
        for z, w in sT:
            if y == z and (x, w) not in sT:
                return False
    return True

# To make the set an equivalence rleation, all three properties most be satisfied
def isEquivalenceRelation(sT):
    if isReflexive(sT) and isSymmetric(sT) and isTransitive(sT):
        return True
    return False


input_sT = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 2), (2, 1), (3, 4),
             (4, 3)}

if isReflexive(input_sT):
    print("R is reflexive")
else:
    print("R is not reflexive")

if isSymmetric(input_sT):
    print("R is symmetric")
else:
    print("R is not symmetric")

if isTransitive(input_sT):
    print("R is transitive")
else:
    print("R is not transitive")

if isEquivalenceRelation(input_sT):
    print("R is an equivalence relation")
else:
    print("R is not an equivalence relation")

# Generate file graph.log
with open("graph.log", "w") as f:
    f.write("digraph example {\n")
    f.write("\trankdir=LR;\n")
    f.write("\tnode [shape = circle];\n")
    for x, y in input_sT:
        f.write(f"\t{x} -> {y} ;\n")
    f.write("}\n")
