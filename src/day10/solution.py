import math

def read_instructions():
    with open("src/day10/input.txt", "r") as input_file:
        for instruction in input_file.read().split("\n"):
            instruction_type, payload = instruction[:4], instruction[4:].strip()
            yield instruction_type, payload
            if instruction_type == "addx":
                yield "noop", ""

def compute_register_history():
    register_value = 1
    register_history = list()
    upcoming_instructions =  dict()
    for instruction_number, (instruction_type, payload) in enumerate(read_instructions()):
        # execute any updates
        if instruction_number in upcoming_instructions:
            register_value += upcoming_instructions[instruction_number]
            upcoming_instructions.pop(instruction_number)

        # log register history
        register_history.append(register_value)

        # begin the cycle
        if instruction_type == "noop":
            continue
        else:
            upcoming_instructions[instruction_number + 2] = int(payload)
    return register_history

def convert_register_to_pixel(cycle, register_value):
        sprite_positions = {register_value-1, register_value, register_value+1}
        if cycle in sprite_positions:
            return "#"
        else:
            return "."

def part_one():
    register_history = compute_register_history()
    return sum([ (cycle+1)*register_history[cycle] for cycle in range(19, register_history_size, 40) ])

def part_two():
    register_history = compute_register_history()
    rows = [ register_history[i:i+40] for i in range(0, len(register_history), 40) ]
    for _, row in enumerate(rows):
        for pixel_number, register_value in enumerate(row):
            yield convert_register_to_pixel(pixel_number, register_value)
        yield "\n"

print("".join(part_two()))



    