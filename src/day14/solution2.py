from itertools import pairwise


def get_rock_lines():
    with open("src/day14/test.txt", "r") as input_file:
        for line in input_file.read().split("\n"):
            yield [ tuple(map(int, point.split(","))) for point in line.split(" -> ") ]

def interpolate_points(a, b):
        is_line_vertical =  a[0] == b[0]
        fixed, *(a_var, b_var) = (a[0], a[1], b[1]) if is_line_vertical else (a[1], a[0], b[0])
        direction = 1 if b_var - a_var > 0 else - 1
        for i in range(a_var, b_var+direction, direction):
            yield (fixed, i) if is_line_vertical else (i, fixed)

def notate_rocks(self, rock_line):
        for a, b in pairwise(rock_line):
            for point in self.interpolate_points(a, b):
                yield point
                
def does_sand_fall_off(dimensions, x, y):
    (x_min, x_max), (y_min, y_max) = dimensions
    return (x_min <= x <= x_max) and (y_min <= y <= y_max)

class Cave:
    def __init__(self, rocks):
        self.rocks = rocks
        self.sand = set()
        self.dimensions = self.get_dimensions()

    def get_dimensions(self):
        xs, ys = zip(*self.rocks)
        return (min(xs), max(xs)), (0, max(ys))


rocks = get_rock_lines()
sand = set()