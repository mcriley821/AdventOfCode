#!/usr/bin/env python
# Day 10 - Advent of Code 2015 
# --- Day 10: Elves Look, Elves Say 
# --- 
# 
# Today, the Elves are playing a 
# game called look-and-say. They 
# take turns making sequences by 
# reading aloud the previous 
# sequence and using that reading as 
# the next sequence. For example, 
# 211 is read as "one two, two 
# ones", which becomes 1221 (1 2, 2 
# 1s). 
# 
# Look-and-say sequences are 
# generated iteratively, using the 
# previous value as input for the 
# next step. For each step, take the 
# previous value, and replace each 
# run of digits (like 111) with the 
# number of digits (3) followed by 
# the digit itself (1). 
# 
# For example:
# 
# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by 
# one 1). 
# 1211 becomes 111221 (one 1, one 2, 
# and two 1s). 
# 111221 becomes 312211 (three 1s, 
# two 2s, and one 1). 
# Starting with the digits in your 
# puzzle input, apply this process 
# 40 times. What is the length of 
# the result? 
# 
# --- Part Two ---
# 
# Neat, right? You might also enjoy 
# hearing John Conway talking about 
# this sequence (that's Conway of 
# Conway's Game of Life fame). 
# 
# Now, starting again with the 
# digits in your puzzle input, apply 
# this process 50 times. What is the 
# length of the new result? 
# 
from get_input import get_input


def to_strings(num):
    strings = []
    current = ''
    for ind, char in enumerate(num):
        current += char
        if ind + 1 >= len(num):
            strings.append(current)
            break
        if char != num[ind + 1]:
            strings.append(current)
            current = ''
    return strings


def to_number(strings):
    return ''.join(str(len(i)) + i[0] for i in strings) 


def main():
    given = get_input(10, 2015)[:-1]
    num = given
    for i in range(40):
        num = to_strings(num)
        num = to_number(num)
        print(f"\rPart 1: {i * 100/ 40}%\t", end='\r')
    print(f'\rPart 1: {len(num)}\t\r')
    
    num = given
    for i in range(50):
        num = to_strings(num)
        num = to_number(num)
        print(f"\rPart 2: {i * 2}%\t", end='\r')
    print(f'\rPart 2: {len(num)}\r')


if __name__ == "__main__":
    main()

