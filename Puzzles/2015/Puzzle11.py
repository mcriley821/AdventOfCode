#!/usr/bin/env python
# Day 11 - Advent of Code 2015 
# --- Day 11: Corporate Policy ---
# 
# Santa's previous password expired, 
# and he needs help choosing a new 
# one. 
# 
# To help him remember his new 
# password after the old one 
# expires, Santa has devised a 
# method of coming up with a 
# password based on the previous 
# one. Corporate policy dictates 
# that passwords must be exactly 
# eight lowercase letters (for 
# security reasons), so he finds his 
# new password by incrementing his 
# old password string repeatedly 
# until it is valid. 
# 
# Incrementing is just like counting 
# with numbers: xx, xy, xz, ya, yb, 
# and so on. Increase the rightmost 
# letter one step; if it was z, it 
# wraps around to a, and repeat with 
# the next letter to the left until 
# one doesn't wrap around. 
# 
# Unfortunately for Santa, a new 
# Security-Elf recently started, and 
# he has imposed some additional 
# password requirements: 
# 
# Passwords must include one 
# increasing straight of at least 
# three letters, like abc, bcd, cde, 
# and so on, up to xyz. They cannot 
# skip letters; abd doesn't count. 
# Passwords may not contain the 
# letters i, o, or l, as these 
# letters can be mistaken for other 
# characters and are therefore 
# confusing. 
# Passwords must contain at least 
# two different, non-overlapping 
# pairs of letters, like aa, bb, or 
# zz. 
# For example:
# 
# hijklmmn meets the first 
# requirement (because it contains 
# the straight hij) but fails the 
# second requirement requirement 
# (because it contains i and l). 
# abbceffg meets the third 
# requirement (because it repeats bb 
# and ff) but fails the first 
# requirement. 
# abbcegjk fails the third 
# requirement, because it only has 
# one double letter (bb). 
# The next password after abcdefgh 
# is abcdffaa. 
# The next password after ghijklmn 
# is ghjaabcc, because you 
# eventually skip all the passwords 
# that start with ghi..., since i is 
# not allowed. 
# Given Santa's current password 
# (your puzzle input), what should 
# his next password be? 
# 
# --- Part Two ---
# 
# Santa's password expired again. 
# What's the next one? 
# 
from get_input import get_input
from string import ascii_lowercase


def increment(string):
    next = ''
    carry = 0
    char = string[-1]
    char_pos = ascii_lowercase.index(char)
    carry, char_pos = divmod(char_pos + 1, 26)
    if carry == 1:
        next += increment(string[:-1])
    else:
        next += string[:-1]
    next += ascii_lowercase[char_pos]
    return next

    
def validate_password(string):
    for i in range(len(ascii_lowercase) - 2):
        if ascii_lowercase[i : i + 3] in string:
            break
    else:
        return False
    if any(i in string for i in ('i', 'o', 'l')):
        return False
    if sum(string.count(i) for i in map(lambda x: 2*x, ascii_lowercase)) >= 2:
        return True
    return False


def main():
    given = get_input(11, 2015)[:-1]
    while not validate_password(given):
        given = increment(given)
    print(f'Part 1: {given}')
    given = increment(given)
    print(given)
    while not validate_password(given):
        given = increment(given)
    print(f'Part 2: {given}')

    
if __name__ == "__main__":
    main()

