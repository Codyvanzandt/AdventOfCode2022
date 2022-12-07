import re
from collections import defaultdict, namedtuple
from itertools import accumulate

def get_separate_commands():
    with open("src/day07/input.txt", "r") as input_file:
        commands = [ command.strip().replace("\n", " ") for command in re.split(r"\$", input_file.read()) if command ]
        return commands

def tokenize_commands():
    for command in get_separate_commands():
        if re.match(r"^cd .+$", command):
            yield  ("cd", re.search(r"^cd (.+)$", command).group(1) )
        elif re.match(r"^ls.+$", command):
            yield ("ls",) + tuple(re.findall(r"dir \S+|\d+ \S+", command))
        else:
            raise ValueError(f"Unexpected command: {command}")

def build_directory_structure():
    directory_structure = defaultdict(int)
    current_path = list()
    for command in tokenize_commands():
        if command[0] == "cd":
            _, directory = command
            if directory == "..":
                current_path.pop()
            else:
                current_path.append(directory)
                directory_structure[tuple(current_path)]
        elif command [0] == "ls":
            _, *contents = command
            for obj in contents:
                size, name = obj.split()
                if size == "dir":
                    continue
                else:
                    for path in accumulate(current_path):
                        directory_structure[ path] += int(size)
    return directory_structure

directory_sizes = build_directory_structure()
print(sum( directory_size for directory_size in directory_sizes.values() if directory_size <= 100000 ))
print(min(directory_size for directory_size in directory_sizes.values() if directory_size >= 30000000 - (70000000 - directory_sizes["/"])))