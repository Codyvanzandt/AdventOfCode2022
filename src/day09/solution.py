from itertools import product
from copy import copy

def get_sign(x):
    return 1 if x>0 else -1 if x<0 else 0

class Snake:
    def __init__(self, max_segments):
        self.segments = [ Rope() ]
        self.max_segments = max_segments
        self.tail_visited_spaces = set()

    def __repr__(self):
        return f"Snake({self.segments})"

    def move_snake(self, x, y):

        self.tail_visited_spaces.add( tuple(self.segments[-1].tail) )

        for segment in self.segments:
            segment.move_head(x, y)
            if not segment.did_tail_move:
                break
        if (last_segment := self.segments[-1]).did_tail_move:
            if len(self.segments) < self.max_segments:
                self.segments.append(Rope(head=last_segment.old_tail, tail=last_segment.old_tail))

class Rope:

    def __init__(self, head=None, tail=None):
        self.head = [0,0] if head is None else list(head)
        self.tail = [0,0] if tail is None else list(tail)
        self.tail_visited_spaces = { (0,0) }
        self.did_tail_move = False
        self.old_tail = self.tail

    def __repr__(self):
        return f"Rope({self.head}, {self.tail})"

    def move_head(self, x, y):
        self.move_rope_end(self.head, x, y)
        if not self.head_and_tail_sufficiently_close():
            self.old_tail = copy(self.tail)
            self.did_tail_move = True
            self.move_tail(*self.find_tail_move())
            self.tail_visited_spaces.add(tuple(self.tail))
        else:
            self.did_tail_move = False
        return self

    def find_tail_move(self):
        x,y = self.head[0] - self.tail[0], self.head[1] - self.tail[1]
        match (x,y):
            case(x, 0):
                return (x-1, 0) if x > 0 else (x+1, 0)
            case (y, 0):
                return (y-1, 0) if y > 0 else (y+1, 0)
            case (x, y):
                return (get_sign(x), get_sign(y))

    def move_tail(self, x, y):
        return self.move_rope_end(self.tail, x, y)

    def move_rope_end(self, rope_end, x, y):
        rope_end[0] += x
        rope_end[1] += y
        return self

    def head_and_tail_sufficiently_close(self):
        spaces_adjacent_to_head = { (self.head[0] + x, self.head[1] + y) for x,y in product((0,1,-1),(0,1,-1)) }
        return tuple(self.tail) in spaces_adjacent_to_head


def convert_input_to_single_moves():
    with open("src/day09/test.txt", "r") as input_file:
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

def part_one():
    rope = Rope()
    for head_move in convert_input_to_single_moves():
        rope.move_head(*head_move)
    return len(rope.tail_visited_spaces)

def part_two():
    snake = Snake(9)
    for head_move in convert_input_to_single_moves():
        snake.move_snake(*head_move)

    print(snake.segments[0])
    print(visualize_results(snake))
    return len(snake.tail_visited_spaces)

def visualize_results(snake):
    xs, ys = zip(*snake.tail_visited_spaces)
    max_x, max_y = max(map(abs,xs)), max(map(abs,ys))
    snake_map = [ ["." for _ in range(2*max_x)] for _ in range(2*max_y) ]
    for (x,y) in snake.tail_visited_spaces:
        snake_map[x][y] = "#"
    return "\n".join( "".join(row) for row in snake_map )

print(part_two())