#!/usr/bin/env python
#  --- Day 5: Hydrothermal Venture ---
#  You come across a field of hydrothermal vents on the ocean floor! These
#  vents constantly produce large, opaque clouds, so it would be best to
#  avoid them if possible.
#  
#  They tend to form in lines; the submarine helpfully produces a list of
#  nearby lines of vents (your puzzle input) for you to review. For example:
#  
#  0,9 -> 5,9
#  8,0 -> 0,8
#  9,4 -> 3,4
#  2,2 -> 2,1
#  7,0 -> 7,4
#  6,4 -> 2,0
#  0,9 -> 2,9
#  3,4 -> 1,4
#  0,0 -> 8,8
#  5,5 -> 8,2
#  
#  Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
#  where x1,y1 are the coordinates of one end the line segment and x2,y2 are
#  the coordinates of the other end. These line segments include the points
#  at both ends. In other words:
#  
#  An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#  An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
#  
#  For now, only consider horizontal and vertical lines: lines where either
#  x1 = x2 or y1 = y2.
#  
#  So, the horizontal and vertical lines from the above list would produce
#  the following diagram:
#  
#  .......1..
#  ..1....1..
#  ..1....1..
#  .......1..
#  .112111211
#  ..........
#  ..........
#  ..........
#  ..........
#  222111....
#  
#  In this diagram, the top left corner is 0,0 and the bottom right corner is
#  9,9. Each position is shown as the number of lines which cover that point
#  or . if no line covers that point. The top-left pair of 1s, for example,
#  comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping
#  lines 0,9 -> 5,9 and 0,9 -> 2,9.
#  
#  To avoid the most dangerous areas, you need to determine the number of
#  points where at least two lines overlap. In the above example, this is
#  anywhere in the diagram with a 2 or larger - a total of 5 points.
#  
#  Consider only horizontal and vertical lines. At how many points do at
#  least two lines overlap?
#  
#  --- Part Two ---
#  Unfortunately, considering only horizontal and vertical lines doesn't give
#  you the full picture; you need to also consider diagonal lines.
#  
#  Because of the limits of the hydrothermal vent mapping system, the lines in
#  your list will only ever be horizontal, vertical, or a diagonal line at 
#  exactly 45 degrees. In other words:
#  
#  An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#  An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
#  Considering all lines from the above example would now produce the following
#  diagram:
#  
#  1.1....11.
#  .111...2..
#  ..2.1.111.
#  ...1.2.2..
#  .112313211
#  ...1.2....
#  ..1...1...
#  .1.....1..
#  1.......1.
#  222111....
#   
#  You still need to determine the number of points where at least two lines
#  overlap. In the above example, this is still anywhere in the diagram with a
#  2 or larger - now a total of 12 points.
#  
#  Consider all of the lines. At how many points do at least two lines overlap?
#
from __future__ import annotations
from get_input import get_input
from dataclasses import dataclass
from math import copysign


@dataclass(slots=True)
class Point:
    x: int
    y: int

    @staticmethod
    def from_string(x_y_str: str):
        return Point(*map(int, x_y_str.split(',')))

    def copy(self) -> Point:
        return Point(self.x, self.y)


@dataclass(slots=True)
class LineSegment:
    p1: Point
    p2: Point
    
    @property
    def horizontal(self):
        return self.p1.y == self.p2.y

    @property
    def vertical(self):
        return self.p1.x == self.p2.x

    def __iter__(self):
        return self._iter()

    def _iter(self):
        point = self.p1.copy()
        yield point
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        x_diff = int(copysign(1, dx)) if dx else 0
        y_diff = int(copysign(1, dy)) if dy else 0
        while point != self.p2:
            point.x += x_diff
            point.y += y_diff
            yield point


def main():
    given = get_input(5, 2021)
    str_lines = [i.split(" -> ") for i in given.split("\n") if i]
    pts = [Point.from_string(i) for pair in str_lines for i in pair]
    lines = [LineSegment(x, y) for x, y in zip(*([iter(pts)] * 2))]

    max_x = max(pts, key=lambda x: x.x).x
    max_y = max(pts, key=lambda x: x.y).y

    grid = [0] * ((max_x + 1) * (max_y + 1))
    for line in lines:
        if not (line.vertical or line.horizontal):
            continue
        for pt in line:
            grid[pt.y * (max_x + 1) + pt.x] += 1
    print("Part 1:", sum(1 for i in grid if i > 1))
    
    for line in lines:
        if line.vertical or line.horizontal:
            continue
        for pt in line:
            grid[pt.y * (max_x + 1) + pt.x] += 1
    print("Part 2:", sum(1 for i in grid if i > 1))


if __name__ == "__main__":
    main()

