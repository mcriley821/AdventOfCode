#!/usr/bin/env python
# Day 11 - Advent of Code 2020 
# --- Day 11: Seating System ---
# 
# Your plane lands with plenty of 
# time to spare. The final leg of 
# your journey is a ferry that goes 
# directly to the tropical island 
# where you can finally start your 
# vacation. As you reach the waiting 
# area to board the ferry, you 
# realize you're so early, nobody 
# else has even arrived yet! 
# 
# By modeling the process people use 
# to choose (or abandon) their seat 
# in the waiting area, you're pretty 
# sure you can predict the best 
# place to sit. You make a quick map 
# of the seat layout (your puzzle 
# input). 
# 
# The seat layout fits neatly on a 
# grid. Each position is either 
# floor (.), an empty seat (L), or 
# an occupied seat (#). For example, 
# the initial seat layout might look 
# like this: 
# 
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# Now, you just need to model the 
# people who will be arriving 
# shortly. Fortunately, people are 
# entirely predictable and always 
# follow a simple set of rules. All 
# decisions are based on the number 
# of occupied seats adjacent to a 
# given seat (one of the eight 
# positions immediately up, down, 
# left, right, or diagonal from the 
# seat). The following rules are 
# applied to every seat 
# simultaneously: 
# 
# If a seat is empty (L) and there 
# are no occupied seats adjacent to 
# it, the seat becomes occupied. 
# If a seat is occupied (#) and four 
# or more seats adjacent to it are 
# also occupied, the seat becomes 
# empty. 
# Otherwise, the seat's state does 
# not change. 
# Floor (.) never changes; seats 
# don't move, and nobody sits on the 
# floor. 
# 
# After one round of these rules, 
# every seat in the example layout 
# becomes occupied: 
# 
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# After a second round, the seats 
# with four or more occupied 
# adjacent seats become empty again: 
# 
# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three 
# more rounds: 
# 
# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##
#
# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##
#
# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##
#
# At this point, something 
# interesting happens: the chaos 
# stabilizes and further 
# applications of these rules cause 
# no seats to change state! Once 
# people stop moving around, you 
# count 37 occupied seats. 
# 
# Simulate your seating area by 
# applying the seating rules 
# repeatedly until no seats change 
# state. How many seats end up 
# occupied? 
# 
# --- Part Two ---
# 
# As soon as people start to arrive, 
# you realize your mistake. People 
# don't just care about adjacent 
# seats - they care about the first 
# seat they can see in each of those 
# eight directions! 
# 
# Now, instead of considering just 
# the eight immediately adjacent 
# seats, consider the first seat in 
# each of those eight directions. 
# For example, the empty seat below 
# would see eight occupied seats: 
# 
# .......#.
# ...#.....
# .#.......
# .........
# ..#L....#
# ....#....
# .........
# #........
# ...#.....
# The leftmost empty seat below 
# would only see one empty seat, but 
# cannot see any of the occupied 
# ones: 
# 
# .............
# .L.L.#.#.#.#.
# .............
# The empty seat below would see no 
# occupied seats: 
# 
# .##.##.
# #.#.#.#
# ##...##
# ...L...
# ##...##
# #.#.#.#
# .##.##.
# Also, people seem to be more 
# tolerant than you expected: it now 
# takes five or more visible 
# occupied seats for an occupied 
# seat to become empty (rather than 
# four or more from the previous 
# rules). The other rules still 
# apply: empty seats that see no 
# occupied seats become occupied, 
# seats matching no rule don't 
# change, and floor never changes. 
# 
# Given the same starting layout as 
# above, these new rules cause the 
# seating area to shift around as 
# follows: 
# 
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
#
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
#
# #.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#
#
# #.L#.##.L#
# #L#####.LL
# L.#.#..#..
# ##L#.##.##
# #.##.#L.##
# #.#####.#L
# ..#.#.....
# LLL####LL#
# #.L#####.L
# #.L####.L#
#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##LL.LL.L#
# L.LL.LL.L#
# #.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLL#.L
# #.L#LL#.L#
#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.#L.L#
# #.L####.LL
# ..#.#.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.LL.L#
# #.LLLL#.LL
# ..#.L.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
#
# Again, at this point, people stop 
# shifting around and the seating 
# area reaches equilibrium. Once 
# this occurs, you count 26 occupied 
# seats. 
# 
# Given the new visibility method 
# and the rule change for occupied 
# seats becoming empty, once 
# equilibrium is reached, how many 
# seats end up occupied? 
# 
from get_input import get_input


