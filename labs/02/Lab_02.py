import pydot

class Estado:
    contador = 0

    def __init__(self, etiqueta=None):
        self.id = Estado.contador
        Estado.contador += 1
        self.etiqueta = etiqueta
        self.transiciones = {}

class NFA:
    def __init__(self, expresion_regular):
        self.inicial = None
        self.final = None
        self.expresion_regular = expresion_regular

    def construir(self):
        pila = []
        for caracter in self.expresion_regular:
            if caracter == '.':
                afn2 = pila.pop()
                afn1 = pila.pop()
                afn1.final.transiciones = afn2.inicial.transiciones
                afn1.final = afn2.final
                pila.append(afn1)
            elif caracter == '|':
                afn2 = pila.pop()
                afn1 = pila.pop()
                inicial = Estado()
                inicial.transiciones.update(afn1.inicial.transiciones)
                inicial.transiciones.update(afn2.inicial.transiciones)
                afn1.final.transiciones[inicial] = None
                afn2.final.transiciones[inicial] = None
                final = Estado()
                afn1.final.transiciones[final] = None
                afn2.final.transiciones[final] = None
                pila.append(NFA(None))
                pila[-1].inicial = inicial
                pila[-1].final = final
            elif caracter == '*':
                afn1 = pila.pop()
                inicial = Estado()
                final = Estado()
                inicial.transiciones[afn1.inicial] = None
                inicial.transiciones[final] = None
                afn1.final.transiciones[afn1.inicial] = None
                afn1.final.transiciones[final] = None
                pila.append(NFA(None))
                pila[-1].inicial = inicial
                pila[-1].final = final
            else:
                inicial = Estado()
                final = Estado()
                inicial.transiciones[final] = caracter
                pila.append(NFA(None))
                pila[-1].inicial = inicial
                pila[-1].final = final
        afn = pila.pop()
        self.inicial = afn.inicial
        self.final = afn.final

    def graficar(self):
        graph = pydot.Dot(graph_type='digraph')
        nodos = set()
        nodos.add(self.inicial)
        nodos.add(self.final)
        for estado in nodos:
            for destino, simbolo in estado.transiciones.items():
                if simbolo is not None:
                    edge = pydot.Edge(str(estado.id), str(destino.id), label=str(simbolo))
                    graph.add_edge(edge)
        graph.write_png('nfa.png')

expresion_regular = 'a*b|c.'
nfa = NFA(expresion_regular)
nfa.construir()
nfa.graficar()