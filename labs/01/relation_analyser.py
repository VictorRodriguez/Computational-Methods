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
                    if (c not in self.values[connection]): # No admite conexiones repetidas
                        self.values[connection].append(c)
                        isNode = True
                        connection = ''

    def isReflexive(self) -> bool:
        for node in self.values:
            if node not in self.values[node]:
                return False
        return True
    
    def isSymmetric(self) -> bool:
        for node in self.values:
            for relations in self.values[node]:
                if (node not in self.values[relations]): #
                    return False
        return True

    def isTransitive(self) -> bool:
        for node in self.values:
            for relations in self.values[node]:
                for z in self.values[relations]:
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
        reflexive = self.isReflexive()
        symmetric = self.isSymmetric()
        transitive = self.isTransitive()
        print("(a) R is{} reflexive".format("" if reflexive else ' not'))
        print("(b) R is{} symmetric".format("" if symmetric else ' not'))
        print("(c) R is{} transitive".format("" if transitive else ' not'))
        print("(d) R does{} have an equivalence relation".format("" if reflexive and symmetric and transitive else 'not'))

def main():
    #g = Graph("{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3), (1,3), (3,1) }") # Should be reflexive, symmetric and transitive
    #g = Graph("{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}") # Should be reflexive, NOT symmetric and transitive
    #g = Graph("{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3), (3, 1)}") # Should be reflexive, NOT symmetric and NOT transitive
    #g = Graph("{(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)}") # Should NOT be Reflexive, and yes symmetric and NOT transitive
    #g = Graph("{(0,0), (1,1), (0,1), (1,0)}") # Should be reflexive, symmetric and transitive
    #g = Graph("{(0,0), (1,0)}") # Should NOT be reflexive, NOT symmetric and yes transitive
    #g = Graph("{}") # Should be reflexive, symmetric and transitive
    #g = Graph("{(0,0), (1,1) (0,0)}") # Should be reflexive, symmetric and transitive
    print("Hello World analyzing input!")
    g = Graph(input("Enter your set: "))
    print("Your set is:", g.values)
    g.isEquivalence()
    g.plot()

if __name__ == "__main__":
    main()
