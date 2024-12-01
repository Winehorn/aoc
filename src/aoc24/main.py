def solve_1_1(first_list: list[int], second_list: list[int]) -> None:
    first_list.sort()
    second_list.sort()
    result = sum([abs(first - second) for first, second in zip(first_list, second_list)])
    print("Day 1 Part 1")
    print(result)

if __name__ == "__main__":
    first_list = []
    second_list = []
    with open("/workspaces/aoc/data/1/1.txt", "r") as file:
        for line in file.readlines():
            points = line.split()
            first_list.append(int(points[0]))
            second_list.append(int(points[1]))
    solve_1_1(first_list, second_list)