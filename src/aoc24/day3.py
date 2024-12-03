from aocd import get_data
import re


def solve_part1() -> None:
    input = get_data(day=3, year=2024)
    matches = re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=input)
    result = sum([int(match[0])*int(match[1]) for match in matches])
    print(result)