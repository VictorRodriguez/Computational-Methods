'''
Nancy Silva Alvarez. A00833627
This program determines whether a given set forms a reflexive, symmetric, or transitive relation, and further checks if it qualifies as an equivalence relation. 
Additionally, it provides a visual representation of the relation through a directed graph using the graphviz library.
'''
import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(tupla):
  Reflexive = False
  Symmetric = False
  Transitive = False
  
  elementos = set()
  for par in tupla:
    elementos.add(par[0])
    elementos.add(par[1])

  # Reflexive (aRa for all a in )
  for elemento in elementos:
    if (elemento, elemento) not in tupla:
      Reflexive = False
      break
    else:
      Reflexive = True
  
  # Symmetric: aRb implies bRa for all a,b in X
  for par in tupla:
    if (par[1], par[0]) not in tupla:
      Symmetric = False
      break
    else:
      Symmetric = True

  # Transitive: aRb and bRc imply aRc for all a,b,c in X
  for a in elementos:
    for b in elementos:
      for c in elementos: 
        if (a,b) in tupla and (b,c) in tupla and (a,c) not in tupla:
          Transitive = False
          break
      if not Transitive:
        break
    if not Transitive:
      break
  else:
    Transitive = True 

  return Reflexive, Symmetric, Transitive    


def plot(tupla):
  grafica = graphviz.Digraph('example', filename='graph')
  for i in tupla:
      grafica.edge(str(i[0]), str(i[1]))
  grafica.view()


def main():
  print("Hello World analyzing input!")
  val = input("Enter your set: ")
  print(val)

  tupla = eval(val)   #De cadena a una estructura de datos 

  Reflexive,Symmetric,Transitive = analyze(tupla)
  plot(tupla)

  #Output
  print("(a) R is" + ("" if Reflexive else " not") + " reflexive.") #Reflexive
  print("(b) R is" + ("" if Symmetric else " not") + " symmetric.") #Symmetric
  print("(c) R is" + ("" if Transitive else " not") + " transitive.") #Transitive
  print("(d) R does" + ("" if Reflexive and Symmetric and Transitive else " not") + " have equivalence relation.") #Equivalence 


if __name__ == "__main__":
  main()
