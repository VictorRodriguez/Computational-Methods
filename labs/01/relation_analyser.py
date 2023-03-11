# Heber Giovanni Moran Briones - A01642300

# IMPORTANTE -> Mantener el nombre del archivo en main.py

import graphviz as gv


# Función que determina si el set es reflexivo
def is_reflexive(R):
  for i in R:
    if (i, i) not in R:
      return False
    else:
      return True


# Función que determina si el set es simétrico
def is_symetric(R):
  for i, j in R:
    if (j, i) not in R:
      return False
  return True


#Función que determina si el set es transitivo
def is_transitive(R):
  for i in R:
    for j in R:
      for s in R:
        if (i, j) in R and (j, s) in R and (s, i) not in R:
          return False
  return True


# Prints de resultados en para ambos casos de cada función
def analyze(R):
  if is_reflexive(R) == True:
    print("Es reflexivo")
  else:
    print("No es reflexivo")

  if is_symetric(R) == True:
    print("Es simetrico")
  else:
    print("No es simetrico")

  if is_transitive(R) == True:
    print("Es transitivo")
  else:
    print("No es transitivo")


# Import del set a un script
def plot(conjunto, archivo):
  g = gv.Digraph()
  for a, b in conjunto:
    g.edge(str(a), str(b))
  g.render(archivo, format='png')


def main():
  # Casos de prueba
  R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)}

  S = {(0, 0), (1, 0)}

  T = {(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)}

  print("Caso de prueba 1\n")
  analyze(R)

  print("\n---------------")

  print("\nCaso de prueba 2\n")
  analyze(S)

  print("\n---------------")

  print("\nCaso de prueba 3\n")
  analyze(T)

  #Solamente usé esta función con un solo set (Set del ejercicio)
  plot(R, "graph.log")


if __name__ == "__main__":
  main()
