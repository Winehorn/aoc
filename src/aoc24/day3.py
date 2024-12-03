from aocd import get_data
import re


def solve_part1() -> None:
    input = get_data(day=3, year=2024)
    result = _get_result(input=input, use_conditionals=False)
    print(result)

def solve_part2() -> None:
    input = get_data(day=3, year=2024)
    result = _get_result(input=input, use_conditionals=True)
    print(result)

def _get_result(input: str, use_conditionals: bool = False) -> int:
    matches = re.findall(pattern=r"(don't|do)|mul\((\d{1,3}),(\d{1,3})\)", string=input)
    do = True
    result = 0
    for match in matches:
        if match[0]:
            do = match[0] == "do"
            continue
        if use_conditionals and not do:
            continue
        if match[1] and match[2]:
            result += int(match[1])*int(match[2])
    return result