def read_input():
    with open("src/day01/input.txt", "r") as input_file:
        return [ [ int(food_item) for food_item in elf_sack.split("\n") ] for elf_sack in input_file.read().split("\n\n") ]

elf_sacks = read_input()

def part_one():
    return max(
        (sum(elf_sack) for elf_sack in elf_sacks)
        )

def part_two():
   return sum(
    list(sorted((sum(elf_sack) for elf_sack in elf_sacks ),reverse=True))[:3] 
        )