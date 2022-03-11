#!/usr/bin/env python
# Day 6 - Advent of Code 2015
# --- Day 6: Probably a Fire Hazard 
# --- 
# 
# Because your neighbors keep 
# defeating you in the holiday house 
# decorating contest year after 
# year, you've decided to deploy one 
# million lights in a 1000x1000 
# grid. 
# 
# Furthermore, because you've been 
# especially nice this year, Santa 
# has mailed you instructions on how 
# to display the ideal lighting 
# configuration. 
# 
# Lights in your grid are numbered 
# from 0 to 999 in each direction; 
# the lights at each corner are at 
# 0,0, 0,999, 999,999, and 999,0. 
# The instructions include whether 
# to turn on, turn off, or toggle 
# various inclusive ranges given as 
# coordinate pairs. Each coordinate 
# pair represents opposite corners 
# of a rectangle, inclusive; a 
# coordinate pair like 0,0 through 
# 2,2 therefore refers to 9 lights 
# in a 3x3 square. The lights all 
# start turned off. 
# 
# To defeat your neighbors this 
# year, all you have to do is set up 
# your lights by doing the 
# instructions Santa sent you in 
# order. 
# 
# For example:
# 
# turn on 0,0 through 999,999 would 
# turn on (or leave on) every light. 
# toggle 0,0 through 999,0 would 
# toggle the first line of 1000 
# lights, turning off the ones that 
# were on, and turning on the ones 
# that were off. 
# turn off 499,499 through 500,500 
# would turn off (or leave off) the 
# middle four lights. 
# After following the instructions, 
# how many lights are lit? 
# 
# --- Part Two ---
# 
# You just finish implementing your 
# winning light pattern when you 
# realize you mistranslated Santa's 
# message from Ancient Nordic 
# Elvish. 
# 
# The light grid you bought actually 
# has individual brightness 
# controls; each light can have a 
# brightness of zero or more. The 
# lights all start at zero. 
# 
# The phrase turn on actually means 
# that you should increase the 
# brightness of those lights by 1. 
# 
# The phrase turn off actually means 
# that you should decrease the 
# brightness of those lights by 1, 
# to a minimum of zero. 
# 
# The phrase toggle actually means 
# that you should increase the 
# brightness of those lights by 2. 
# 
# What is the total brightness of 
# all lights combined after 
# following Santa's instructions? 
# 
# For example:
# 
# turn on 0,0 through 0,0 would 
# increase the total brightness by 
# 1. 
# toggle 0,0 through 999,999 would 
# increase the total brightness by 
# 2000000. 

from get_input import get_input
from PIL import Image


def hex_to_rgb(num):
    r = num >> 16
    g = (num >> 8) & 0xff
    b = num & 0xff
    return (r, g, b)


def rgb_to_hex(tup):
    num = tup[0]
    num = (num << 8) + tup[1]
    num = (num << 8) + tup[2]
    return num


