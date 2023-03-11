# Reflexivity, Symmetry and Transitivity
# Diego Sebastian Garcia Cabrera A01634071
# Implementation of computational methods
# Group: 601
# Tecnologico de Monterrey Campus Guadalajara
# Sabado 11 de Marzo de 2023

#Instructions
# Let R be a binary relation on a set A.
# - R is reflexive if for all x A, xRx.
# - R is symmetric if for all x,y A, if xRy, then yRx.
# - R is transitive if for all x,y, z A, if xRy and yRz, then xRz.

# R is an equivalence relation if A is nonempty and R is reflexive, symmetric and transitive

import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html

#Definition of global variables
listAlphabet = []
setAlphabet = set()
valSet = set()


#This function analy<es input from the user (R) and makes a list with the alphabet
def analyzeAlphabet(val):
  #Iterates val input
  for i in val:
    if i != "," and i != "{" and i != "}" and i != "(" and i != ")" and i != " ":
      #Check if i numbers isnt in the list already
      if not i in listAlphabet:
        listAlphabet.append(int(i))


def Reflexive(valSet, setAlphabet):
  #Iterates tne alphabet
  for i in setAlphabet:
    #Checks if (i,i) is present in the input set
    # If one pair isnt reflexive the whole set isnt reflesive so it returns False, otherwise it completes the for cycle and returns true
    if (i, i) not in valSet:
      return False
  return True


def Symmetric(valSet):
  # Definition of variables x,y as ordered pair of input set R
  for x, y in valSet:
    # Checks symmetric relation of x,y to y,x in R, returns false if y,x not in set input, returns true if for cycle is completed succesfully
    if (y, x) not in valSet:
      return False
  return True


def Transitive(valSet):
  # Definition of variables x,y as ordered pair of input set R
  for x, y in valSet:
    # Definition of variables n,m as ordered pair of input set R
    for n, m in valSet:
      # Checks transitive properties
      if y == n and (n, m) not in valSet:
        # End of function and exits with false
        return False
  return True


def Equiv(valSet, setAlphabet):
  # Input set (R) has a equivalent relation if the set have at least 1 pair and if its reflexive, symmetric and trasnitive, otehrwise its not equivalent
  if Reflexive(valSet, setAlphabet) and Symmetric(valSet) and Transitive(
      valSet) and len(valSet) > 0:
    return True
  else:
    return False


def plot(setAlphabet, valSet):
  with open("graph.log", "w") as f:
    f.write("digraph G {\n")
    for x in setAlphabet:
      f.write(f"{x} [shape=circle]\n")
    for x, y in valSet:
      f.write(f"{x} -> {y}\n")
    f.write("}\n")


def main():
  print(
    "Set example: R = {(0, 1), (0, 0), (3, 1), (1, 1), (0, 3), (3, 0), (3, 3), (2, 2), (1, 0), (1, 3)}"
  )
  print("Hello World analyzing input!")
  # (val) = input set <string>
  val = input("Enter your set: ")
  # Converts R = (val) into a set <set> -> valSet
  valSet = eval(val)
  # Obtains alphabet from (val) into a <list> -< listAlphabet
  analyzeAlphabet(val)
  # Converts (listAlphabet) into a <set> (setAlphabet)
  setAlphabet = set(listAlphabet)
  # Runs predefined functions and return variables for each relation analysis
  Reflexive1 = Reflexive(valSet, setAlphabet)
  Symmetric1 = Symmetric(valSet)
  Transitive1 = Transitive(valSet)
  Equiv1 = Equiv(valSet, setAlphabet)

  #Output for user
  if Reflexive1 == True:
    print("(a) R is reflexive")
  else:
    print("(a) R is not reflexive")
  if Symmetric1 == True:
    print("(b) R is symmetric")
  else:
    print("(b) R is not symmetric")
  if Transitive1 == True:
    print("(c) R is transitive")
  else:
    print("(c) R is not transitive")
  if Equiv1 == True:
    print("(d) R does have equivalence relation")
  else:
    print("(d) R does not have equivalence relation")

  plot(setAlphabet, valSet)


if __name__ == "__main__":
  main()
