from collections import deque
from functools import cmp_to_key


def get_list_pairs():
    with open("src/day13/input.txt", "r") as input_file:
        pairs = input_file.read().split("\n\n")
        for pair in pairs:
            a, b = pair.split("\n")
            yield ((eval(a)), (eval(b)))


def evaluate_pair(a, b):
    match a, b:
        case int(), int():
            if a == b:
                return None
            else:
                return a < b
        case int(), list():
            return evaluate_pair([a], b)
        case list(), int():
            return evaluate_pair(a, [b])
        case list(), list():
            for a_i, b_i in zip(a, b):
                if (z := evaluate_pair(a_i, b_i)) is not None:
                    return z
            return evaluate_pair(len(a), len(b))


def part_one():
    pairs = get_list_pairs()
    return sum((i + 1 for i, (a, b) in enumerate(pairs) if evaluate_pair(a, b)))


def part_two():
    decode_1, decode_2 = [[2]], [[6]]
    pairs = [packet for pair in get_list_pairs() for packet in pair] + [
        decode_1,
        decode_2,
    ]
    comparator = lambda a, b: 1 if evaluate_pair(a, b) else -1
    sorted_packets = sorted(pairs, key=cmp_to_key(comparator), reverse=True)
    return (sorted_packets.index(decode_1) + 1) * (sorted_packets.index(decode_2) + 1)
