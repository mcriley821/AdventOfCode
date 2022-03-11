#!/usr/bin/env python
# Day 20 - Advent of Code 2020 
# --- Day 20: Jurassic Jigsaw ---
# 
# The high-speed train leaves the 
# forest and quickly carries you 
# south. You can even see a desert 
# in the distance! Since you have 
# some spare time, you might as well 
# see if there was anything 
# interesting in the image the 
# Mythical Information Bureau 
# satellite captured. 
# 
# After decoding the satellite 
# messages, you discover that the 
# data actually contains many small 
# images created by the satellite's 
# camera array. The camera array 
# consists of many cameras; rather 
# than produce a single square 
# image, they produce many smaller 
# square image tiles that need to be 
# reassembled back into a single 
# image. 
# 
# Each camera in the camera array 
# returns a single monochrome image 
# tile with a random unique ID 
# number. The tiles (your puzzle 
# input) arrived in a random order. 
# 
# Worse yet, the camera array 
# appears to be malfunctioning: each 
# image tile has been rotated and 
# flipped to a random orientation. 
# Your first task is to reassemble 
# the original image by orienting 
# the tiles so they fit together. 
# 
# To show how the tiles should be 
# reassembled, each tile's image 
# data includes a border that should 
# line up exactly with its adjacent 
# tiles. All tiles have this border, 
# and the border lines up exactly 
# when the tiles are both oriented 
# correctly. Tiles at the edge of 
# the image also have this border, 
# but the outermost edges won't line 
# up with any other tiles. 
# 
# For example, suppose you have the 
# following nine tiles: 
# 
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
# 
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
# 
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
# 
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
# 
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
# 
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
# 
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
# 
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
# 
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
#
# By rotating, flipping, and 
# rearranging them, you can find a 
# square arrangement that causes all 
# adjacent borders to line up: 
# 
# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...
# 
# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####
# 
# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....
#
# For reference, the IDs of the 
# above tiles are: 
# 
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
#
# To check that you've assembled the 
# image correctly, multiply the IDs 
# of the four corner tiles together. 
# If you do this with the assembled 
# tiles from the example above, you 
# get 1951 * 3079 * 2971 * 1171 = 
# 20899048083289. 
# 
# Assemble the tiles into an image. 
# What do you get if you multiply 
# together the IDs of the four 
# corner tiles? 
# 
# --- Part Two ---
# 
# Now, you're ready to check the 
# image for sea monsters. 
# 
# The borders of each tile are not 
# part of the actual image; start by 
# removing them. 
# 
# In the example above, the tiles 
# become: 
# 
# .#.#..#. ##...#.# #..#####
# ###....# .#....#. .#......
# ##.##.## #.#.#..# #####...
# ###.#### #...#.## ###.#..#
# ##.#.... #.##.### #...#.##
# ...##### ###.#... .#####.#
# ....#..# ...##..# .#.###..
# .####... #..#.... .#......
# 
# #..#.##. .#..###. #.##....
# #.####.. #.####.# .#.###..
# ###.#.#. ..#.#### ##.#..##
# #.####.. ..##..## ######.#
# ##..##.# ...#...# .#.#.#..
# ...#..#. .#.#.##. .###.###
# .#.#.... #.##.#.. .###.##.
# ###.#... #..#.##. ######..
# 
# .#.#.### .##.##.# ..#.##..
# .####.## #.#...## #.#..#.#
# ..#.#..# ..#.#.#. ####.###
# #..####. ..#.#.#. ###.###.
# #####..# ####...# ##....##
# #.##..#. .#...#.. ####...#
# .#.###.. ##..##.. ####.##.
# ...###.. .##...#. ..#..###
#
# Remove the gaps to form the actual 
# image: 
# 
# .#.#..#.##...#.##..#####
# ###....#.#....#..#......
# ##.##.###.#.#..######...
# ###.#####...#.#####.#..#
# ##.#....#.##.####...#.##
# ...########.#....#####.#
# ....#..#...##..#.#.###..
# .####...#..#.....#......
# #..#.##..#..###.#.##....
# #.####..#.####.#.#.###..
# ###.#.#...#.######.#..##
# #.####....##..########.#
# ##..##.#...#...#.#.#.#..
# ...#..#..#.#.##..###.###
# .#.#....#.##.#...###.##.
# ###.#...#..#.##.######..
# .#.#.###.##.##.#..#.##..
# .####.###.#...###.#..#.#
# ..#.#..#..#.#.#.####.###
# #..####...#.#.#.###.###.
# #####..#####...###....##
# #.##..#..#...#..####...#
# .#.###..##..##..####.##.
# ...###...##...#...#..###
#
# Now, you're ready to search for 
# sea monsters! Because your image 
# is monochrome, a sea monster will 
# look like this: 
# 
#                   # 
# #    ##    ##    ###
#  #  #  #  #  #  #   
#
# When looking for this pattern in 
# the image, the spaces can be 
# anything; only the # need to 
# match. Also, you might need to 
# rotate or flip your image before 
# it's oriented correctly to find 
# sea monsters. In the above image, 
# after flipping and rotating it to 
# the appropriate orientation, there 
# are two sea monsters (marked with 
# O): 
# 
# .####...#####..#...###..
# #####..#..#.#.####..#.#.
# .#.#...#.###...#.##.O#..
# #.O.##.OO#.#.OO.##.OOO##
# ..#O.#O#.O##O..O.#O##.##
# ...#.#..##.##...#..#..##
# #.##.#..#.#..#..##.#.#..
# .###.##.....#...###.#...
# #.####.#.#....##.#..#.#.
# ##...#..#....#..#...####
# ..#.##...###..#.#####..#
# ....#.##.#.#####....#...
# ..##.##.###.....#.##..#.
# #...#...###..####....##.
# .#.##...#.##.#.#.###...#
# #.###.#..####...##..#...
# #.###...#.##...#.##O###.
# .O##.#OO.###OO##..OOO##.
# ..O#.O..O..O.#O##O##.###
# #.#..##.########..#..##.
# #.#####..#.#...##..#....
# #....##..#.#########..##
# #...#.....#..##...###.##
# #..###....##.#...##.##.#
#
# Determine how rough the waters are 
# in the sea monsters' habitat by 
# counting the number of # that are 
# not part of a sea monster. In the 
# above example, the habitat's water 
# roughness is 273. 
# 
# How many # are not part of a sea 
# monster? 
# 
from get_input import get_input
from itertools import product


