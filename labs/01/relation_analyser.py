import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def TransitiveHelper(edges, key, visit):
  visit.append(key)
  for value in edges[key]:
    if value not in visit:
      TransitiveHelper(edges , value , visit)
    
def Transitive(edges, key):
  visit=[]
  TransitiveHelper(edges,key,visit)
  return visit

def analyze(val):
    
    nodes=[]
    sym={}
    edges={}
    
    for pair in set:
      #Create nodes list
      if pair[0] not in nodes:
        nodes.append(pair[0])


      #Create Symmetric list
      #Source
      if pair[0] not in sym:
        sym[pair[0]]=[0,0]
      #Destination
      if pair[1] not in sym:
          sym[pair[1]]=[0,0]

      sym[pair[0]][0]+=1
      sym[pair[1]][1]+=1

      #Create edges list
      if pair[0] not in edges:
        edges[pair[0]]=[]

      edges[pair[0]].append(pair[1])


      #CHECK
      r=True
      s=True
      t=True
      i=0
    
      for node in nodes:
        #Check Reflexive
        if (node not in edges[node]):
          r=False

        #Check Symmetric
        pair=sym[node]
        if(pair[0]!=pair[1]):
          s=False

      #Check Transitive
      while(t and i<len(nodes)):
        state=nodes[i]
        visit= Transitive(edges, state)
        if (sorted(visit)!=sorted(edges[state])):
          t=False
        i+=1

      print("nodes: ",nodes)
      print("edges: ",edges)
      print("degree in/out: ",sym)
      return r,s,t

def plot():
    """
    Here goes your code to do the plot of the set
    """
    
    #CREATE GRAPH
    graph=graphviz.Digraph('G', filename='Lab_01')

    #LEFT TO RIGHT
    graph.attr(rankdir='LR')

    #SHAPE
    graph.attr('node', shape='circle')

    #EDGES
    for i in info:
      graph.edge(str(i[0]),str(i[1]))

    graph.view()

    
   
def main():
    #print("Hello World analyzing input!")
    #val = input("Enter your set: ")
    val= { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot()

if __name__ == "__main__":
    main()
