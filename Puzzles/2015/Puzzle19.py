#!/usr/bin/env python
from get_input import get_input
import re


def parse_given(given):
    subs = {}
    molecule = ""
    for line in given.split('\n'):
        if line == '':
            continue
        elif '=>' in line:
            mole, rep = line.split(' => ')
            subs[mole] = rep
        else:
            molecule = line
    return (subs, molecule)


def main():
    given = get_input(19, 2015)
    subs, mole = parse_given(given)
    
    # Part 1
    moles = set()
    for sub in subs:
        out = []
        temp = mole.partition(sub)
        while sub in temp[-1]:
            out.extend(temp[:-1])
            temp = temp[-1].partition(sub)
        if len(out) == 0:
            out = list(temp)
        while '' in out:
            out.remove('')
        for i in range(out.count(sub)):
            temp = out.copy()
            temp[temp.index(sub, i + 1)] = subs[sub]
            print(temp, '\n')
            moles.add(''.join(i for i in temp))
    print(f"Part 1: {len(moles)}")


if __name__ == "__main__":
    main()

