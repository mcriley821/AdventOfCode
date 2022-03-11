#!/usr/bin/env python
# Day 17 - Advent of Code 2020 
# --- Day 17: Conway Cubes ---
# 
# As your flight slowly drifts 
# through the sky, the Elves at the 
# Mythical Information Bureau at the 
# North Pole contact you. They'd 
# like some help debugging a 
# malfunctioning experimental energy 
# source aboard one of their 
# super-secret imaging satellites. 
# 
# The experimental energy source is 
# based on cutting-edge technology: 
# a set of Conway Cubes contained in 
# a pocket dimension! When you hear 
# it's having problems, you can't 
# help but agree to take a look. 
# 
# The pocket dimension contains an 
# infinite 3-dimensional grid. At 
# every integer 3-dimensional 
# coordinate (x,y,z), there exists a 
# single cube which is either active 
# or inactive. 
# 
# In the initial state of the pocket 
# dimension, almost all cubes start 
# inactive. The only exception to 
# this is a small flat region of 
# cubes (your puzzle input); the 
# cubes in this region start in the 
# specified active (#) or inactive 
# (.) state. 
# 
# The energy source then proceeds to 
# boot up by executing six cycles. 
# 
# Each cube only ever considers its 
# neighbors: any of the 26 other 
# cubes where any of their 
# coordinates differ by at most 1. 
# For example, given the cube at 
# x=1,y=2,z=3, its neighbors include 
# the cube at x=2,y=2,z=2, the cube 
# at x=0,y=2,z=3, and so on. 
# 
# During a cycle, all cubes 
# simultaneously change their state 
# according to the following rules: 
# 
# If a cube is active and exactly 2 
# or 3 of its neighbors are also 
# active, the cube remains active. 
# Otherwise, the cube becomes 
# inactive. 
# If a cube is inactive but exactly 
# 3 of its neighbors are active, the 
# cube becomes active. Otherwise, 
# the cube remains inactive. 
# The engineers responsible for this 
# experimental energy source would 
# like you to simulate the pocket 
# dimension and determine what the 
# configuration of cubes should be 
# at the end of the six-cycle boot 
# process. 
# 
# For example, consider the 
# following initial state: 
# 
# .#.
# ..#
# ###
# Even though the pocket dimension 
# is 3-dimensional, this initial 
# state represents a small 
# 2-dimensional slice of it. (In 
# particular, this initial state 
# defines a 3x3x1 region of the 
# 3-dimensional space.) 
# 
# Simulating a few cycles from this 
# initial state produces the 
# following configurations, where 
# the result of each cycle is shown 
# layer-by-layer at each given z 
# coordinate (and the frame of view 
# follows the active cells in each 
# cycle): 
# 
# Before any cycles:
# 
# z=0
# .#.
# ..#
# ###
# 
# 
# After 1 cycle:
# 
# z=-1
# #..
# ..#
# .#.
# 
# z=0
# #.#
# .##
# .#.
# 
# z=1
# #..
# ..#
# .#.
# 
# 
# After 2 cycles:
# 
# z=-2
# .....
# .....
# ..#..
# .....
# .....
# 
# z=-1
# ..#..
# .#..#
# ....#
# .#...
# .....
# 
# z=0
# ##...
# ##...
# #....
# ....#
# .###.
# 
# z=1
# ..#..
# .#..#
# ....#
# .#...
# .....
# 
# z=2
# .....
# .....
# ..#..
# .....
# .....
# 
# 
# After 3 cycles:
# 
# z=-2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
# 
# z=-1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
# 
# z=0
# ...#...
# .......
# #......
# .......
# .....##
# .##.#..
# ...#...
# 
# z=1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
# 
# z=2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
# After the full six-cycle boot 
# process completes, 112 cubes are 
# left in the active state. 
# 
# Starting with your given initial 
# configuration, simulate six 
# cycles. How many cubes are left in 
# the active state after the sixth 
# cycle? 
# 
# --- Part Two ---
# 
# For some reason, your simulated 
# results don't match what the 
# experimental energy source 
# engineers expected. Apparently, 
# the pocket dimension actually has 
# four spatial dimensions, not 
# three. 
# 
# The pocket dimension contains an 
# infinite 4-dimensional grid. At 
# every integer 4-dimensional 
# coordinate (x,y,z,w), there exists 
# a single cube (really, a 
# hypercube) which is still either 
# active or inactive. 
# 
# Each cube only ever considers its 
# neighbors: any of the 80 other 
# cubes where any of their 
# coordinates differ by at most 1. 
# For example, given the cube at 
# x=1,y=2,z=3,w=4, its neighbors 
# include the cube at 
# x=2,y=2,z=3,w=3, the cube at 
# x=0,y=2,z=3,w=4, and so on. 
# 
# The initial state of the pocket 
# dimension still consists of a 
# small flat region of cubes. 
# Furthermore, the same rules for 
# cycle updating still apply: during 
# each cycle, consider the number of 
# active neighbors of each cube. 
# 
# For example, consider the same 
# initial state as in the example 
# above. Even though the pocket 
# dimension is 4-dimensional, this 
# initial state represents a small 
# 2-dimensional slice of it. (In 
# particular, this initial state 
# defines a 3x3x1x1 region of the 
# 4-dimensional space.) 
# 
# Simulating a few cycles from this 
# initial state produces the 
# following configurations, where 
# the result of each cycle is shown 
# layer-by-layer at each given z and 
# w coordinate: 
# 
# Before any cycles:
# 
# z=0, w=0
# .#.
# ..#
# ###
# 
# 
# After 1 cycle:
# 
# z=-1, w=-1
# #..
# ..#
# .#.
# 
# z=0, w=-1
# #..
# ..#
# .#.
# 
# z=1, w=-1
# #..
# ..#
# .#.
# 
# z=-1, w=0
# #..
# ..#
# .#.
# 
# z=0, w=0
# #.#
# .##
# .#.
# 
# z=1, w=0
# #..
# ..#
# .#.
# 
# z=-1, w=1
# #..
# ..#
# .#.
# 
# z=0, w=1
# #..
# ..#
# .#.
# 
# z=1, w=1
# #..
# ..#
# .#.
# 
# 
# After 2 cycles:
# 
# z=-2, w=-2
# .....
# .....
# ..#..
# .....
# .....
# 
# z=-1, w=-2
# .....
# .....
# .....
# .....
# .....
# 
# z=0, w=-2
# ###..
# ##.##
# #...#
# .#..#
# .###.
# 
# z=1, w=-2
# .....
# .....
# .....
# .....
# .....
# 
# z=2, w=-2
# .....
# .....
# ..#..
# .....
# .....
# 
# z=-2, w=-1
# .....
# .....
# .....
# .....
# .....
# 
# z=-1, w=-1
# .....
# .....
# .....
# .....
# .....
# 
# z=0, w=-1
# .....
# .....
# .....
# .....
# .....
# 
# z=1, w=-1
# .....
# .....
# .....
# .....
# .....
# 
# z=2, w=-1
# .....
# .....
# .....
# .....
# .....
# 
# z=-2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
# 
# z=-1, w=0
# .....
# .....
# .....
# .....
# .....
# 
# z=0, w=0
# .....
# .....
# .....
# .....
# .....
# 
# z=1, w=0
# .....
# .....
# .....
# .....
# .....
# 
# z=2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
# 
# z=-2, w=1
# .....
# .....
# .....
# .....
# .....
# 
# z=-1, w=1
# .....
# .....
# .....
# .....
# .....
# 
# z=0, w=1
# .....
# .....
# .....
# .....
# .....
# 
# z=1, w=1
# .....
# .....
# .....
# .....
# .....
# 
# z=2, w=1
# .....
# .....
# .....
# .....
# .....
# 
# z=-2, w=2
# .....
# .....
# ..#..
# .....
# .....
# 
# z=-1, w=2
# .....
# .....
# .....
# .....
# .....
# 
# z=0, w=2
# ###..
# ##.##
# #...#
# .#..#
# .###.
# 
# z=1, w=2
# .....
# .....
# .....
# .....
# .....
# 
# z=2, w=2
# .....
# .....
# ..#..
# .....
# .....
# After the full six-cycle boot 
# process completes, 848 cubes are 
# left in the active state. 
# 
# Starting with your given initial 
# configuration, simulate six cycles 
# in a 4-dimensional space. How many 
# cubes are left in the active state 
# after the sixth cycle? 
# 
from get_input import get_input
from collections import deque
from itertools import product
from copy import deepcopy


