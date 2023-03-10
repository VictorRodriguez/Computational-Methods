import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

class Graph:
    def __init__(self, str) -> None:
        self.values = {}
        isNode = True
        connection = ''
        for c in str:
            if (c.isnumeric()):
                if isNode: #Si es nodo
                    if (c not in self.values): #Si no lo encuentra en el grafo
                        self.values[c] = []
                    isNode = False
                    connection = c
                else:
                    self.values[connection].append(c)
                    isNode = True
                    connection = ''

    def print(self):
        print(self.values)

    def isReflexive(self) -> bool:
        for node in self.values:
            if node not in self.values[node]:
                return False
        return True
    
    def isSymmetric(self) -> bool:
        for node in self.values:
            for relations in self.values[node]:
                if (relations != node):
                    if (node not in self.values[relations]): #
                        return False
        return True

    def isTransitive(self) -> bool:
        #Check if we have more than 2 nodes
        if (len(self.values) < 3):
            return False
        for node in self.values:
            for relations in self.values[node]:
                if (relations != node):
                    for z in self.values[relations]:
                        if (z != node and z != relations):
                            if (z not in self.values[node]):
                                return False
        return True
    
    def plot(self) -> None:
        # Create a graphviz graph object and display it on screen
        d = graphviz.Digraph(format='png')
        for node in self.values:
            for relations in self.values[node]:
                d.edge(node, relations)
        d.render('test-output/round-table.gv', view=True)
    
    def isEquivalence(self) -> None:
        if (len(self.values) == 0):
            print("There are no nodes in the graph")
            return
        print(f"\
    1. Reflexive: {self.isReflexive()} \
    2. Symmetric: {self.isSymmetric()} \
    3. Transitive: {self.isTransitive()}")

def main():
    #g = Graph("{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3), (1,3), (3,1) }") # Should be reflexive, symmetric and transitive
    #g = Graph("{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}") # Should be reflexive, NOT symmetric and transitive
    #g = Graph("{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3), (3, 1)}") # Should be reflexive, NOT symmetric and transitive
    #g = Graph("{(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)}") # Should NOT be Reflexive, and yes symmetric and yes transitive
    #g = Graph("{(0,0), (1,1), (0,1), (1,0)}") # Should be reflexive, symmetric and NOT transitive
    #g = Graph("{(0,0), (1,0)}") # Should be reflexive, symmetric and NOT transitive
    print("Hello World analyzing input!")
    g = Graph(input("Enter your set: "))
    g.print()
    g.isEquivalence()
    g.plot()

if __name__ == "__main__":
    main()
