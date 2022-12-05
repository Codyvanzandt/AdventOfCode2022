from string import ascii_lowercase, ascii_uppercase

PRIORITY_DICT = dict(zip(ascii_lowercase, range(1, 27))) | dict(
    zip(ascii_uppercase, range(27, 53))
)


def read_input():
    with open("src/day03/input.txt", "r") as input_file:
        for rucksack in input_file.readlines():
            compartment1, compartment2 = (
                rucksack[: len(rucksack) // 2],
                rucksack[len(rucksack) // 2 :],
            )
            yield (set(compartment1), set(compartment2))


def find_priority(item):
    return PRIORITY_DICT[item]


def part_one():
    return sum(
        find_priority(next(iter(compartment1.intersection(compartment2))))
        for compartment1, compartment2 in read_input()
    )


def part_two():
    rucksacks = [
        compartment1 + compartment2.strip()
        for compartment1, compartment2 in read_input()
    ]
    groups_of_three = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    badges = [next(iter(set.intersection(*a))) for a in groups_of_three]
    return sum(map(find_priority, badges))