class Space4D:
    def __init__(self, space_slice):
        self.width = len(space_slice[0])
        self.height = len(space_slice)
        self.depth = 1
        self.w = 1
        self.space = deque([deque([deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]) for _ in range(self.depth)]) for _ in range(self.w)])
        for ind, row in enumerate(space_slice):
            if row != '':
                self.space[0][0][ind] = deque([1 if i == '#' else 0 for i in row])

    def change_state(self):
        self.add_layer()
        copy = deepcopy(self.space)
        for w in range(self.w):
            cube = copy[w]
            for z in range(self.depth):
                layer = cube[z]
                for y in range(self.height):
                    row = layer[y]
                    for x in range(self.width):
                        state = row[x]
                        on_state_count = 0
                        for neighbor in self.get_neighbors((w, z, y, x)):
                            w_, z_, y_, x_ = neighbor
                            try:
                                neighbor_state = copy[w_][z_][y_][x_]
                            except:
                                continue
                            if neighbor_state == 1:
                                on_state_count += 1
                        if state == 0 and on_state_count == 3:
                            self.space[w][z][y][x] = 1
                        elif state == 1 and not (on_state_count == 2 or on_state_count == 3):
                            self.space[w][z][y][x] = 0                        
    
    def get_neighbors(self, coord):
        out = list(product(*(range(i - 1, i + 2) for i in coord)))
        out.remove(coord)
        return out
        
    def add_layer(self):
        self.width += 2
        self.height += 2
        self.depth += 2
        self.w += 2
        for d3 in self.space:
            for layer in d3:
                for row in layer:
                    row.appendleft(0)
                    row.append(0)
                layer.appendleft(deque([0 for _ in range(self.width)]))
                layer.append(deque([0 for _ in range(self.width)]))
            d3.appendleft(deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]))
            d3.append(deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]))
        self.space.appendleft(deque([deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]) for _ in range(self.depth)]))
        self.space.append(deque([deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]) for _ in range(self.depth)]))
        
    def __repr__(self):
        string = ''
        for i, d3 in enumerate(self.space):
            string += f'{i}\t'
            for layer in d3:
                for row in layer:
                    string += f'{row}\n\t'
                string += '\n\t'
            string += '\n'
        return string


