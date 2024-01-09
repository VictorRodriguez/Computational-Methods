#Aracelli Boza A01662934
def esReflexiva(pares):
  for elemento in set([par[0] for par in pares]):
      if (elemento, elemento) not in pares:
          return False
  return True

def esSimetrica(pares):
  for par in pares:
      inverso = (par[1], par[0])
      if inverso not in pares:
          return False
  return True

def esTransitiva(pares):
  for i in pares:
      for j in pares:
          if i[1] == j[0]:
              compuesto = (i[0], j[1])
              if compuesto not in pares:
                  return False
  return True

def imprimirDigraph(pares):
  digraph = "digraph example {\n 	rankdir=LR;\n 	node [shape = circle];\n"
  for par in pares:
    digraph += f"\t{par[0]} -> {par[1]} ;\n"
  digraph += "}"
  print(digraph)

def ingresar_pares():
  pares = []

  try:
      numPares = int(input("Ingrese el número de pares: "))
  except ValueError:
      print("Ingresa un valor válido para el número de pares")
      return []
    
  for _ in range(numPares):
      try:
          x = int(input("Ingrese el primer elemento del par ordenado: "))
          y = int(input("Ingrese el segundo elemento del par ordenado: "))
          par = (x, y)
          pares.append(par)
      except ValueError:
          print("Ingresa valores válidos para los elementos del par")
  return pares

def main():
  pares = ingresar_pares()

  if not pares:
      print("No se ingresaron pares. Bye")
      return

  imprimirDigraph(pares)

  countEquivalencia = 0
  if esReflexiva(pares):
      print("La relación es reflexiva")
      countEquivalencia += 1
  else:
      print("La relación no es reflexiva")

  if esSimetrica(pares):
      print("La relación es simétrica")
      countEquivalencia += 1
  else:
      print("La relación no es simétrica")

  if esTransitiva(pares):
      print("La relación es transitiva")
      countEquivalencia += 1
  else:
      print("La relación no es transitiva")

  if countEquivalencia == 3:
      print("\nLa relación es de equivalencia")
  else:
      print("\nLa relación no es de equivalencia")

if __name__ == "__main__":
  main()
