from string import ascii_lowercase, ascii_uppercase

PRIORITY_DICT = dict(zip(ascii_lowercase,range(1,27))) | dict(zip(ascii_uppercase,range(27,53)))

def read_input():
    with open("src/day03/test.txt", "r") as input_file:
        for rucksack in input_file.readlines():
            compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
            yield (compartment1, compartment2)

def find_priority(item):
    return PRIORITY_DICT[item]


def part_one():
    return sum(
        find_priority(next(iter(set(compartment1).intersection(set(compartment2))))) for compartment1, compartment2 in read_input()
    )