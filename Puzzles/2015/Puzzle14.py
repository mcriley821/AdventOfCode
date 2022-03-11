#!/usr/bin/env python
# Day 14 - Advent of Code 2015 
# --- Day 14: Reindeer Olympics ---
# 
# This year is the Reindeer 
# Olympics! Reindeer can fly at high 
# speeds, but must rest occasionally 
# to recover their energy. Santa 
# would like to know which of his 
# reindeer is fastest, and so he has 
# them race. 
# 
# Reindeer can only either be flying 
# (always at their top speed) or 
# resting (not moving at all), and 
# always spend whole seconds in 
# either state. 
# 
# For example, suppose you have the 
# following Reindeer: 
# 
# Comet can fly 14 km/s for 10 
# seconds, but then must rest for 
# 127 seconds. 
# Dancer can fly 16 km/s for 11 
# seconds, but then must rest for 
# 162 seconds. 
# After one second, Comet has gone 
# 14 km, while Dancer has gone 16 
# km. After ten seconds, Comet has 
# gone 140 km, while Dancer has gone 
# 160 km. On the eleventh second, 
# Comet begins resting (staying at 
# 140 km), and Dancer continues on 
# for a total distance of 176 km. On 
# the 12th second, both reindeer are 
# resting. They continue to rest 
# until the 138th second, when Comet 
# flies for another ten seconds. On 
# the 174th second, Dancer flies for 
# another 11 seconds. 
# 
# In this example, after the 1000th 
# second, both reindeer are resting, 
# and Comet is in the lead at 1120 
# km (poor Dancer has only gotten 
# 1056 km by that point). So, in 
# this situation, Comet would win 
# (if the race ended at 1000 
# seconds). 
# 
# Given the descriptions of each 
# reindeer (in your puzzle input), 
# after exactly 2503 seconds, what 
# distance has the winning reindeer 
# traveled?
# 
# --- Part Two ---
# 
# Seeing how reindeer move in 
# bursts, Santa decides he's not 
# pleased with the old scoring 
# system. 
# 
# Instead, at the end of each 
# second, he awards one point to the 
# reindeer currently in the lead. 
# (If there are multiple reindeer 
# tied for the lead, they each get 
# one point.) He keeps the 
# traditional 2503 second time 
# limit, of course, as doing 
# otherwise would be entirely 
# ridiculous. 
# 
# Given the example reindeer from 
# above, after the first second, 
# Dancer is in the lead and gets one 
# point. He stays in the lead until 
# several seconds into Comet's 
# second burst: after the 140th 
# second, Comet pulls into the lead 
# and gets his first point. Of 
# course, since Dancer had been in 
# the lead for the 139 seconds 
# before that, he has accumulated 
# 139 points by the 140th second. 
# 
# After the 1000th second, Dancer 
# has accumulated 689 points, while 
# poor Comet, our old champion, only 
# has 312. So, with the new scoring 
# system, Dancer would win (if the 
# race ended at 1000 seconds). 
# 
# Again given the descriptions of 
# each reindeer (in your puzzle 
# input), after exactly 2503 
# seconds, how many points does the 
# winning reindeer have? 
# 
from get_input import get_input


def parse_racer_info(racer_info):
    racers = {}
    for line in racer_info.split('\n'):
        if line != '':
            line = line.replace(' can fly', '') 
            line = line.replace(' seconds, but then must rest for', '')
            line = line.replace(' km/s for', '')
            line = line.replace(' seconds.', '')
            racer, speed, time, rest_time = line.split(' ')
            racers.update({
                racer: {
                    'speed': int(speed),
                    'stamina': int(time), 
                    'rest': int(rest_time),
                    'distance': 0,
                    'points': 0,
                    'timer': 0,
                    'flying': False
                    }
                })
    return racers


def time_step(racers):
    for racer in racers:
        racer = racers[racer]
        if racer['timer'] == 0:
            racer['flying'] = not racer['flying']
            racer['timer'] += racer['rest'] if not racer['flying'] else racer['stamina']
        racer['timer'] -= 1
        if racer['flying']:
            racer['distance'] += racer['speed']


def assign_points(racers):
    top = racers[max(racers, key=lambda x: racers[x]['distance'])]['distance']
    for racer in racers:
        racer = racers[racer]
        if racer['distance'] == top:
            racer['points'] += 1
            

def main():
    given = get_input(14, 2015)
    racers = parse_racer_info(given)
    for i in range(2503):
        time_step(racers)
        assign_points(racers)
    print('Part 1:', racers[max(racers, key=lambda x: racers[x]['distance'])]['distance'])
    print('Part 2:', racers[max(racers, key=lambda x: racers[x]['points'])]['points'])
    
    
if __name__ == "__main__":
    main()

