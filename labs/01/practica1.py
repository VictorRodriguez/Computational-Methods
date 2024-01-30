#José Guerrero A01285612
#8 de enero del 2024

from graphviz import Digraph

# Creamos el objeto de Graphviz
dot = Digraph()

#Funcion para verificar si el set es reflexivo
def is_reflexive(set):
    for element in set:
        #Por elemento(secuencia) en el set, creamos una secuencia con el elemento 0 y el elemento 0 para buscar los pares
        #en el set ej.- (0,0) (1,1) (2,2) (3,3)
        if (element[0], element[0]) not in set: #Si no se encuentra el par, regresa False
            return False
        else:
            pass
        #Si sale del loop, regresa True
    return True


#Funcion para verificar si el set es simetrico
def is_symmetric(set):
    for element in set: #Por cada secuencia en el set
        #Creamos una secuencia para buscar el opuesto del elemento
        if (element[1], element[0]) not in set: 
            #Si no se encuentra el opuesto, regresa False
            return False
        else:
            #Si se encuentra, pasa al siguiente elemento
            pass
    #Si sale del loop, regresa True
    return True


#Funcion para verificar si el set es transitivo
def is_transitive(set):
    #Por cada secuencia en el set
    for element in set:
        #Agarramos una segunda secuencia para buscar el opuesto del elemento
        for element2 in set:
            #Si el segundo elemento de la primera secuencia es igual al primer elemento de la segunda secuencia
            if element[1] == element2[0]: 
                #Creamos secuencia de elemento[0] y elemento2[1] para buscar si esta en el set
                if (element[0], element2[1]) not in set:
                    return False
    return True

# Set a verificar
set = {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)}

# Llamamos a las funciones y las imprimimos
print("Reflexive:", is_reflexive(set))
print("Symmetric:", is_symmetric(set))
print("Transitive:", is_transitive(set))

#-------------------------GRAPHVIZ-------------------------#

# Metodos para usar Graphviz
dot.attr(rankdir='LR')
dot.attr('node', shape='circle')

#Creamos los nodos
dot.edge('0', '0')
dot.edge('0', '1')
dot.edge('0', '3')
dot.edge('1', '0')
dot.edge('1', '1')
dot.edge('2', '2')
dot.edge('3', '0')
dot.edge('3', '3')

#Renderizamos la imagen
dot.render('example_graph', format='png', cleanup=True)