class Tile:
    def __init__(self, tile_s):
        self.id = None
        self.tile = []
        self.load_from_string(tile_s)
        self.left_tile = None
        self.right_tile = None
        self.top_tile = None
        self.bottom_tile = None

    def load_from_string(self, string):
        for ind, line in enumerate(string.split('\n')):
            if ind == 0:
                self.id = int(line.replace('Tile ', '').replace(':', ''))
            else:
                self.tile.append(line)
        
    def flip_left_right(self):
        for ind, s in enumerate(self.tile):
            self.tile[ind] = ''.join(reversed(s))
        self.left_tile, self.right_tile = self.right_tile, self.left_tile
        self.flipped = True
        for i in self.adjacent_tiles:
            if not i.flipped:
                i.flip_left_right()
    
    def flip_top_bottom(self):
        self.tile = list(reversed(self.tile))
        self.top_tile, self.bottom_tile = self.bottom_tile, self.top_tile
        self.flipped = True
        for i in self.adjacent_tiles:
            if not i.flipped:
                i.flip_top_bottom()
    
    def rotate_right(self):
        self.tile = [''.join(i[ind] for i in reversed(self.tile)) for ind in range(len(self.tile))]
        self.top_tile, self.right_tile, self.bottom_tile, self.left_tile = self.left_tile, self.top_tile, self.right_tile, self.bottom_tile
        
    def remove_border(self):
        self.tile = [i[1:-1] for i in self.tile[1:-1]]
        
    @property
    def top(self):
        return self.tile[0]
    
    @property
    def flipped_top(self):
        return ''.join(reversed(self.tile[0]))
    
    @property
    def bottom(self):
        return self.tile[-1]
    
    @property
    def flipped_bottom(self):
        return ''.join(reversed(self.tile[-1]))
    
    @property
    def left(self):
        return ''.join(i[0] for i in self.tile)
    
    @property
    def flipped_left(self):
        return ''.join(i[0] for i in reversed(self.tile))
    
    @property
    def right(self):
        return ''.join(i[-1] for i in self.tile)
    
    @property
    def flipped_right(self):
        return ''.join(i[-1] for i in reversed(self.tile))
        
    @property
    def adjacent_tiles(self):
        return [i for i in [self.top_tile, self.right_tile, self.bottom_tile, self.left_tile] if i is not None]

    def __repr__(self):
        return '\n'.join(self.tile)            


def split_tiles(given):
    for i in given.split('\n\n'):
        if i != '':
            yield i


