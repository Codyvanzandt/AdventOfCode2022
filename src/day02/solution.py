def read_input():
    with open("src/day02/input.txt", "r") as input_file:
        return [ tuple(line.split()) for line in input_file.read().split("\n") ]

rps_rounds = read_input()

def score_round(result):
    return {
        ("A", "X") : 3 + 1,
        ("A", "Y") : 6 + 2,
        ("A", "Z") : 0 + 3,
        ("B", "X") : 0 + 1,
        ("B", "Y") : 3 + 2,
        ("B", "Z") : 6 + 3,
        ("C", "X") : 6 + 1,
        ("C", "Y") : 0 + 2,
        ("C", "Z") : 3 + 3,
    } [result]

def determine_sign(result):
    return {
        ("A", "X") : ("A", "Z"), 
        ("A", "Y") : ("A", "X"),
        ("A", "Z") : ("A", "Y"),
        ("B", "X") : ("B", "X"),
        ("B", "Y") : ("B", "Y"),
        ("B", "Z") : ("B", "Z"),
        ("C", "X") : ("C", "Y"),
        ("C", "Y") : ("C", "Z"),
        ("C", "Z") : ("C", "X"),
    }[result]

def part_one():
    return sum(map(score_round, rps_rounds))

def part_two():
    return sum(map(score_round, map(determine_sign, rps_rounds)))
