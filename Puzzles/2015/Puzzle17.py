#!/usr/bin/env python
# Day 17 - Advent of Code 2015 
# --- Day 17: No Such Thing as Too 
# Much --- 
# 
# The elves bought too much eggnog 
# again - 150 liters this time. To 
# fit it all into your refrigerator, 
# you'll need to move it into 
# smaller containers. You take an 
# inventory of the capacities of the 
# available containers. 
# 
# For example, suppose you have 
# containers of size 20, 15, 10, 5, 
# and 5 liters. If you need to store 
# 25 liters, there are four ways to 
# do it: 
# 
# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
# Filling all containers entirely, 
# how many different combinations of 
# containers can exactly fit all 150 
# liters of eggnog? 
# 
# Your puzzle answer was 4372.
# 
# The first half of this puzzle is 
# complete! It provides one gold 
# star: * 
# 
# --- Part Two ---
# 
# While playing with all the 
# containers in the kitchen, another 
# load of eggnog arrives! The 
# shipping and receiving department 
# is requesting as many containers 
# as you can spare. 
# 
# Find the minimum number of 
# containers that can exactly fit 
# all 150 liters of eggnog. How many 
# different ways can you fill that 
# number of containers and still 
# hold exactly 150 litres? 
# 
# In the example above, the minimum 
# number of containers was two. 
# There were three ways to use that 
# many containers, and so the answer 
# there would be 3. 
# 
from get_input import get_input
from itertools import combinations


def main():
    given = get_input(17, 2015)
    given = [int(i) for i in given.split('\n') if i != '']
    count = 0
    ways = []
    for i in range(1, len(given)):
        for comb in combinations(given, i):
            if sum(comb) == 150:
                count += 1
                ways.append(comb)
    print(f"Part 1: {count}")
    
    minim = min(ways, key=len)
    print(f"Part 2: {sum(1 for i in ways if len(i) == len(minim))}")


if __name__ == "__main__":
    main()