def main():
    given = get_input(20, 2020)
    tiles = {}
    for tile in split_tiles(given):
        t = Tile(tile)
        tiles[t.id] = t

    # need to find corners
    sides = ['top', 'left', 'right', 'bottom', 'flipped_top', 'flipped_left', 'flipped_right', 'flipped_bottom']
    all_sides = []
    for t1 in tiles.values():
        for side in sides:
            all_sides.append(getattr(t1, side))
    
    edges = []
    for side in all_sides:
        if all_sides.count(side) + all_sides.count(''.join(reversed(side))) == 2:
            edges.append(side)
    
    corners = []
    for tile in tiles.values():
        count = 0
        for side in sides[:4]:
            if getattr(tile, side) in edges:
                count += 1
        if count == 2:
            corners.append(tile)    
        
    prod = 1
    for t in corners:
        prod *= t.id    
    print(f'Part 1: {prod}')
    
    # build jigsaw
    puzzle = []
    row = corners[0]
    while row.top not in edges or row.left not in edges:
        row.rotate_right()
    row = [row]
    while len(puzzle) != int(len(tiles) ** 0.5):
        while len(row) != int(len(tiles) ** 0.5):
            t1 = row[-1]
            for t2 in tiles.values():
                if t2 is t1 or any(t2 in row for row in puzzle):
                    continue
                for side in sides:
                    if getattr(t2, side) == t1.right:
                        while t2.left != t1.right:
                            t2.rotate_right()
                            if t2.flipped_left == t1.right:
                                t2.flip_top_bottom()
                                break
                        t1.right_tile = t2
                        t2.left_tile = t1
                        row.append(t2)
                        break
                else:
                    # not on this tile
                    continue
                if t2.right in edges:
                    puzzle.append(row)
                    t1 = row[0]
                    for t2 in tiles.values():
                        if t2 is t1 or any(t2 in row for row in puzzle):
                            continue
                        for side in sides:
                            if getattr(t2, side) == t1.bottom:
                                while t2.top != t1.bottom:
                                    t2.rotate_right()
                                    if t2.flipped_top == t1.bottom:
                                        t2.flip_left_right()
                                        break
                                t1.bottom_tile = t2
                                t2.top_tile = t1
                                row = [t2]
                                break
                        else:
                            continue
                        break
                    else:
                        break
            else:
                break
    
    for row in puzzle:
        for tile in row:
            tile.remove_border()
        
    puzzle_s = ''
    for tile_row in puzzle:
        for i in range(len(tile_row[0].tile)):
            puzzle_s += ''.join(tile.tile[i] for tile in tile_row) + '\n'
        puzzle_s += '\n'
    
    # now have entire puzzle
    # need to search for sea monsters
    sea_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """[1:].split('\n')

    def match_rows(row, matcher, replace=False):
        importants = []
        for i in range(len(matcher)):
            if matcher[i] == '#':
                importants.append(i)
        for ind in range(len(row)):
            if ind + len(matcher) == len(row):
                return (False, -1)
            else:
                # only # matters
                if all(row[ind + i] == '#' for i in importants):
                    if replace:
                        row = list(row)
                        for i in importants:
                            row[ind + i] = '.'
                        row = ''.join(row)
                        return row
                    return (True, ind)
                else:
                    continue                
    
    # assume correct orientation
    puzzle = puzzle_s.split('\n')
    while '' in puzzle:
        puzzle.remove('')
    for i in range(len(puzzle[0]) - len(sea_monster[0])):
        for row_ind, row in enumerate(puzzle):
            if row_ind + 2 == len(puzzle):
                break
            present, index = match_rows(row[i:], sea_monster[0])
            if present:
                present, index2 = match_rows(puzzle[row_ind + 1][i:], sea_monster[1])
                if present and index == index2:
                    present, index3 = match_rows(puzzle[row_ind + 2][i:], sea_monster[2])
                    if present and index == index3:
                        puzzle[row_ind] = puzzle[row_ind].replace(row[i:], match_rows(row[i:], sea_monster[0], True))
                        puzzle[row_ind + 1] = puzzle[row_ind + 1].replace(puzzle[row_ind + 1][i:], match_rows(puzzle[row_ind + 1][i:], sea_monster[1], True))
                        puzzle[row_ind + 2] = puzzle[row_ind + 2].replace(puzzle[row_ind + 2][i:], match_rows(puzzle[row_ind + 2][i:], sea_monster[2], True))
    
    print(f"Part 2: {sum(sum(1 for char in row if char == '#') for row in puzzle)}")


if __name__ == "__main__":
    main()

