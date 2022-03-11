#!/usr/bin/env python
# Day 18 - Advent of Code 2015 
# --- Day 18: Like a GIF For Your 
# Yard --- 
# 
# After the million lights incident, 
# the fire code has gotten stricter: 
# now, at most ten thousand lights 
# are allowed. You arrange them in a 
# 100x100 grid. 
# 
# Never one to let you down, Santa 
# again mails you instructions on 
# the ideal lighting configuration. 
# With so few lights, he says, 
# you'll have to resort to 
# animation. 
# 
# Start by setting your lights to 
# the included initial configuration 
# (your puzzle input). A # means 
# "on", and a . means "off". 
# 
# Then, animate your grid in steps, 
# where each step decides the next 
# configuration based on the current 
# one. Each light's next state 
# (either on or off) depends on its 
# current state and the current 
# states of the eight lights 
# adjacent to it (including 
# diagonals). Lights on the edge of 
# the grid might have fewer than 
# eight neighbors; the missing ones 
# always count as "off". 
# 
# For example, in a simplified 6x6 
# grid, the light marked A has the 
# neighbors numbered 1 through 8, 
# and the light marked B, which is 
# on an edge, only has the neighbors 
# marked 1 through 5: 
# 
# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
# The state a light should have next 
# is based on its current state (on 
# or off) plus the number of 
# neighbors that are on: 
# 
# A light which is on stays on when 
# 2 or 3 neighbors are on, and turns 
# off otherwise. 
# A light which is off turns on if 
# exactly 3 neighbors are on, and 
# stays off otherwise. 
# All of the lights update 
# simultaneously; they all consider 
# the same current state before 
# moving to the next. 
# 
# Here's a few steps from an example 
# configuration of another 6x6 grid: 
# 
# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
# 
# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
# 
# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
# 
# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
# 
# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
# After 4 steps, this example has 
# four lights on. 
# 
# In your grid of 100x100 lights, 
# given your initial configuration, 
# how many lights are on after 100 
# steps? 
# 
# Your puzzle answer was 1061.
# 
# The first half of this puzzle is 
# complete! It provides one gold 
# star: * 
# 
# --- Part Two ---
# 
# You flip the instructions over; 
# Santa goes on to point out that 
# this is all just an implementation 
# of Conway's Game of Life. At 
# least, it was, until you notice 
# that something's wrong with the 
# grid of lights you bought: four 
# lights, one in each corner, are 
# stuck on and can't be turned off. 
# The example above will actually 
# run like this: 
# 
# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#
# 
# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####
# 
# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###
# 
# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#
# 
# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#
# 
# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#
# After 5 steps, this example now 
# has 17 lights on. 
# 
# In your grid of 100x100 lights, 
# given your initial configuration, 
# but with the four corners always 
# in the on state, how many lights 
# are on after 100 steps? 
# 
from get_input import get_input
import numpy as np
import os


def get_grid(given):
    grid = []
    for line in given.split('\n'):
        if line != '':
            grid.append([i for i in line])
    return grid


class LightGrid:
    states = {
        '#': 1,
        '.': 0
    }
    def __init__(self, configuration):
        self.grid = get_grid(configuration)
        self.states_history = [np.array([[1 if i == '#' else 0 for i in row] for row in self.grid.copy()]).astype('uint8')]
        
    def _get_adjacents(self, row, column, v2):
        if v2 and (row == 0 or row == len(self.grid) - 1) and (column == 0 or column == len(self.grid[0]) - 1):
            return 3
        if row - 1 >= 0:
            tl = self.grid[row - 1][column - 1] if column - 1 >= 0 else '.'
            t = self.grid[row - 1][column]
            tr = self.grid[row - 1][column + 1] if column + 1 < len(self.grid[0]) else '.'
        else:
            tl, t, tr = '.', '.', '.'
        l = self.grid[row][column - 1] if column - 1 >= 0 else '.'
        r = self.grid[row][column + 1] if column + 1 < len(self.grid[0]) else '.'
        if row + 1 < len(self.grid):
            bl = self.grid[row + 1][column - 1] if column - 1 >= 0 else '.'
            b = self.grid[row + 1][column]
            br = self.grid[row + 1][column + 1] if column + 1 < len(self.grid[0]) else '.'
        else:
            bl, b, br = '.', '.', '.'
        return sum(1 for i in (tl, t, tr, l, r, bl, b, br) if i == '#')
    
    def change_state(self, v2=False):
        copy = [i.copy() for i in self.grid]
        for row_ind, row in enumerate(copy):
            for col_ind, state in enumerate(row):
                adj = self._get_adjacents(row_ind, col_ind, v2)
                if state == '.' and adj == 3:
                    copy[row_ind][col_ind] = '#'
                elif state == '#' and not (adj == 2 or adj == 3):
                    copy[row_ind][col_ind] = '.'
        self.grid = copy
        self.states_history.append(np.array([[1 if i == '#' else 0 for i in row] for row in self.grid.copy()]).astype('uint8'))
    
    def print_grid(self):
        [print('\r' + ''.join([i for i in row])) for row in self.grid]                    


def main():
    given = get_input(18, 2015)
    lights = LightGrid(given)
    
    for i in range(100):
        lights.change_state()
    print(f"Part 1: {sum(sum(1 for i in row if i == '#') for row in lights.grid)}")
    
    lights2 = LightGrid(given)
    for i in range(100):
        lights2.change_state(True)
    print(f"Part 2: {sum(sum(1 for i in row if i == '#') for row in lights2.grid)}")

    
if __name__ == "__main__":
    main()

