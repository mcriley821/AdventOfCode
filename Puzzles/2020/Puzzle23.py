#!/usr/bin/env python
# Day 23 - Advent of Code 2020 
# --- Day 23: Crab Cups ---
# 
# The small crab challenges you to a 
# game! The crab is going to mix up 
# some cups, and you have to predict 
# where they'll end up. 
# 
# The cups will be arranged in a 
# circle and labeled clockwise (your 
# puzzle input). For example, if 
# your labeling were 32415, there 
# would be five cups in the circle; 
# going clockwise around the circle 
# from the first cup, the cups would 
# be labeled 3, 2, 4, 1, 5, and then 
# back to 3 again. 
# 
# Before the crab starts, it will 
# designate the first cup in your 
# list as the current cup. The crab 
# is then going to do 100 moves. 
# 
# Each move, the crab does the 
# following actions: 
# 
# The crab picks up the three cups 
# that are immediately clockwise of 
# the current cup. They are removed 
# from the circle; cup spacing is 
# adjusted as necessary to maintain 
# the circle. 
# The crab selects a destination 
# cup: the cup with a label equal to 
# the current cup's label minus one. 
# If this would select one of the 
# cups that was just picked up, the 
# crab will keep subtracting one 
# until it finds a cup that wasn't 
# just picked up. If at any point in 
# this process the value goes below 
# the lowest value on any cup's 
# label, it wraps around to the 
# highest value on any cup's label 
# instead. 
# The crab places the cups it just 
# picked up so that they are 
# immediately clockwise of the 
# destination cup. They keep the 
# same order as when they were 
# picked up. 
# The crab selects a new current 
# cup: the cup which is immediately 
# clockwise of the current cup. 
# For example, suppose your cup 
# labeling were 389125467. If the 
# crab were to do merely 10 moves, 
# the following changes would occur: 
# 
# -- move 1 --
# cups: (3) 8  9  1  2  5  4  6  7 
# pick up: 8, 9, 1
# destination: 2
# 
# -- move 2 --
# cups:  3 (2) 8  9  1  5  4  6  7 
# pick up: 8, 9, 1
# destination: 7
# 
# -- move 3 --
# cups:  3  2 (5) 4  6  7  8  9  1 
# pick up: 4, 6, 7
# destination: 3
# 
# -- move 4 --
# cups:  7  2  5 (8) 9  1  3  4  6 
# pick up: 9, 1, 3
# destination: 7
# 
# -- move 5 --
# cups:  3  2  5  8 (4) 6  7  9  1 
# pick up: 6, 7, 9
# destination: 3
# 
# -- move 6 --
# cups:  9  2  5  8  4 (1) 3  6  7 
# pick up: 3, 6, 7
# destination: 9
# 
# -- move 7 --
# cups:  7  2  5  8  4  1 (9) 3  6 
# pick up: 3, 6, 7
# destination: 8
# 
# -- move 8 --
# cups:  8  3  6  7  4  1  9 (2) 5 
# pick up: 5, 8, 3
# destination: 1
# 
# -- move 9 --
# cups:  7  4  1  5  8  3  9  2 (6)
# pick up: 7, 4, 1
# destination: 5
# 
# -- move 10 --
# cups: (5) 7  4  1  8  3  9  2  6 
# pick up: 7, 4, 1
# destination: 3
# 
# -- final --
# cups:  5 (8) 3  7  4  1  9  2  6 
#
# In the above example, the cups' 
# values are the labels as they 
# appear moving clockwise around the 
# circle; the current cup is marked 
# with ( ). 
# 
# After the crab is done, what order 
# will the cups be in? Starting 
# after the cup labeled 1, collect 
# the other cups' labels clockwise 
# into a single string with no extra 
# characters; each number except 1 
# should appear exactly once. In the 
# above example, after 10 moves, the 
# cups clockwise from 1 are labeled 
# 9, 2, 6, 5, and so on, producing 
# 92658374. If the crab were to 
# complete all 100 moves, the order 
# after cup 1 would be 67384529. 
# 
# Using your labeling, simulate 100 
# moves. What are the labels on the 
# cups after cup 1? 
# 
# --- Part Two ---
# 
# Due to what you can only assume is 
# a mistranslation (you're not 
# exactly fluent in Crab), you are 
# quite surprised when the crab 
# starts arranging many cups in a 
# circle on your raft - one million 
# (1000000) in total. 
# 
# Your labeling is still correct for 
# the first few cups; after that, 
# the remaining cups are just 
# numbered in an increasing fashion 
# starting from the number after the 
# highest number in your list and 
# proceeding one by one until one 
# million is reached. (For example, 
# if your labeling were 54321, the 
# cups would be numbered 5, 4, 3, 2, 
# 1, and then start counting up from 
# 6 until one million is reached.) 
# In this way, every number from one 
# through one million is used 
# exactly once. 
# 
# After discovering where you made 
# the mistake in translating Crab 
# Numbers, you realize the small 
# crab isn't going to do merely 100 
# moves; the crab is going to do ten 
# million (10000000) moves! 
# 
# The crab is going to hide your 
# stars - one each - under the two 
# cups that will end up immediately 
# clockwise of cup 1. You can have 
# them if you predict what the 
# labels on those cups will be when 
# the crab is finished. 
# 
# In the above example (389125467), 
# this would be 934001 and then 
# 159792; multiplying these together 
# produces 149245887792. 
# 
# Determine which two cups will end 
# up immediately clockwise of cup 1. 
# What do you get if you multiply 
# their labels together? 
# 
from get_input import get_input


