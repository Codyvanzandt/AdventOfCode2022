def read_elf_pairs():
    with open("src/day04/input.txt", "r") as input_file:
        for elf_pair in input_file.read().splitlines():
            elf1, elf2 = elf_pair.split(",")
            yield parse_elf_range(elf1), parse_elf_range(elf2)


def parse_elf_range(elf_range):
    start, stop = map(int, elf_range.split("-"))
    return set(range(start, stop+1))


def do_elves_fully_overlap(elf_range1, elf_range2):
    return elf_range1.issubset(elf_range2) or elf_range2.issubset(elf_range1)

def do_elves_partially_overlap(elf_range1, elf_range2):
    return not elf_range1.isdisjoint(elf_range2)


def part_one():
    return sum((do_elves_fully_overlap(*elves) for elves in read_elf_pairs()))


def part_two():
    return sum((do_elves_partially_overlap(*elves) for elves in read_elf_pairs()))