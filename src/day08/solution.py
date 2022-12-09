from pprint import pprint
import math

def get_trees():
    with open("src/day08/input.txt", "r") as input_file:
        return [ 
            [int(val) for val in row]
            for row in input_file.read().split("\n") 
            ]

def get_view_lines_to_tree(trees, tree_i, tree_j):
    column = [ other_tree for other_i, other_tree in enumerate(trees[tree_i])]
    row = [ other_tree for other_i, other_tree in enumerate(list(zip(*trees))[tree_j])]
    left, right = column[:tree_j], column[tree_j+1:]
    top, bottom = row[:tree_i], row[tree_i+1:]
    return left, list(reversed(right)), top, list(reversed(bottom))

def compute_scenic_score(trees, tree_i, tree_j):
    view_distances = []
    tree_height = trees[tree_i][tree_j]
    view_lines = map(reversed, get_view_lines_to_tree(trees, tree_i, tree_j))
    for view_line in view_lines:
        view_distance = 0
        for other_tree_height in view_line:
            view_distance += 1
            if other_tree_height >= tree_height:
                break
        view_distances.append(view_distance)
    return math.prod(view_distances)

def part_one(trees):
    visible_trees = 0
    for tree_i, tree_row in enumerate(trees):
        for tree_j, tree in enumerate(tree_row):
            tree_view_lines = get_view_lines_to_tree(trees, tree_i, tree_j)
            if any( all(tree > other_tree for other_tree in tree_line) for tree_line in tree_view_lines ):
                visible_trees += 1
    return visible_trees

def part_two(trees):
    n_columns, n_rows = len(trees), len(trees[0])
    return max([ compute_scenic_score(trees, i, j ) for i in range(n_columns) for j in range(n_rows) ])

trees = get_trees()
print(part_two(trees))