def get_adjacents(row_ind, ind, num_rows, len_rows):
    tl, t, tr = None, None, None
    l, r = None, None
    bl, b, br = None, None, None
    if row_ind - 1 >= 0:
        tl = (row_ind - 1, ind - 1) if ind - 1 >= 0 else None
        t = (row_ind - 1, ind)
        tr = (row_ind - 1, ind + 1) if ind + 1 < len_rows else None
    l = (row_ind, ind - 1) if ind - 1 >= 0 else None
    r = (row_ind, ind + 1) if ind + 1 < len_rows else None
    if row_ind + 1 < num_rows:
        bl = (row_ind + 1, ind - 1) if ind - 1 >= 0 else None
        b = (row_ind + 1, ind)
        br = (row_ind + 1, ind + 1) if ind + 1 < len_rows else None
    return (tl, t, tr, l, r, bl, b, br)
    

def queens_sight(row_ind, ind, num_rows, len_rows):
    tl, t, tr = [], [], []
    l, r = [], []
    bl, b, br = [], [], []
    row_ind_ctr = 1
    diag_ctr = 1
    while row_ind - row_ind_ctr >= 0:
        if ind - diag_ctr >= 0:
            tl.append((row_ind - row_ind_ctr, ind - diag_ctr))
        t.append((row_ind - row_ind_ctr, ind))
        if ind + diag_ctr < len_rows:
            tr.append((row_ind - row_ind_ctr, ind + diag_ctr))
        row_ind_ctr += 1
        diag_ctr += 1
    ind_ctr = 1
    while ind - ind_ctr >= 0:
        l.append((row_ind, ind - ind_ctr))
        ind_ctr += 1
    ind_ctr = 1
    while ind + ind_ctr < len_rows:
        r.append((row_ind, ind + ind_ctr))
        ind_ctr += 1
    row_ind_ctr = 1
    diag_ctr = 1
    while row_ind + row_ind_ctr < num_rows:
        if ind - diag_ctr >= 0:
            bl.append((row_ind + row_ind_ctr, ind - diag_ctr))
        b.append((row_ind + row_ind_ctr, ind))
        if ind + diag_ctr < len_rows:
            br.append((row_ind + row_ind_ctr, ind + diag_ctr))
        row_ind_ctr += 1
        diag_ctr += 1
    return ((tl, t, tr, l, r, bl, b, br))


def change_state(grid, leave=False):
    copy = [i.copy() for i in grid.copy()]
    for row_ind, row in enumerate(copy):
        for ind, seat in enumerate(row):
            # occupy seat 
            if seat == 'L' and not leave:    
                if all(copy[i[0]][i[1]] != '#' for i in get_adjacents(row_ind, ind, len(copy), len(row)) if i is not None):
                    grid[row_ind][ind] = '#'
            # leave seat
            elif seat == '#' and leave:
                if sum(1 for i in get_adjacents(row_ind, ind, len(copy), len(row)) if i is not None and copy[i[0]][i[1]] == '#') >= 4:
                    grid[row_ind][ind] = 'L'


def change_state_queen(grid, leave=False):
    copy = [i.copy() for i in grid.copy()]
    for row_ind, row in enumerate(copy):
        for ind, seat in enumerate(row):
            if seat == 'L' and not leave:
                count = 0
                for sightline in queens_sight(row_ind, ind, len(copy), len(row)):
                    for seen in sightline:
                        if copy[seen[0]][seen[1]] == '.':
                            continue
                        elif copy[seen[0]][seen[1]] == '#':
                            count += 1
                            break
                        else:
                            break
                if count == 0:
                    grid[row_ind][ind] = '#'
            elif seat == '#' and leave:
                count = 0
                for sightline in queens_sight(row_ind, ind, len(copy), len(row)):
                    for seen in sightline:
                        if copy[seen[0]][seen[1]] == '#':
                            count += 1
                            break # goto next sightline
                        elif copy[seen[0]][seen[1]] == 'L':
                            break
                        else:
                            continue
                if count >= 5:
                    grid[row_ind][ind] = 'L'
                    

def get_occupied(grid):
    return sum(sum(1 for i in row if i == '#') for row in grid)
    

def main():
    given = get_input(11, 2020)
    grid = [[j for j in i] for i in given.split('\n') if i != '']
    grid2 = [i.copy() for i in grid.copy()]
    
    last_occupied = 0
    change_state(grid)
    change_state(grid, True)
    while last_occupied != get_occupied(grid):
        last_occupied = get_occupied(grid)
        change_state(grid)
        change_state(grid, True)
    
    print('Part 1:', last_occupied)
    
    last_occupied = 0
    change_state_queen(grid2)
    change_state_queen(grid2, True)
    while last_occupied != get_occupied(grid2):
        last_occupied = get_occupied(grid2)
        change_state_queen(grid2)
        change_state_queen(grid2, True)
    
    print('Part 2:', last_occupied)
    

if __name__ == "__main__":
    main()

