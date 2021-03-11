#!/usr/bin/env python3
def matrix_shape(matrix):
    if type(matrix[0]) != list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
