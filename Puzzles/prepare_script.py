#!/usr/bin/env python
from os import makedirs, chmod
from os.path import exists
from bs4 import BeautifulSoup
import requests
import pathlib
import os


PUZZLES_DIRECTORY = pathlib.Path(__file__).parent
assert PUZZLES_DIRECTORY.name == "Puzzles", "Script not in correct directory!"
GET_INPUT_SCRIPT = PUZZLES_DIRECTORY / "get_input.py"
SCRIPT_TEMPLATE = PUZZLES_DIRECTORY / "puzzle_template.py"
INPUTS_DIRECTORY = PUZZLES_DIRECTORY / "Inputs"
ADVENT_OF_CODE_URL = "https://adventofcode.com"


def process_description_chunk(chunk: str) -> str:
    ind = 0
    new_chunk = ''
    while ind < len(chunk):
        size = 75
        line = chunk[ind: ind + size]
        if len(line) == size:
            while not line[-1].isspace():
                size -= 1
                line = chunk[ind: ind + size]
        line = line.strip()
        new_chunk += f"#  {line}\n"
        ind += size
    return new_chunk


def get_description(puzzle: int, year: int) -> str:
    url = f"{ADVENT_OF_CODE_URL}/{year}/day/{puzzle}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Puzzle page returned: {response.reason}")
    puzzle_page = BeautifulSoup(response.content, "html.parser")
    description_html = puzzle_page.find("article", class_="day-desc")
    description = ""
    for element in description_html.children:
        description += process_description_chunk(
                ''.join(i for i in element.strings if i))
    index = 0
    for line in description.split('\n'):
        if line and not line.startswith("#  "):
            description = f"{description[:index]}#  {description[index:]}"
            index += 3
        index += len(line) + 1  # account for \n that was lost each line
    return description


def prepare_puzzle_directory(puzzle_dir: pathlib.Path):
    if not puzzle_dir.exists():
        puzzle_dir.mkdir()
        get_input_symlink = puzzle_dir / GET_INPUT_SCRIPT.name
        get_input_symlink.symlink_to(GET_INPUT_SCRIPT)


def prepare_script(puzzle: int, year: int, overwrite: bool = False):
    puzzle_dir = PUZZLES_DIRECTORY / str(year)
    prepare_puzzle_directory(puzzle_dir)
    script_file = puzzle_dir / f"Puzzle{puzzle:02}.py"
    if not script_file.exists() or overwrite:
        script_file.write_text(fill_script_template(puzzle, year))
        script_file.chmod(0o755)
    else:
        print("File exists, so not preparing...")


def fill_script_template(puzzle: int, year: int) -> str:
    template = SCRIPT_TEMPLATE.read_text()
    return template.replace("%puzzle", str(puzzle)).replace("%year", str(year))


def main():
    from argparse import ArgumentParser
    from datetime import datetime

    parser = ArgumentParser()
    parser.add_argument("puzzle", type=int, help="puzzle number to get")
    parser.add_argument("-y", "--year", type=int, default=datetime.now().year,
                        help="year of the puzzle to get")
    parser.add_argument("-f", "--force", action="store_true",
                        help="force overwrite an existing file")
    ns = parser.parse_args()

    prepare_script(ns.puzzle, ns.year, overwrite=ns.force)


if __name__ == "__main__":
    main()