class LightGrid:
    def __init__(self, rows, columns, default=0, pixel_mode='binary'):
        self._grid = []
        for _ in range(rows):
            self._grid.append([0] * columns)
        self.rows = rows
        self.columns = columns
        self._pixel_mode = pixel_mode
    
    @property
    def pixel_mode(self):
        return self._pixel_mode
    
    @pixel_mode.setter
    def pixel_mode(self, value):
        if value in ['binary', 'rgb', 'hex']:
            old = self._pixel_mode
            self._pixel_mode = value
            for ind, row in enumerate(self._grid):
                for col_ind, color in enumerate(row):
                    self._grid[ind][col_ind] = self._change_pixel_mode(old, value, color)
    
    def _change_pixel_mode(self, old, new, color):
        if old == 'binary' and new == 'hex':
            return 0xffffff if color == 1 else 0
        elif old == 'binary' and new == 'rgb':
            return (255, 255, 255) if color == 1 else (0,0,0)
        elif old == 'rgb' and new == 'binary':
            return 0 if color == (0,0,0) else 1
        elif old == 'rgb' and new == 'hex':
            return rgb_to_hex(color)
        elif old == 'hex' and new == 'binary':
            return 0 if color == 0 else 1
        elif old == 'hex' and new == 'rgb':
            return hex_to_rgb(color)
        
    def change_lights(self, rectangle, value, toggle=False):
        if not toggle:
            self._check_pixel(value)
        top_left = rectangle[0]
        bottom_right = rectangle[1]
        for row in range(top_left[1], bottom_right[1] + 1):
            for col in range(top_left[0], bottom_right[0] + 1):
                if not toggle:
                    self._grid[row][col] = self._get_default_pixel(value)
                else:
                    self._grid[row][col] = self._get_default_pixel(0) if self._grid[row][col] != self._get_default_pixel(0) else self._get_default_pixel(value)
    
    def dim_lights(self, rectangle, value):
        tl = rectangle[0]
        br = rectangle[1]
        for row in range(tl[1], br[1] + 1):
            for col in range(tl[0], br[0] + 1):
                self._grid[row][col] += value
                if self._grid[row][col] < 0:
                    self._grid[row][col] = 0
    
    def _get_default_pixel(self, x):
        if self._pixel_mode == 'binary':
            return 1 if x != 0 else 0
        elif self._pixel_mode == 'rgb':
            return x if x != 0 else (0, 0, 0)
        elif self._pixel_mode == 'hex':
            return x if x != 0 else 0

    def _check_pixel(self, value):
        if self._pixel_mode == 'binary':
            if value != 0 and value != 1:
                raise TypeError('Pixel value does not match mode...')    
        elif self._pixel_mode == 'rgb':
            if type(value) != tuple or len(value) != 3 or type(value[0]) != int or tupe(value[1]) != int or type(value[2]) != int:
                raise TypeError('Pixel value does not match mode...')
        elif self._pixel_mode == 'hex':
            if type(value) != int or value < 0 or value > 0xffffff:
                raise TypeError('Pixel value does not match mode...')

    def __str__(self):
        string = ''
        for row in self._grid:
            string += str(row) + '\n'
        return string
        
    def __repr__(self):
        return str(self)    

    def __getitem__(self, ind):
        return self._grid[ind]
        
    def to_image(self):
        if self._pixel_mode == 'binary':
            mode = '1'
        else:
            mode = 'RGB'
        img = Image.new(mode, (self.columns, self.rows))
        for r_ind, r in enumerate(self._grid):
            for c_ind, c in enumerate(r):
                if self._pixel_mode == 'hex':
                    img.putpixel((c_ind, r_ind), hex_to_rgb(c))
                else:
                    img.putpixel((c_ind, r_ind), c)
        return img
    
    def count_on_lights(self):
        total = 0
        for row in self._grid:
            total += sum([1 for i in row if i != self._get_default_pixel(0)])
        return total
        
    def count_lights(self):
        total = 0
        for row in self._grid:
            total += sum([i for i in row])
        return total
    
            
def parse_instruction(line):
    if 'toggle' in line:
        do = 'toggle'
        line = line.replace('toggle ', '')
    elif 'on' in line:
        do = 'on'
        line = line.replace('turn on ', '')
    elif 'off' in line:
        do = 'off'
        line = line.replace('turn off ', '')
    tl, br = line.split(' through ')
    tl = tl.split(',')
    tl = (int(tl[0]), int(tl[1]))
    br = br.split(',')
    br = (int(br[0]), int(br[1]))
    return ((tl, br), do)
    
    
def main():
    lg = LightGrid(1000, 1000)
    instructions = get_input(6, 2015)
    for instruction in instructions.split('\n'):
        if instruction != '':
            rect, do = parse_instruction(instruction)
            if do == 'on':
                lg.change_lights(rect, 1)
            elif do == 'off':
                lg.change_lights(rect, 0)
            elif do == 'toggle':
                lg.change_lights(rect, 1, True)
    print('Part 1:', lg.count_on_lights())
    print('Working...')
    new_lg = LightGrid(1000, 1000)
    for instruction in instructions.split('\n'):
        if instruction != '':
            rect, do = parse_instruction(instruction)
            if do == 'on':
                new_lg.dim_lights(rect, 1)
            elif do == 'off':
                new_lg.dim_lights(rect, -1)
            elif do == 'toggle':
                new_lg.dim_lights(rect, 2)
    print('Part 2:', new_lg.count_lights())
    
if __name__ == "__main__":
    main()

