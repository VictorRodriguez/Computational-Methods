import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val, alphabet):
  Reflexive = True
  Symmetric = True
  Transitive = True
  #Reflexive
  for value in alphabet:
    if (value, value) not in val: 
      Reflexive = False
      break
  #Symmetric
  for tupla in val:
    if (tupla[0], tupla[1]) not in val or tupla[1] not in alphabet or tupla[0] not in alphabet:
      Symmetric = False
      break
  #Transitive
  for tupla1 in val:
    for tupla2 in val:
      if (tupla1[0], tupla2[1]) not in val:
        Transitive = False
        break
  return Reflexive, Symmetric, Transitive

def plot(val):
  g = graphviz.Digraph('G', filename='graph.log')
  for tuple in val:
    g.edge(str(tuple[0]),str(tuple[1]))
  g.view()

def main():
  print("Hello World analyzing input!")
  #val = input("Enter your set: ")
  #Set which is Symmetric, Reflexive and Transitive for testing
  #conjunto_tuplasSRT = "{(1,1), (2,2), (3,3), (1,2), (2,1), (1,3), (3,1), (2,3), (3,2)}"
  #alfabetoSRT = { 1, 2, 3}
  #So we dont take half an hour writing 
  val = "{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }"
  print(val)
  #Alphabet is defined
  alphabet = {0, 1, 2, 3}
  #Spaces and periods are removed
  val = val.replace(' ', '').replace('.', '')
  #The string becomes a set of tuples
  set_tuple = set(eval(val))
  #function called
  Reflexive, Symmetric, Transitive = analyze(set_tuple, alphabet)
  print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
  plot(set_tuple)

if __name__ == "__main__":
  main()
