#!/usr/bin/env python
from PrepareScript import process_description_chunk
from argparse import ArgumentParser
from datetime import datetime


def add_description(puzzle: int, year: int, description: str):
    fname = f"{year}/Puzzle{str(puzzle).zfill(2)}.py"
    with open(fname, 'r') as f:
        script = f.read()

    index = 0
    for line in script.split('\n'):
        if not line.startswith('#'):
            break
        index += len(line) + 1
    processed = process_description_chunk(description)
    ind = 0
    for line in processed.split('\n'):
        if not line.startswith('#  '):
            processed = f"{processed[:ind] }#  {processed[ind:]}"
            ind += 3
        ind += len(line) + 1
    new_script = script[:index] + processed + '\n' + script[index:]
    
    with open(fname, 'w') as f:
        f.write(new_script)


def main():
    parser = ArgumentParser()
    parser.add_argument("puzzle", type=int, help="puzzle number to add to")
    parser.add_argument("part_two_desc", help="description of part 2")
    parser.add_argument("-t", "--year", type=int, default=datetime.now().year,
                        help="specify the year of the puzzle")

    ns = parser.parse_args()

    add_description(ns.puzzle, ns.year, ns.part_two_desc)


if __name__ == "__main__":
    main()

