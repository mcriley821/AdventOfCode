#!/usr/bin/env python
# Day 16 - Advent of Code 2015 
# --- Day 16: Aunt Sue ---
# 
# Your Aunt Sue has given you a 
# wonderful gift, and you'd like to 
# send her a thank you card. 
# However, there's a small problem: 
# she signed it "From, Aunt Sue". 
# 
# You have 500 Aunts named "Sue".
# 
# So, to avoid sending the card to 
# the wrong person, you need to 
# figure out which Aunt Sue (which 
# you conveniently number 1 to 500, 
# for sanity) gave you the gift. You 
# open the present and, as luck 
# would have it, good ol' Aunt Sue 
# got you a My First Crime Scene 
# Analysis Machine! Just what you 
# wanted. Or needed, as the case may 
# be. 
# 
# The My First Crime Scene Analysis 
# Machine (MFCSAM for short) can 
# detect a few specific compounds in 
# a given sample, as well as how 
# many distinct kinds of those 
# compounds there are. According to 
# the instructions, these are what 
# the MFCSAM can detect: 
# 
# children, by human DNA age analysis.
# cats. It doesn't differentiate 
# individual breeds. 
# Several seemingly random breeds of 
# dog: samoyeds, pomeranians, 
# akitas, and vizslas. 
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or 
# gasoline or something. 
# perfumes, which is handy, since 
# many of your Aunts Sue wear a few 
# kinds. 
# In fact, many of your Aunts Sue 
# have many of these. You put the 
# wrapping from the gift into the 
# MFCSAM. It beeps inquisitively at 
# you a few times and then prints 
# out a message on ticker tape: 
# 
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
# You make a list of the things you 
# can remember about each Aunt Sue. 
# Things missing from your list 
# aren't zero - you simply don't 
# remember the value. 
# 
# What is the number of the Sue that 
# got you the gift? 
# 
# --- Part Two ---
# 
# As you're about to send the thank 
# you note, something in the 
# MFCSAM's instructions catches your 
# eye. Apparently, it has an 
# outdated retroencabulator, and so 
# the output from the machine isn't 
# exact values - some of them 
# indicate ranges. 
# 
# In particular, the cats and trees 
# readings indicates that there are 
# greater than that many (due to the 
# unpredictable nuclear decay of cat 
# dander and tree pollen), while the 
# pomeranians and goldfish readings 
# indicate that there are fewer than 
# that many (due to the modial 
# interaction of magnetoreluctance). 
# 
# What is the number of the real 
# Aunt Sue? 
# 
from get_input import get_input


mfcsam_output = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1 
}


def find_sue(all_sues, p1=False):
    out = ('', 0)
    for sue in all_sues.split('\n'):
        if sue != '':
            num = sue.split(':')[0].replace('Sue ','')
            attrs = sue.replace(f'Sue {num}: ', '')
            likeihood = 0
            for attr in attrs.split(', '):
                name, val = attr.split(':')
                if (name == 'cats' or name == 'trees' ) and mfcsam_output[name] < int(val) and not p1:
                    likeihood += 1
                elif (name == 'pomeranians' or name == 'goldfish') and mfcsam_output[name] > int(val) and not p1:
                    likeihood += 1
                elif mfcsam_output[name] == int(val):
                    likeihood += 1
            if likeihood > out[1]:
                out = (sue, likeihood)
    return out[0].split(':')[0]


def main():
    given = get_input(16, 2015)
    print(f'Part 1: {find_sue(given, True)}')
    print(f'Part 2: {find_sue(given)}')


if __name__ == "__main__":
    main()

