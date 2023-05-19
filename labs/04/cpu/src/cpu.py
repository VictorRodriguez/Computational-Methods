"""@package docstring
Documentation for CPU module.
More details.
"""

import csv
import numpy

map_field = numpy.zeros(shape=(4,4))

def func():
    """Documentation for a function.
    More details.
    """
    pass
def do_instruction(inst):
    print(inst)
    print(map_field)

def read_file():
    inst_list = []
    with open('instructions.asm') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            inst_list.append(row)
    return inst_list

def main():
    print("Hello World!")
    inst_list = read_file()
    for inst in inst_list:
        do_instruction(inst)

if __name__ == "__main__":
    main()

