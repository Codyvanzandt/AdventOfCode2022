def read_elf_pairs():
    with open("src/day04/input.txt", "r") as input_file:
        for elf_pair in input_file.read().splitlines():
            elf1, elf2 = elf_pair.split(",")
            yield parse_elf_range(elf1), parse_elf_range(elf2)

def parse_elf_range(elf_range):
    start, stop = map(int, elf_range.split("-"))
    return range(start, stop)

def do_elves_fully_overlap(elf_range1, elf_range2):
    if (elf_range1.start <= elf_range2.start) and (elf_range1.stop >= elf_range2.stop):
        return True
    elif (elf_range2.start <= elf_range1.start) and (elf_range2.stop >= elf_range1.stop):
        return True
    else:
        return False

def do_elves_partially_overlap(elf_range1, elf_range2):
    if elf_range1.start <= elf_range2.stop <= elf_range1.stop:
        return True
    elif elf_range2.start <= elf_range1.stop <= elf_range2.stop:
        return True
    else:
        return False

def part_one():
    return sum( (do_elves_fully_overlap(*elves) for elves in read_elf_pairs()) )

def part_two():
    return sum( (do_elves_partially_overlap(*elves) for elves in read_elf_pairs()) )