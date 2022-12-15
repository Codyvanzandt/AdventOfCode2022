from itertools import pairwise

def get_rock_lines():
    with open("src/day14/test.txt", "r") as input_file:
        for line in input_file.read().split("\n"):
            yield [ tuple(map(int, point.split(","))) for point in line.split(" -> ") ]

class Cave:
    def __init__(self, rock_lines):
        self.rocks = {(500,0)}
        self.sand = set()
        for rock_line in rock_lines:
            self.add_rock_line(rock_line)
        self.dimensions = self.get_dimensions()

    def simulate_sandfall(self):
        sand = 0
        while self.add_sand():
            sand += 1
        return sand

    def add_sand(self):
        status, sand_coords = self.find_sand_coordinates(500, 0)
        if status:
            self.sand.add(sand_coords)
            return True
        else:
            return False

    def find_sand_coordinates(self, x, y):
        if self.sand_falls_off(x, y):
            return False, (None, None)
        if self.is_open(x, y+1):
            return self.find_sand_coordinates(x, y+1)
        elif self.is_open(x-1, y+1):
            return self.find_sand_coordinates(x-1, y+1)
        elif self.is_open(x+1, y+1):
            return self.find_sand_coordinates(x+1, y+1)
        return True, (x,y)
        
    def is_open(self, x, y):
        return (x,y) not in self.rocks and (x,y) not in self.sand

    def sand_falls_off(self, x,y):
        (x_min, x_max), (y_min, y_max) = self.dimensions 
        return not (y_min <= y <= y_max)

    def add_rock_line(self, rock_line):
        self.notate_rocks(rock_line)

    def notate_rocks(self, rock_line):
        for a, b in pairwise(rock_line):
            for point in self.interpolate_points(a, b):
                self.rocks.add(point)

    def draw(self):
        x_dim, y_dim = self.dimensions
        for y in range(y_dim[0], y_dim[1]+1):
            for x in range(x_dim[0], x_dim[1]+1):
                print("#" if (x,y) in self.rocks else "o" if (x,y) in self.sand else ".", end="")
            print("\n")
        print("\n")

    def get_dimensions(self):
        xs, ys = zip(*self.rocks)
        return (-float("inf"), float("inf")), (0, max(ys))
        

    @staticmethod
    def interpolate_points(a, b):
        is_line_vertical =  a[0] == b[0]
        fixed, *(a_var, b_var) = (a[0], a[1], b[1]) if is_line_vertical else (a[1], a[0], b[0])
        direction = 1 if b_var - a_var > 0 else - 1
        for i in range(a_var, b_var+direction, direction):
            yield (fixed, i) if is_line_vertical else (i, fixed)
            

c = Cave(get_rock_lines())

print(c.simulate_sandfall())