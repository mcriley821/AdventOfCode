#!/usr/bin/env python
from argparse import ArgumentParser
from datetime import datetime


def process_description(description: str) -> list[str]:
    desc_lines = description.split("\n")
    for line_no, line in enumerate(iter(desc_lines)):
        line = "#  " + line.lstrip()
        if len(line) > 80:
            ind = 80
            while not line[ind].isspace():
                ind -= 1

            desc_lines[line_no] = line[:ind] + '\n'
            desc_lines.insert(line_no + 1, line[ind + 1:])
        else:
            desc_lines[line_no] = line + '\n'
    return desc_lines


def add_description(puzzle: int, year: int, description: str):
    fname = f"Puzzles/{year}/Puzzle{str(puzzle).zfill(2)}.py"
    with open(fname, 'r') as f:
        script = f.readlines()

    for line_no, line in enumerate(script):
        if not line.startswith('#'):
            break
    
    description = process_description(description)
    for line in reversed(description):
        script.insert(line_no, line)
    
    with open(fname, 'w') as f:
        f.writelines(script)


def main():
    parser = ArgumentParser()
    parser.add_argument("puzzle", type=int, help="puzzle number to add to")
    parser.add_argument("desc", help="description to insert")
    parser.add_argument("-t", "--year", type=int, default=datetime.now().year,
                        help="specify the year of the puzzle")

    ns = parser.parse_args()

    add_description(ns.puzzle, ns.year, ns.desc)


if __name__ == "__main__":
    main()

