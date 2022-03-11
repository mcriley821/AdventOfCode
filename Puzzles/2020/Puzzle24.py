#!/usr/bin/env python
# Day 24 - Advent of Code 2020 
# --- Day 24: Lobby Layout ---
# 
# Your raft makes it to the tropical 
# island; it turns out that the 
# small crab was an excellent 
# navigator. You make your way to 
# the resort. 
# 
# As you enter the lobby, you 
# discover a small problem: the 
# floor is being renovated. You 
# can't even reach the check-in desk 
# until they've finished installing 
# the new tile floor. 
# 
# The tiles are all hexagonal; they 
# need to be arranged in a hex grid 
# with a very specific color 
# pattern. Not in the mood to wait, 
# you offer to help figure out the 
# pattern. 
# 
# The tiles are all white on one 
# side and black on the other. They 
# start with the white side facing 
# up. The lobby is large enough to 
# fit whatever pattern might need to 
# appear there. 
# 
# A member of the renovation crew 
# gives you a list of the tiles that 
# need to be flipped over (your 
# puzzle input). Each line in the 
# list identifies a single tile that 
# needs to be flipped by giving a 
# series of steps starting from a 
# reference tile in the very center 
# of the room. (Every line starts 
# from the same reference tile.) 
# 
# Because the tiles are hexagonal, 
# every tile has six neighbors: 
# east, southeast, southwest, west, 
# northwest, and northeast. These 
# directions are given in your list, 
# respectively, as e, se, sw, w, nw, 
# and ne. A tile is identified by a 
# series of these directions with no 
# delimiters; for example, esenee 
# identifies the tile you land on if 
# you start at the reference tile 
# and then move one tile east, one 
# tile southeast, one tile 
# northeast, and one tile east. 
# 
# Each time a tile is identified, it 
# flips from white to black or from 
# black to white. Tiles might be 
# flipped more than once. For 
# example, a line like esew flips a 
# tile immediately adjacent to the 
# reference tile, and a line like 
# nwwswee flips the reference tile 
# itself. 
# 
# Here is a larger example:
# 
# sesenwnenenewseeswwswswwnenewsewsw
# 
# neeenesenwnwwswnenewnwwsewnenwseswesw 
# seswneswswsenwwnwse
# 
# nwnwneseeswswnenewneswwnewseswneseene 
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# 
# wsweesenenewnwwnwsenewsenwwsesesenwne 
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# 
# eneswnwswnwsenenwnwnwwseeswneewsenese 
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
#
# In the above example, 10 tiles are 
# flipped once (to black), and 5 
# more are flipped twice (to black, 
# then back to white). After all of 
# these instructions have been 
# followed, a total of 10 tiles are 
# black. 
# 
# Go through the renovation crew's 
# list and determine which tiles 
# they need to flip. After all of 
# the instructions have been 
# followed, how many tiles are left 
# with the black side up? 
# 
# --- Part Two ---
# 
# The tile floor in the lobby is 
# meant to be a living art exhibit. 
# Every day, the tiles are all 
# flipped according to the following 
# rules: 
# 
# Any black tile with zero or more 
# than 2 black tiles immediately 
# adjacent to it is flipped to 
# white. 
# Any white tile with exactly 2 
# black tiles immediately adjacent 
# to it is flipped to black. 
# Here, tiles immediately adjacent 
# means the six tiles directly 
# touching the tile in question. 
# 
# The rules are applied 
# simultaneously to every tile; put 
# another way, it is first 
# determined which tiles need to be 
# flipped, then they are all flipped 
# at the same time. 
# 
# In the above example, the number 
# of black tiles that are facing up 
# after the given number of days has 
# passed is as follows: 
# 
# Day 1: 15
# Day 2: 12
# Day 3: 25
# Day 4: 14
# Day 5: 23
# Day 6: 28
# Day 7: 41
# Day 8: 37
# Day 9: 49
# Day 10: 37
# 
# Day 20: 132
# Day 30: 259
# Day 40: 406
# Day 50: 566
# Day 60: 788
# Day 70: 1106
# Day 80: 1373
# Day 90: 1844
# Day 100: 2208
#
# After executing this process a 
# total of 100 times, there would be 
# 2208 black tiles facing up. 
# 
# How many tiles will be black after 
# 100 days? 
# 
from get_input import get_input


class HexGrid:
    def __init__(self, width, height):
        self._grid = [[0 for _ in range(width)] for _ in range(height)]
        self.center = (width // 2, height // 2)
        self.ones = set()
    
    def follow(self, directions):
        pointer = self.center
        for direction in self._get_direction(directions):
            if direction == 'e':
                pointer = (pointer[0], pointer[1] + 2)
            elif direction == 'w':
                pointer = (pointer[0], pointer[1] - 2)
            elif direction == 'ne':
                pointer = (pointer[0] - 1, pointer[1] + 1)
            elif direction == 'nw':
                pointer = (pointer[0] - 1, pointer[1] - 1)
            elif direction == 'se':
                pointer = (pointer[0] + 1, pointer[1] + 1)
            elif direction == 'sw':
                pointer = (pointer[0] + 1, pointer[1] - 1)
        self[pointer] = 1 if self[pointer] == 0 else 0
        if self[pointer] == 1:
            self.ones.add(pointer)
        else:
            self.ones.remove(pointer)
            
    def _get_direction(self, directions):
        directions = list(directions)
        while directions:
            next_direction = directions.pop(0)
            if next_direction == 's' or next_direction == 'n':
                next_direction += directions.pop(0)
            yield next_direction
            
    def next_day(self):
        flip = set()
        for pointer in self.ones:
            total = sum(self[i] for i in self._adjacents(*pointer))
            if total == 0 or total > 2:
                flip.add(pointer)
            for adj in self._adjacents(*pointer):
                if self[adj] == 0 and sum(self[i] for i in self._adjacents(*adj)) == 2:
                    flip.add(adj)                
        
        for pointer in flip:
            self[pointer] = 1 if self[pointer] == 0 else 0
            if self[pointer] == 1:
                self.ones.add(pointer)
            else:
                self.ones.remove(pointer)

    @classmethod
    def _adjacents(self, row, ind):
        w = (row, ind - 2)
        nw = (row - 1, ind - 1)
        ne = (row - 1, ind + 1)
        e = (row, ind + 2)
        se = (row + 1, ind + 1)
        sw = (row + 1, ind - 1)
        return [w, nw, ne, e, se, sw]
    
    def __getitem__(self, index):
        if type(index) is tuple:
            return self._grid[index[0]][index[1]]
        else:
            return self._grid[index]
    
    def __setitem__(self, index, value):
        if type(index) is tuple:
            self._grid[index[0]][index[1]] = value
        else:
            self._grid[index] = value
    
    @property
    def black_tile_count(self):
        return len(self.ones)


def main():
    given = get_input(24, 2020)
    grid = HexGrid(2000, 2000)
    for dirs in given.split('\n'):
        if dirs != '':
            grid.follow(dirs)
    print(f"Part 1: {grid.black_tile_count}")
    
    for day in range(1, 101):
        grid.next_day()
    
    print(f"Part 2: {grid.black_tile_count}")


if __name__ == "__main__":
    main()

