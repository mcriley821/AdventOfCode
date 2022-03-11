#!/usr/bin/env python
# Day 12 - Advent of Code 2020 
# --- Day 12: Rain Risk ---
# 
# Your ferry made decent progress 
# toward the island, but the storm 
# came in faster than anyone 
# expected. The ferry needs to take 
# evasive actions! 
# 
# Unfortunately, the ship's 
# navigation computer seems to be 
# malfunctioning; rather than giving 
# a route directly to safety, it 
# produced extremely circuitous 
# instructions. When the captain 
# uses the PA system to ask if 
# anyone can help, you quickly 
# volunteer. 
# 
# The navigation instructions (your 
# puzzle input) consists of a 
# sequence of single-character 
# actions paired with integer input 
# values. After staring at them for 
# a few minutes, you work out what 
# they probably mean: 
# 
# Action N means to move north by 
# the given value. 
# Action S means to move south by 
# the given value. 
# Action E means to move east by the 
# given value. 
# Action W means to move west by the 
# given value. 
# Action L means to turn left the 
# given number of degrees. 
# Action R means to turn right the 
# given number of degrees. 
# Action F means to move forward by 
# the given value in the direction 
# the ship is currently facing. 
# The ship starts by facing east. 
# Only the L and R actions change 
# the direction the ship is facing. 
# (That is, if the ship is facing 
# east and the next instruction is 
# N10, the ship would move north 10 
# units, but would still move east 
# if the following action were F.) 
# 
# For example:
# 
# F10
# N3
# F7
# R90
# F11
# These instructions would be 
# handled as follows: 
# 
# F10 would move the ship 10 units 
# east (because the ship starts by 
# facing east) to east 10, north 0. 
# N3 would move the ship 3 units 
# north to east 10, north 3. 
# F7 would move the ship another 7 
# units east (because the ship is 
# still facing east) to east 17, 
# north 3. 
# R90 would cause the ship to turn 
# right by 90 degrees and face 
# south; it remains at east 17, 
# north 3. 
# F11 would move the ship 11 units 
# south to east 17, south 8. 
# At the end of these instructions, 
# the ship's Manhattan distance (sum 
# of the absolute values of its 
# east/west position and its 
# north/south position) from its 
# starting position is 17 + 8 = 25. 
# 
# Figure out where the navigation 
# instructions lead. What is the 
# Manhattan distance between that 
# location and the ship's starting 
# position? 
# 
# --- Part Two ---
# 
# Before you can give the 
# destination to the captain, you 
# realize that the actual action 
# meanings were printed on the back 
# of the instructions the whole 
# time. 
# 
# Almost all of the actions indicate 
# how to move a waypoint which is 
# relative to the ship's position: 
# 
# Action N means to move the 
# waypoint north by the given value. 
# Action S means to move the 
# waypoint south by the given value. 
# Action E means to move the 
# waypoint east by the given value. 
# Action W means to move the 
# waypoint west by the given value. 
# Action L means to rotate the 
# waypoint around the ship left 
# (counter-clockwise) the given 
# number of degrees. 
# Action R means to rotate the 
# waypoint around the ship right 
# (clockwise) the given number of 
# degrees. 
# Action F means to move forward to 
# the waypoint a number of times 
# equal to the given value. 
# The waypoint starts 10 units east 
# and 1 unit north relative to the 
# ship. The waypoint is relative to 
# the ship; that is, if the ship 
# moves, the waypoint moves with it. 
# 
# For example, using the same 
# instructions as above: 
# 
# F10 moves the ship to the waypoint 
# 10 times (a total of 100 units 
# east and 10 units north), leaving 
# the ship at east 100, north 10. 
# The waypoint stays 10 units east 
# and 1 unit north of the ship. 
# N3 moves the waypoint 3 units 
# north to 10 units east and 4 units 
# north of the ship. The ship 
# remains at east 100, north 10. 
# F7 moves the ship to the waypoint 
# 7 times (a total of 70 units east 
# and 28 units north), leaving the 
# ship at east 170, north 38. The 
# waypoint stays 10 units east and 4 
# units north of the ship. 
# R90 rotates the waypoint around 
# the ship clockwise 90 degrees, 
# moving it to 4 units east and 10 
# units south of the ship. The ship 
# remains at east 170, north 38. 
# F11 moves the ship to the waypoint 
# 11 times (a total of 44 units east 
# and 110 units south), leaving the 
# ship at east 214, south 72. The 
# waypoint stays 4 units east and 10 
# units south of the ship. 
# After these operations, the ship's 
# Manhattan distance from its 
# starting position is 214 + 72 = 
# 286. 
# 
# Figure out where the navigation 
# instructions actually lead. What 
# is the Manhattan distance between 
# that location and the ship's 
# starting position? 
# 
# 
# 
from get_input import get_input
from math import sin, cos, pi