class Space3D:
    def __init__(self, space_slice):
        self.width = len(space_slice[0])
        self.height = len(space_slice)
        self.depth = 1
        self.space = deque([deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]) for _ in range(self.depth)])
        for ind, row in enumerate(space_slice):
            if row != '':
                self.space[0][ind] = deque([1 if i == '#' else 0 for i in row])

    def change_state(self):
        self.add_layer()
        copy = deepcopy(self.space)
        for z in range(self.depth):
            layer = copy[z]
            for y in range(self.height):
                row = layer[y]
                for x in range(self.width):
                    state = row[x]
                    on_state_count = 0
                    for neighbor in self.get_neighbors((z, y, x)):
                        z_, y_, x_ = neighbor
                        try:
                            neighbor_state = copy[z_][y_][x_]
                        except:
                            continue
                        if neighbor_state == 1:
                            on_state_count += 1
                    if state == 0 and on_state_count == 3:
                        self.space[z][y][x] = 1
                    elif state == 1 and not (on_state_count == 2 or on_state_count == 3):
                        self.space[z][y][x] = 0                        
    
    def get_neighbors(self, coord):
        out = list(product(*(range(i - 1, i + 2) for i in coord)))
        out.remove(coord)
        return out
        
    def add_layer(self):
        self.width += 2
        self.height += 2
        self.depth += 2
        for layer in self.space:
            for row in layer:
                row.appendleft(0)
                row.append(0)
            layer.appendleft(deque([0 for _ in range(self.width)]))
            layer.append(deque([0 for _ in range(self.width)]))
        self.space.appendleft(deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]))
        self.space.append(deque([deque([0 for _ in range(self.width)]) for _ in range(self.height)]))        
        
    def __repr__(self):
        string = ''
        for layer in self.space:
            for row in layer:
                string += f'{row}\n'
            string += '\n'
        return string
        
        
def main():
    given = get_input(17, 2020)
    s3 = Space3D(given.split('\n'))
    for _ in range(6):
        s3.change_state()
    print(f'Part 1: {sum(sum(sum(i for i in row) for row in layer) for layer in s3.space)}')
    
    s4 = Space4D(given.split('\n'))
    for _ in range(6):
        s4.change_state()
    print(f'Part 2: {sum(sum(sum(sum(i for i in row) for row in layer) for layer in cube) for cube in s4.space)}')


if __name__ == "__main__":
    main()

