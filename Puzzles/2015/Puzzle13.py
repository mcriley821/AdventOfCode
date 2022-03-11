#!/usr/bin/env python
# Day 13 - Advent of Code 2015 
# --- Day 13: Knights of the Dinner 
# Table --- 
# 
# In years past, the holiday feast 
# with your family hasn't gone so 
# well. Not everyone gets along! 
# This year, you resolve, will be 
# different. You're going to find 
# the optimal seating arrangement 
# and avoid all those awkward 
# conversations. 
# 
# You start by writing up a list of 
# everyone invited and the amount 
# their happiness would increase or 
# decrease if they were to find 
# themselves sitting next to each 
# other person. You have a circular 
# table that will be just big enough 
# to fit everyone comfortably, and 
# so each person will have exactly 
# two neighbors. 
# 
# For example, suppose you have only 
# four attendees planned, and you 
# calculate their potential 
# happiness as follows: 
# 
# Alice would gain 54 happiness 
# units by sitting next to Bob. 
# Alice would lose 79 happiness 
# units by sitting next to Carol. 
# Alice would lose 2 happiness units 
# by sitting next to David. 
# Bob would gain 83 happiness units 
# by sitting next to Alice. 
# Bob would lose 7 happiness units 
# by sitting next to Carol. 
# Bob would lose 63 happiness units 
# by sitting next to David. 
# Carol would lose 62 happiness 
# units by sitting next to Alice. 
# Carol would gain 60 happiness 
# units by sitting next to Bob. 
# Carol would gain 55 happiness 
# units by sitting next to David. 
# David would gain 46 happiness 
# units by sitting next to Alice. 
# David would lose 7 happiness units 
# by sitting next to Bob. 
# David would gain 41 happiness 
# units by sitting next to Carol. 
# Then, if you seat Alice next to 
# David, Alice would lose 2 
# happiness units (because David 
# talks so much), but David would 
# gain 46 happiness units (because 
# Alice is such a good listener), 
# for a total change of 44. 
# 
# If you continue around the table, 
# you could then seat Bob next to 
# Alice (Bob gains 83, Alice gains 
# 54). Finally, seat Carol, who sits 
# next to Bob (Carol gains 60, Bob 
# loses 7) and David (Carol gains 
# 55, David gains 41). The 
# arrangement looks like this: 
# 
#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83
# After trying every other seating 
# arrangement in this hypothetical 
# scenario, you find that this one 
# is the most optimal, with a total 
# change in happiness of 330. 
# 
# What is the total change in 
# happiness for the optimal seating 
# arrangement of the actual guest 
# list? 
# 
# --- Part Two ---
# 
# In all the commotion, you realize 
# that you forgot to seat yourself. 
# At this point, you're pretty 
# apathetic toward the whole thing, 
# and your happiness wouldn't really 
# go up or down regardless of who 
# you sit next to. You assume 
# everyone else would be just as 
# ambivalent about sitting next to 
# you, too. 
# 
# So, add yourself to the list, and 
# give all happiness relationships 
# that involve you a score of 0. 
# 
# What is the total change in 
# happiness for the optimal seating 
# arrangement that actually includes 
# yourself? 
# 
from get_input import get_input
from itertools import permutations


def parse_guest_info(guest_info):
    guests = {}
    guest_list = []
    for line in guest_info:
        line = line.replace(' would', '')
        line = line.replace(' happiness units by sitting next to', '')
        line = line.replace('.','')
        guest, pos_neg, val, next_to = line.split(' ')
        if pos_neg == 'gain':
            val = int(val)
        else:
            val = -int(val)
        if guest not in guest_list:
            guest_list.append(guest)
        if guest not in guests:
            guests.update({guest: {}})
        guests[guest].update({next_to: val})
    return guest_list, guests        
    

def calculate_happiness(info, arrangement):
    total = 0
    for ind, person in enumerate(arrangement):
        if ind + 1 >= len(arrangement):
            total += info[person][arrangement[0]]
            total += info[arrangement[0]][person]
            break
        total += info[person][arrangement[ind + 1]]
        total += info[arrangement[ind + 1]][person]
    return total
        
        
def main():
    given = get_input(13, 2015)
    given = [i for i in given.split('\n') if i != '']
    guest_list, guests = parse_guest_info(given)
        
    print('Part 1:', max(calculate_happiness(guests, arrangement) for arrangement in permutations(guest_list)))
    
    guests.update({'Myself': {}})    
    for guest in guest_list:
        guests['Myself'].update({guest: 0})
        guests[guest].update({'Myself': 0})
    guest_list.append('Myself')
    
    print('Part 2:', max(calculate_happiness(guests, arrangement) for arrangement in permutations(guest_list)))


if __name__ == "__main__":
    main()