def move_ship(_from, command):
    direct, dist = command[0], command[1:]
    dist = int(dist)
    if direct == 'E':
        return (_from[0] + dist, _from[1], _from[2])
    elif direct == 'N':
        return  (_from[0], _from[1] + dist, _from[2])
    elif direct == 'W':
        return (_from[0] - dist, _from[1], _from[2])
    elif direct == 'S':
        return (_from[0], _from[1] - dist, _from[2])
    elif direct == 'F':
        if _from[2] == 0:
            return move_ship(_from, f'E{dist}')
        elif _from[2] == 90:
            return move_ship(_from, f'N{dist}')
        elif _from[2] == 180:
            return move_ship(_from, f'W{dist}')
        elif _from[2] == 270:
            return move_ship(_from, f'S{dist}')
    elif direct == 'L':
        return (_from[0], _from[1], (_from[2] + dist) % 360)
    elif direct == 'R':
        return (_from[0], _from[1], (_from[2] - dist) % 360)
    else:
        raise ValueError(f"Unknown command '{direct}'")


def move_waypoint(wpt_pos, ship_pos, command):
    direct, dist = command[0], command[1:]
    dist = int(dist)
    if direct == 'E':
        wpt_pos = (wpt_pos[0] + dist, wpt_pos[1])
        return (wpt_pos, ship_pos)
    elif direct == 'W':
        wpt_pos = (wpt_pos[0] - dist, wpt_pos[1])
        return (wpt_pos, ship_pos)
    elif direct == 'N':
        wpt_pos = (wpt_pos[0], wpt_pos[1] + dist)
        return (wpt_pos, ship_pos)
    elif direct == 'S':
        wpt_pos = (wpt_pos[0], wpt_pos[1] - dist)
        return (wpt_pos, ship_pos)
    elif direct == 'R':
        dist *= pi / 180
        x = round(cos(dist) * wpt_pos[0]) + round(sin(dist) * wpt_pos[1])
        y = -round(sin(dist) * wpt_pos[0]) + round(cos(dist) * wpt_pos[1])
        return ((x, y), ship_pos)
    elif direct == 'L':
        dist *= pi / 180
        x = -round(sin(dist) * wpt_pos[1]) + round(cos(dist) * wpt_pos[0])
        y = round(sin(dist)*wpt_pos[0]) + round(cos(dist) * wpt_pos[1])
        return ((x, y), ship_pos)
    elif direct == 'F':
        x = wpt_pos[0] * dist
        y = wpt_pos[1] * dist
        ship_pos = (ship_pos[0] + x, ship_pos[1] + y)
        return (wpt_pos, ship_pos)
    

def manhattan_distance(location):
    return abs(location[0]) + abs(location[1])


def main():
    given = get_input(12, 2020)
    commands = [i for i in given.split('\n') if i != '']
    pos = (0, 0, 0)
    for command in commands:
        pos = move_ship(pos, command)
    
    ship = (0, 0)
    wpt = (10, 1)
    for command in commands:
        wpt, ship = move_waypoint(wpt, ship, command)

    print(f'Part 1: {manhattan_distance(pos)}')
    print(f'Part 2: {manhattan_distance(ship)}')
    

if __name__ == "__main__":
    main()

