#!/usr/bin/env python
# Day 7 - Advent of Code 2015 
# --- Day 7: Some Assembly Required 
# --- 
# 
# This year, Santa brought little 
# Bobby Tables a set of wires and 
# bitwise logic gates! 
# Unfortunately, little Bobby is a 
# little under the recommended age 
# range, and he needs help 
# assembling the circuit. 
# 
# Each wire has an identifier (some 
# lowercase letters) and can carry a 
# 16-bit signal (a number from 0 to 
# 65535). A signal is provided to 
# each wire by a gate, another wire, 
# or some specific value. Each wire 
# can only get a signal from one 
# source, but can provide its signal 
# to multiple destinations. A gate 
# provides no signal until all of 
# its inputs have a signal. 
# 
# The included instructions booklet 
# describes how to connect the parts 
# together: x AND y -> z means to 
# connect wires x and y to an AND 
# gate, and then connect its output 
# to wire z. 
# 
# For example:
# 
# 123 -> x means that the signal 123 
# is provided to wire x. 
# x AND y -> z means that the 
# bitwise AND of wire x and wire y 
# is provided to wire z. 
# p LSHIFT 2 -> q means that the 
# value from wire p is left-shifted 
# by 2 and then provided to wire q. 
# NOT e -> f means that the bitwise 
# complement of the value from wire 
# e is provided to wire f. 
# Other possible gates include OR 
# (bitwise OR) and RSHIFT 
# (right-shift). If, for some 
# reason, you'd like to emulate the 
# circuit instead, almost all 
# programming languages (for 
# example, C, JavaScript, or Python) 
# provide operators for these gates. 
# 
# For example, here is a simple 
# circuit: 
# 
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
#
# After it is run, these are the 
# signals on the wires: 
# 
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
#
# In little Bobby's kit's 
# instructions booklet (provided as 
# your puzzle input), what signal is 
# ultimately provided to wire a? 
# 
# --- Part Two ---
# 
# Now, take the signal you got on 
# wire a, override wire b to that 
# signal, and reset the other wires 
# (including wire a). What new 
# signal is ultimately provided to 
# wire a? 
# 
from get_input import get_input
from functools import cache
            

def parse_ops(given):
    out = {}
    for line in given:
        op, end = line.split(' -> ')
        out.update({end: op})
    return out


ops = {}

@cache
def get_value(name):
    if name.isnumeric():
        return int(name)
    op = ops[name]
    if op.isnumeric():
        return int(op)
    else:
        op = op.split(' ')
        if 'AND' in op:
            return get_value(op[0]) & get_value(op[2])
        elif 'OR' in op:
            return get_value(op[0]) | get_value(op[2])
        elif 'LSHIFT' in op:
            return get_value(op[0]) << get_value(op[2])
        elif 'RSHIFT' in op:
            return get_value(op[0]) >> get_value(op[2])
        elif 'NOT' in op:
            return ~get_value(op[1]) & 0xffff
        else:
            return get_value(op[0])


def main():
    given = get_input(7, 2015)
    given = [i for i in given.split('\n') if i != '']
    global ops
    ops = parse_ops(given)

    a = get_value('a')
    print('Part 1:', a)

    get_value.cache_clear()
    ops['b'] = str(a)
    print('Part 2:', get_value('a'))


if __name__ == "__main__":
    main()

