#!/usr/bin/python3
"""
function that returns the perimeter
of the island described in grid
"""


def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                # Each land cell contributes 4 to the perimeter

                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                    # Reduce perimeter by 2 if left cell is land

                # Check top cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                    # Reduce perimeter by 2 if top cell is land

    return perimeter
