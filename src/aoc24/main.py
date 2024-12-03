from collections import Counter
import day3

def solve_1_1(first_list: list[int], second_list: list[int]) -> None:
    first_list.sort()
    second_list.sort()
    result = sum([abs(first - second) for first, second in zip(first_list, second_list)])
    print("Day 1 Part 1")
    print(result)

def solve_1_2(first_list: list[int], second_list: list[int]) -> None:
    first_list_counter = Counter(first_list)
    second_list_counter = Counter(second_list)

    similarity_score = 0

    for list_number in first_list_counter:
        similarity_score += list_number * first_list_counter[list_number] * second_list_counter[list_number]
    print("Day 2 Part 2")
    print(similarity_score)
    
if __name__ == "__main__":
    day3.solve_part1()