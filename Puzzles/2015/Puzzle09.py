#!/usr/bin/env python
# Day 9 - Advent of Code 2015 
# --- Day 9: All in a Single Night ---
# 
# Every year, Santa manages to 
# deliver all of his presents in a 
# single night. 
# 
# This year, however, he has some 
# new locations to visit; his elves 
# have provided him the distances 
# between every pair of locations. 
# He can start and end at any two 
# (different) locations he wants, 
# but he must visit each location 
# exactly once. What is the shortest 
# distance he can travel to achieve 
# this? 
# 
# For example, given the following 
# distances: 
# 
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:
# 
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> 
# Dublin -> Belfast = 605, and so 
# the answer is 605 in this example. 
# 
# What is the distance of the 
# shortest route? 
# 
# --- Part Two ---
# 
# The next year, just to show off, 
# Santa decides to take the route 
# with the longest distance instead. 
# 
# He can still start and end at any 
# two (different) locations he 
# wants, and he still must visit 
# each location exactly once. 
# 
# For example, given the distances 
# above, the longest route would be 
# 982 via (for example) Dublin -> 
# London -> Belfast. 
# 
# What is the distance of the 
# longest route? 
# 
# 
# 
from get_input import get_input
from itertools import permutations
import sys


def parse_distances(distances):
    out = {}
    locs = []
    for distance in distances.split('\n'):
        if distance != '':
            trip, dist = distance.split(' = ')
            _from, _to = trip.split(' to ')
            if _to not in locs:
                locs.append(_to)
            if _from not in locs:
                locs.append(_from)
            dist = int(dist)
            if trip not in out.keys():
                out.update({trip: dist})
            reverse = f"{_to} to {_from}"
            if reverse not in out.keys():
                out.update({reverse: dist})
    return out, locs


def main():
    given = get_input(9, 2015)
    dists, locs = parse_distances(given)
    
    def make_path(lists):
        out = []
        for ind, each in enumerate(lists):
            if ind == len(lists) - 1:
                break
            else:
                out.append(f"{each} to {lists[ind + 1]}")
        return out

    def get_min_max(locations):
        minim = sys.maxsize
        maxim = 0
        for path in permutations(locations):
            temp = sum(dists[i] for i in make_path(path))
            if temp < minim:
                minim = temp
            if temp > maxim:
                maxim = temp
        return (minim, maxim)
    
    mini, maxi = get_min_max(locs)
    print('Part 1:', mini)
    print('Part 2:', maxi)

    
if __name__ == "__main__":
    main()

