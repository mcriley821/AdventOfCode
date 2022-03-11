#!/usr/bin/env python
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
assert ROOT_DIR.name == "AdventOfCode", "Script in incorrect directory!"


def get_input(puzzle: int, year: int) -> str:
    input_dir = ROOT_DIR / "Inputs" / str(year)
    file = input_dir / f"Puzzle{puzzle:02}Input.txt"
    if file.exists():
        return file.read_text()
    else:
        raise FileNotFoundError(f"Couldn't find {file}!")

