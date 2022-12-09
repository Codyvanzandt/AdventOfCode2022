from itertools import pairwise


def convert_input_to_single_moves():
    with open("src/day09/input.txt", "r") as input_file:
        for line in input_file.read().split("\n"):
            direction, distance = line.split()
            match (direction):
                case ("R"):
                    single_movement = (1, 0)
                case ("L"):
                    single_movement = (-1, 0)
                case ("U"):
                    single_movement = (0, 1)
                case ("D"):
                    single_movement = (0, -1)
            for _ in range(int(distance)):
                yield single_movement


def update_rope(rope, move):
    return rope[0] + move[0], rope[1] + move[1]


def update_tail(head, tail):
    tail_move = find_tail_move(head, tail)
    return update_rope(tail, tail_move)


def find_tail_move(head, tail):
    x, y = head[0] - tail[0], head[1] - tail[1]
    if abs(x) >= 2 or abs(y) >= 2:
        return (get_sign(x), get_sign(y))
    return (0, 0)


def get_sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def part_one():
    tail_visited_spaces = set()
    head, tail = (0, 0), (0, 0)
    for move in convert_input_to_single_moves():
        head = update_rope(head, move)
        tail = update_tail(head, tail)
        tail_visited_spaces.add(tail)
    return len(tail_visited_spaces)


def part_two():
    rope = [(0, 0) for _ in range(10)]
    tail_visited_spaces = set()
    for move in convert_input_to_single_moves():
        rope[0] = update_rope(rope[0], move)
        for i, j in pairwise(range(10)):
            head = rope[i]
            tail = rope[j]
            rope[j] = update_tail(head, tail)
        tail_visited_spaces.add(rope[-1])
    return len(tail_visited_spaces)
