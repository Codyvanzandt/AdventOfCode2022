
def read_input():
    with open("src/day06/input.txt", "r") as input_file:
        return input_file.read()

def find_n_sequential_uniques(datastream, n):
    datastream = read_input()
    for i in range(len(datastream)):
        if len(set(datastream[i:i+n])) == n:
            return i+n

def part_one():
    return find_n_sequential_uniques(read_input(), 4)

def part_two():
    return find_n_sequential_uniques(read_input(), 14)