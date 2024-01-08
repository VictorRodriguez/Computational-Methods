import graphviz # https://graphviz.readthedocs.io/en/stable/index.html


def analyze(val):
    """
    1. Reflexive: aRa for all a in X.
    2. Symmetric: aRb implies bRa for all a,b in X.
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X.
    """
    tuples = set()
    edge_dict = {}
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    equal_pair_numbers = 0
    # Parse the input, assuming the input is a valid relation of tuples in the
    # form of (x, y), where x and y are positive integers,
    # e.g. {(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)}
    # and that all the found nodes are part of the alphabet set
    open_parenthesis = []
    first_tuple_val_completed = False
    first_tuple_val_digits, second_tuple_val_digits = [], []
    for ch in val:
        # Start of a tuple
        if ch == '(':
            open_parenthesis.append(ch)
        # End of a tuple
        elif ch == ')':
            first_tuple_val = int(''.join(first_tuple_val_digits))
            second_tuple_val = int(''.join(second_tuple_val_digits))
            # Add each tuple
            tuples.add((first_tuple_val, second_tuple_val))
            # Associate each node with its neighbors
            # First tuple value
            if first_tuple_val not in edge_dict:
                edge_dict[first_tuple_val] = set()
            edge_dict[first_tuple_val].add(second_tuple_val)
            # Second tuple value
            if second_tuple_val not in edge_dict:
                edge_dict[second_tuple_val] = set()
            open_parenthesis.pop()
            first_tuple_val_completed = False
            first_tuple_val_digits, second_tuple_val_digits = [], []
        # Inside a tuple
        elif ch in numbers:
            # Get digits of each value of a tuple
            if not first_tuple_val_completed:
                first_tuple_val_digits.append(ch)
            else:
                second_tuple_val_digits.append(ch)
        # Comma between values of a tuple
        elif ch == ',' and open_parenthesis:
            first_tuple_val_completed = True
        
    Reflexive = True
    Symmetric = True
    Transitive = True
    
    # Check for reflexivity
    for key, value in edge_dict.items():
        if key not in value:
            Reflexive = False
        else:
            edge_dict[key].remove(key) # Remove reflexive pair
        # Prepare dictionary for transitivity check
        # (add neighbors of neighbors)
        for neighbor in value:
            edge_dict[key] = value.union(edge_dict[neighbor])
    
    # Check for symmetry (first check)
    for pair in tuples:
        if pair[0] == pair[1]:
            equal_pair_numbers += 1
        elif (pair[1], pair[0]) not in tuples:
            Symmetric = False
    
    # Check for transitivity (first check)
    for key, value in edge_dict.items():
        for neighbor in value:
            if (key, neighbor) not in tuples:
                Transitive = False
    
    # Check for symmetry and transitivity (second check)
    if len(tuples) == equal_pair_numbers:
        Symmetric = False
        Transitive = False

    return Reflexive,Symmetric,Transitive,tuples

def plot(tuples):
    """Here goes your code to do the plot of the set."""
    g = graphviz.Digraph('G', filename='hello.gv')
    for pair in tuples:
        g.edge(str(pair[0]), str(pair[1]))
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    Reflexive,Symmetric,Transitive,tuples = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(tuples)

if __name__ == "__main__":
    main()
