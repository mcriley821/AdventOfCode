#!/usr/bin/env python
# Day 5 - Advent of Code 2015
# --- Day 5: Doesn't He Have 
# Intern-Elves For This? --- 
# 
# Santa needs help figuring out 
# which strings in his text file are 
# naughty or nice. 
# 
# A nice string is one with all of 
# the following properties: 
# 
# It contains at least three vowels 
# (aeiou only), like aei, xazegov, 
# or aeiouaeiouaeiou. 
# It contains at least one letter 
# that appears twice in a row, like 
# xx, abcdde (dd), or aabbccdd (aa, 
# bb, cc, or dd). 
# It does not contain the strings 
# ab, cd, pq, or xy, even if they 
# are part of one of the other 
# requirements. 
# For example:
# 
# ugknbfddgicrmopn is nice because 
# it has at least three vowels 
# (u...i...o...), a double letter 
# (...dd...), and none of the 
# disallowed substrings. 
# aaa is nice because it has at 
# least three vowels and a double 
# letter, even though the letters 
# used by different rules overlap. 
# jchzalrnumimnmhp is naughty 
# because it has no double letter. 
# haegwjzuvuyypxyu is naughty 
# because it contains the string xy. 
# dvszwmarrgswjxmb is naughty 
# because it contains only one 
# vowel. 
# How many strings are nice?
# 
# --- Part Two ---
# 
# Realizing the error of his ways, 
# Santa has switched to a better 
# model of determining whether a 
# string is naughty or nice. None of 
# the old rules apply, as they are 
# all clearly ridiculous. 
# 
# Now, a nice string is one with all 
# of the following properties: 
# 
# It contains a pair of any two 
# letters that appears at least 
# twice in the string without 
# overlapping, like xyxy (xy) or 
# aabcdefgaa (aa), but not like aaa 
# (aa, but it overlaps). 
# It contains at least one letter 
# which repeats with exactly one 
# letter between them, like xyx, 
# abcdefeghi (efe), or even aaa. 
# For example:
# 
# qjhvhtzxzqqjkmpb is nice because 
# is has a pair that appears twice 
# (qj) and a letter that repeats 
# with exactly one letter between 
# them (zxz). 
# xxyxx is nice because it has a 
# pair that appears twice and a 
# letter that repeats with one 
# between, even though the letters 
# used by each rule overlap. 
# uurcxstgmygtbstg is naughty 
# because it has a pair (tg) but no 
# repeat with a single letter 
# between them. 
# ieodomkazucvgmuy is naughty 
# because it has a repeating letter 
# with one between (odo), but no 
# pair that appears twice. 
# How many strings are nice under 
# these new rules? 

from get_input import get_input
from string import ascii_lowercase as alph


def is_nice_string(s):
    nots = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    if any(i in s for i in nots):
        return False
    if sum(s.count(i) for i in vowels) < 3:
                return False
    doubles = list(map(lambda x: 2 * x, alph))
    if any(i in s for i in doubles):
        return True
    return False


def new_is_nice(s):
    has_double = False
    has_sandwich = False
    for ind, char in enumerate(s):
        if ind + 1 < len(s):
            sub_s = char + s[ind + 1]
        if s.count(sub_s) >= 2:
            has_double = True
        if ind + 2 < len(s):
            if s[ind + 2] == char:
                has_sandwich = True
    if has_double and has_sandwich:
        return True
    return False    


def main():
    given = get_input(5, 2015)
    given = given.split('\n')[:-1]
    
    nice_count = sum(
        is_nice_string(i) for i in given)
    print('Part 1:', nice_count)
    
    new_count = sum(
        new_is_nice(i) for i in given)
    print('Part 2:', new_count)


if __name__ == "__main__":
    main()

