import re


def get_puzzle():
    with open("src/day05/input.txt", "r") as input_file:
        crate_state_string, procecure_string = input_file.read().split("\n\n")
        return crate_state_string, procecure_string


def parse_crate_state(crate_state_string):
    stacks = [
        [stack[i : i + 4].strip() for i in range(0, len(stack), 4)] for stack in reversed(crate_state_string.split("\n"))
    ]
    return stacks[1:]


def parse_procedure(procecure_string):
    for line in procecure_string.split("\n"):
        numbers = re.findall(r"move (\d+) from (\d+) to (\d+)", line)
        yield from numbers


def create_stack_state(stacks):
    stack_state = {i: list() for i in range(10)}
    for stack in stacks:
        for i, stack_value in enumerate(stack):
            if stack_value:
                stack_state[i + 1].append(stack_value)
    return stack_state


def part_one():
    crate_state_string, procedure_string = get_puzzle()
    crate_state = create_stack_state(parse_crate_state(crate_state_string))
    procedure_numbers = parse_procedure(procedure_string)
    for (number_to_move, move_from, move_to) in procedure_numbers:
        for _ in range(int(number_to_move)):
            crate = crate_state[int(move_from)].pop()
            crate_state[int(move_to)].append(crate)
    return "".join(crate_stack[-1] for crate_stack in crate_state.values() if crate_stack)


def part_two():
    crate_state_string, procedure_string = get_puzzle()
    crate_state = create_stack_state(parse_crate_state(crate_state_string))
    procedure_numbers = parse_procedure(procedure_string)
    for (number_to_move, move_from, move_to) in procedure_numbers:
        for i in range(-int(number_to_move), 0, 1):
            crate = crate_state[int(move_from)].pop(i)
            crate_state[int(move_to)].append(crate)
    return "".join(crate_stack[-1] for crate_stack in crate_state.values() if crate_stack)