class Cup:
    def __init__(self, value):
        self._value = None
        self._left = None
        self._right = None
        self.value = value
        
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, value):
        if isinstance(value, Cup):
            self._left = value
    
    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, value):
        if isinstance(value, Cup):
            self._right = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if type(val) is int:
            self._value = val
    
    def __next__(self):
        return self.right
        
    def __repr__(self):
        return repr(self._value)
    

class Circle:
    def __init__(self, string, p2=False):
        self._circle = {int(i): Cup(int(i)) for i in string if i.isnumeric()}
        if p2:
            for i in range(10, 1_000_001):
                self._circle.update({i: Cup(i)})
        l = list(self._circle.keys())
        for index, key in enumerate(l):
            value = self._circle[key]
            if index == 0:
                value.left = self._circle[l[-1]]
                value.right = self._circle[l[index + 1]]
                continue
            elif index == len(l) - 1:
                value.left = self._circle[l[index - 1]]
                value.right = self._circle[l[0]]
                break
            else:
                value.left = self._circle[l[index - 1]]
                value.right = self._circle[l[index + 1]]
                
        self.current = self._circle[l[0]]
        
    def rotate(self):
        current_cup = self.current
        next_three = [next(current_cup)]
        for _ in range(2):
            next_three.append(next(next_three[-1]))
        after = next(next_three[-1])
        current_cup.right, after.left = after, current_cup
        dest_cup_value = current_cup.value - 1
        while any(i.value == dest_cup_value for i in next_three) or dest_cup_value not in self._circle:
            dest_cup_value -= 1
            if dest_cup_value <= 0:
                dest_cup_value += max(self._circle) + 1
        dest_cup = self._circle[dest_cup_value]
        after = next(dest_cup)
        dest_cup.right, next_three[0].left, next_three[-1].right, after.left = next_three[0], dest_cup, after, next_three[-1]
        self.current = next(self.current)
        
    def __getitem__(self, index):
        return self._circle[index]
        
    def __repr__(self):
        start = [self._circle[list(self._circle.keys())[0]]]
        for _ in range(len(self._circle)):
            start.append(next(start[-1]))
        return str(start)
    
    def __len__(self):
        return len(self._circle)
    

def main():
    given = get_input(23, 2020)
    circle = Circle(given)
    for _ in range(100):
        circle.rotate()
    ans = [circle[1]]
    for _ in range(len(circle) - 1):
        ans.append(next(ans[-1]))
    
    print(f"Part 1: {''.join(str(i) for i in ans[1:])}")
    
    circle = Circle(given, True)
    for i in range(10_000_000):
        if i % 1000 == 0:
            print(f'\rPart 2: {100 * i / 10_000_000:6.2f}%',end='\r')
        circle.rotate()
    next_two = [next(circle[1]), next(next(circle[1]))]
    ans = next_two[0].value * next_two[1].value
    print(f"\rPart 2: {ans}")


if __name__ == "__main__":
    main()

