import re
import math
from collections import deque

class Monkey:
    def __init__(self, monkey_number, items, operation, test, true_monkey, false_monkey):
        self.monkey_number = monkey_number
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.tossed_item = 0

    def inspect_item(self):
        return self.items.popleft()

    def calculate_worry_level(self, item, special_modulus=None):
        worry_level = eval(self.operation, {}, {"old":item})
        return worry_level if special_modulus is None else worry_level % special_modulus

    def find_target_monkey(self, worry_level):
        if worry_level % self.test == 0:
            return self.true_monkey
        else:
            return self.false_monkey

def read_monkeys():
    with open("src/day11/input.txt", "r") as input_file:
        for monkey_number, monkey_data in enumerate(input_file.read().split("\n\n")):
            _, items, operation, test, if_true, if_false = monkey_data.split("\n")
            items = deque(int(item) for item in re.findall(r"\d+", items))
            operation = operation.split("= ")[1]
            test = int(re.search(r"\d+", test).group(0))
            true_monkey = int(re.search("\d+", if_true).group(0))
            false_monkey = int(re.search("\d+", if_false).group(0))
            yield Monkey(monkey_number, items, operation, test, true_monkey, false_monkey)

def perform_keep_away(rounds=1):
    monkeys = list(read_monkeys())
    special_modulus = math.prod(monkey.test for monkey in monkeys)
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.inspect_item()
                monkey.tossed_item += 1
                worry_level = monkey.calculate_worry_level(item, special_modulus)
                target_monkey = monkeys[monkey.find_target_monkey(worry_level)]
                target_monkey.items.append(worry_level)
    return monkeys

def moneky_solver():
    monkeys = perform_keep_away(rounds=10000)
    monkey_tosses = sorted(list((monkey.tossed_item for monkey in monkeys)), reverse=True)
    return math.prod(monkey_tosses[:2])