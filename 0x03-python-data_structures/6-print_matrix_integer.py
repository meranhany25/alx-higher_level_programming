#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ A function that prints integers from a list of lists """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")
