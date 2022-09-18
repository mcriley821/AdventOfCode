#!/usr/bin/env python
#  --- Day 9: Smoke Basin ---
#  These caves seem to be lava tubes. Parts are even still volcanically active;
#  small hydrothermal vents release smoke into the caves that slowly settles
#  like rain.
#  
#  If you can model how the smoke flows through the caves, you might be able to
#  avoid it and be that much safer. The submarine generates a heightmap of the
#  floor of the nearby caves for you (your puzzle input).
#  
#  Smoke flows to the lowest point of the area it's in. For example, consider
#  the following heightmap:
#  
#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#
#  Each number corresponds to the height of a particular location, where 9 is
#  the highest and 0 is the lowest a location can be.
#  
#  Your first goal is to find the low points - the locations that are lower than
#  any of its adjacent locations. Most locations have four adjacent locations
#  (up, down, left, and right); locations on the edge or corner of the map have
#  three or two adjacent locations, respectively. (Diagonal locations do not
#  count as adjacent.)
#  
#  In the above example, there are four low points: two are in the first row 
#  (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row
#  (also a 5). All other locations on the heightmap have some lower adjacent
#  location, and so are not low points.
#  
#  The risk level of a low point is 1 plus its height. In the above example, the
#  risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels
#  of all low points in the heightmap is therefore 15.
#  
#  Find all of the low points on your heightmap. What is the sum of the risk
#  levels of all low points on your heightmap?
#
#  --- Part Two ---
#  Next, you need to find the largest basins so you know what areas are most
#  important to avoid.
#  
#  A basin is all locations that eventually flow downward to a single low point.
#  Therefore, every low point has a basin, although some basins are very small.
#  Locations of height 9 do not count as being in any basin, and all other
#  locations will always be part of exactly one basin.
#  
#  The size of a basin is the number of locations within the basin, including
#  the low point. The example above has four basins.
#  
#  The top-left basin, size 3:
#  
#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#
#  The top-right basin, size 9:
#  
#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#
#  The middle basin, size 14:
#  
#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#
#  The bottom-right basin, size 9:
#  
#  2199943210
#  3987894921
#  9856789892
#  8767896789
#  9899965678
#
#  Find the three largest basins and multiply their sizes together. In the above
#  example, this is 9 * 14 * 9 = 1134.
#  
#  What do you get if you multiply together the sizes of the three largest
#  basins?

from get_input import get_input
from collections.abc import Iterator
from functools import reduce
from itertools import product


def risk_levels(grid: list[list[int]]) -> Iterator[int]:
    for row_ind, row in enumerate(grid):
        for col_ind, pt in enumerate(row):
            if all(pt < grid[r][c] for r,c in neighbors(grid, row_ind, col_ind)):
                yield pt + 1


def neighbors(grid: list[list[int]], row: int, col: int) -> Iterator[int]:
    if row - 1 >= 0:
        yield row - 1, col
    if col - 1 >= 0:
        yield row, col - 1
    if col + 1 < len(grid[row]):
        yield row, col + 1
    if row + 1 < len(grid):
        yield row + 1, col


def basin_search(grid: list[list[int]]) -> Iterator[int]:
    open = set((x, y) for x, y in product(range(len(grid)), range(len(grid[0]))))

    while len(open):
        sz, closed = basin_fill(grid, {open.pop()})
        yield sz
        open -= closed


def basin_fill(
        grid: list[list[int]], open: set[tuple[int, int]]
            ) -> tuple[int, set[tuple[int, int]]]:
    closed = set()
    basin = set()

    while len(open):
        loc = open.pop()

        if grid[loc[0]][loc[1]] == 9:
            closed.add(loc)
            continue
        
        basin.add(loc)

        for neighbor in neighbors(grid, *loc):
            if neighbor not in closed and neighbor not in basin:
                open.add(neighbor)

    return len(basin), basin | closed
            


def main():
    given = get_input(9, 2021)
    grid = [list(map(int, i.strip())) for i in given.split()]
    
    print("Part 1:", sum(risk_levels(grid)))

    basins = tuple(sorted(basin_search(grid), reverse=True))
    print("Part 2:", reduce(lambda x, y: x * y, basins[:3], 1))


if __name__ == "__main__":
    main()

