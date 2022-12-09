from pprint import pprint
import math


def get_trees():
    with open("src/day08/input.txt", "r") as input_file:
        return [[int(val) for val in row] for row in input_file.read().split("\n")]


def get_view_lines_to_tree(trees, tree_i, tree_j):
    column = [other_tree for other_i, other_tree in enumerate(trees[tree_i])]
    row = [other_tree for other_i, other_tree in enumerate(list(zip(*trees))[tree_j])]
    left, right = column[:tree_j], column[tree_j + 1 :]
    top, bottom = row[:tree_i], row[tree_i + 1 :]
    return left, list(reversed(right)), top, list(reversed(bottom))


def get_view_lines_from_tree(trees, tree_i, tree_j):
    return [
        list(reversed(view_line))
        for view_line in get_view_lines_to_tree(trees, tree_i, tree_j)
    ]


def is_tree_visible(trees, tree_i, tree_j):
    tree_height = trees[tree_i][tree_j]
    tree_view_lines = get_view_lines_to_tree(trees, tree_i, tree_j)
    for view_line in tree_view_lines:
        if all(tree_height > other_tree_height for other_tree_height in view_line):
            return True
    return False


def compute_scenic_score(trees, tree_i, tree_j):
    view_distances = []
    tree_height = trees[tree_i][tree_j]
    for view_line in get_view_lines_from_tree(trees, tree_i, tree_j):
        current_view_distance = 0
        for other_tree_height in view_line:
            current_view_distance += 1
            if other_tree_height >= tree_height:
                break
        view_distances.append(current_view_distance)
    return math.prod(view_distances)


def part_one():
    trees = get_trees()
    all_tree_indices = ((i, j) for i in range(len(trees)) for j in range(len(trees[0])))
    visisble_trees = (is_tree_visible(trees, i, j) for (i, j) in all_tree_indices)
    return sum(visisble_trees)


def part_two():
    trees = get_trees()
    all_tree_indices = ((i, j) for i in range(len(trees)) for j in range(len(trees[0])))
    scenic_scores = (compute_scenic_score(trees, i, j) for (i, j) in all_tree_indices)
    return max(scenic_scores)
