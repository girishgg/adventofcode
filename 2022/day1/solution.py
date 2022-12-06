def read_file(filename: str) -> [str]:
    with open(filename, 'r') as file:
        return [[int(calory) for calory in calories.strip().split('\n')] for calories in file.read().strip().split("\n\n")]


def day1() -> (int, int):
    file = 'puzzle.txt'
    data = read_file(file)

    def part1(calories_by_elfs: [(int)]) -> {}:
        max_calories = [sum(calories) for calories in calories_by_elfs]
        max_calories.sort(reverse=True)

        return {'max_calories_list': max_calories, 'max': max_calories[0]}

    def part2(max_calories: [int]) -> int:
        return sum(max_calories[:3])

    part_1 = part1(data)

    return part_1['max'], part2(part_1['max_calories_list'])


if __name__ == "__main__":
    print("Part 1: %d, Part 2: %d" % day1())
