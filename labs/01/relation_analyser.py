import graphviz

def analyze(val):
  """
  Here goes your code to do the analysis
  1. Reflexive: aRa for all a in X,
  2. Symmetric: aRb implies bRa for all a,b in X
  3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
  """

  Reflexive = False
  Symmetric = False
  Transitive = False
  ##PRIMERO REALIZAMOS EL ANALISIS DE REFLEXIVO
  ##OBTENEMOS EL ALFABETO
  value = ""
  alfabeto = []
  for i in range(len(val)):
    value = list(val)[i]
    #print (value)
    for j in range(len(value)):
      #print (value[j])
      while j < len(value):
        if value[j] not in alfabeto:
          alfabeto.append(value[j])
        j = j+1
  #print("alfabeto: ", alfabeto)
  ##AHORA COMPROBAREMOS QUE TODOS LOS SIMBOLOS TENGAN REFLEXION
  cont = len(alfabeto)
  for x in val:
    if x[0] == x[1]:
      cont = cont - 1
  if cont == 0: 
    Reflexive = True

  ##ANALISIS SIMETRICO
  cont= len(val)
  for x in val:
    index0 = x[0]
    index1 = x[1]
    for y in val:
      if y[0] == index1 and y[1] == index0:
        #print ("Cumple simetria", index1, "," , index0)
        cont = cont - 1
  if cont == 0:      
    Symmetric = True
        
  ##ANALISIS TRANSITIVO
  for i in val:
    if i[0] != i[1]:
      for j in val:
        if (j[0] == i[1] and j[1] != i[0] and j[0] != j[1]):
          for k in val:
            if k[0] == i[0] and k[1] == j[1]:
              #print ("Cumple transitividad", i[0], "," , i[1], "," , j[1])
              Transitive = True
  

  return Reflexive,Symmetric,Transitive

def plot(val):
  """
  Here goes your code to do the plot of the set
  """
  g = graphviz.Digraph('G', filename='graph.log')
  g.attr(rankdir='LR')
  g.attr('node',shape='circle')

  for i in val:
    g.edge(str(i[0]),str(i[1]))
  
  g.view()


def main():
    print("Hello World analyzing input!")
    #val = input("Enter your set: ")
    val = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }

    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
