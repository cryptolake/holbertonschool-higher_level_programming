#!/usr/bin/python3
"""Pascal triangle."""


def pascal_triangle(n):
    """Pascal triangle."""
    tria = [[1]]
    if (n <= 0):
        return []
    for i in range(1, n):
        tria.append([])
        for j in range(0, i + 1):
            if j == 0 or j == i:
                tria[i].append(1)
            else:
                tria[i].append(tria[i-1][j-1] + tria[i-1][j])
    return tria
