from aocd import get_data
import re


def solve_part1() -> None:
    input = get_data(day=3, year=2024)
    result = _get_result(input=input, use_conditionals=False)
    print(result)

def _get_result(input: str, use_conditionals: bool = False) -> int:
    matches = re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=input)
    result = sum([int(match[0])*int(match[1]) for match in matches])
    return result