import string
import networkx
from collections import defaultdict, deque


def read_elevation_map():
    with open("src/day12/input.txt", "r") as input_file:
        return [list(row) for row in input_file.read().split("\n")]


def transform_map_to_numbers(elevation_map):
    elevation_dictionary = {"S": 0, "E": 25} | {
        letter: i for i, letter in enumerate(string.ascii_lowercase)
    }
    return [[elevation_dictionary[letter] for letter in row] for row in elevation_map]


def get_edges(elevation_map):
    max_rows, max_cols = len(elevation_map), len(elevation_map[0])
    for n_row, row in enumerate(elevation_map):
        for n_col, current_node_elevation in enumerate(row):
            adjacent_indices = (
                (n_row, n_col - 1),
                (n_row, n_col + 1),
                (n_row - 1, n_col),
                (n_row + 1, n_col),
            )
            for (other_row, other_col) in adjacent_indices:
                if 0 <= other_row < max_rows and 0 <= other_col < max_cols:
                    other_node_elevation = elevation_map[other_row][other_col]
                    if other_node_elevation - current_node_elevation <= 1:
                        yield (
                            (n_row, n_col),
                            (other_row, other_col),
                        )


def make_graph(elevation_map):
    return networkx.DiGraph(get_edges(transform_map_to_numbers(read_elevation_map())))


def get_start_and_end_indices(elevation_map):
    start, end = None, None
    for row_n, row in enumerate(elevation_map):
        for col_n, value in enumerate(row):
            if value == "S":
                start = (row_n, col_n)
            if value == "E":
                end = (row_n, col_n)
    return start, end


def shortest_path_length(graph, source, target):
    try:
        return bfs(graph, source)[target]
    except KeyError:
        return float("inf")


def bfs(g, source):
    to_visit = deque([source])
    distances = {source: 0}
    while to_visit:
        new_node = to_visit.popleft()
        for neighbor in g[new_node]:
            if neighbor not in distances:
                to_visit.append(neighbor)
                distances[neighbor] = distances[new_node] + 1
    return distances


def part_one():
    elevation_map = read_elevation_map()
    elevation_graph = make_graph(elevation_map)
    start, end = get_start_and_end_indices(elevation_map)
    return shortest_path_length(elevation_graph, start, end)


def part_two():
    paths = list()
    elevation_map = read_elevation_map()
    elevation_graph = make_graph(elevation_map)
    _, end = get_start_and_end_indices(elevation_map)
    starting_points = [
        (row, col)
        for row in range(len(elevation_map))
        for col in range(len(elevation_map[0]))
        if elevation_map[row][col] == "a"
    ]
    return min(
        [
            shortest_path_length(elevation_graph, starting_point, end)
            for starting_point in starting_points
        ]
    )


print(part_one())
print(part_two())
