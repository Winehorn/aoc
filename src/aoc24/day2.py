from __future__ import annotations
from aocd import get_data
from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class Report():
    levels: tuple[int, ...]

    @classmethod
    def from_line(cls, line: str) -> Report:
        return Report(levels=tuple([int(level) for level in line.split(" ")]))
    
    def is_save(self, has_problem_dampener: bool = False):
        def _is_save(levels: Sequence[int]) -> bool:
            diffs = [first_level - second_level for first_level, second_level in zip(levels, levels[1:])]
            # Return false if level diffs are not in range.
            if not all(map(lambda diff: 1 <= abs(diff) <= 3, diffs)):
                return False
            # Return true if diffs all go in the same direction.
            return len(set(map(lambda diff: diff < 0, diffs))) == 1
        
        if _is_save(self.levels):
            return True
        if not has_problem_dampener:
            return False
        
        possible_levels = [list(self.levels)[:i] + list(self.levels)[i+1:] for i in range(len(self.levels))]
        return any([_is_save(levels) for levels in possible_levels])

def solve_day2_part1() -> None:
    input = get_data(day=2, year=2024)
    lines = input.splitlines()
    num_save_reports = 0
    for line in lines:
        report = Report.from_line(line)
        if report.is_save():
            num_save_reports += 1
    print(num_save_reports)

def solve_day2_part2() -> None:
    input = get_data(day=2, year=2024)
    lines = input.splitlines()
    num_save_reports = 0
    for line in lines:
        report = Report.from_line(line)
        if report.is_save(has_problem_dampener=True):
            num_save_reports += 1
    print(num_save_reports)