#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1])
        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle[i].append(1)
    return triangle
