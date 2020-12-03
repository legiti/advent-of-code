import os
import math

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'pearson_input.txt')


def get_tree_count_pt_1():
    line_count = 0
    tree_count = 0
    with open(input_path) as f:
        for line in f:
            path = (3 * line_count) % 31
            if line[path] == '#':
                print(f'hit a tree at index {path} in {line}')
                tree_count = tree_count + 1
            line_count = line_count + 1
    return tree_count


def get_tree_count_pt_2():
    line_count = 0
    down_1_routes = {'1': 0, '3': 0, '5': 0, '7': 0}
    tree_count_down_2 = 0
    with open(input_path) as f:
        for line in f:
            if line_count % 2 == 0:
                path = int((line_count / 2) % 31)
                if line[path] == '#':
                    tree_count_down_2 = tree_count_down_2 + 1
            for route in down_1_routes.keys():
                path = (int(route) * line_count) % 31
                if line[path] == '#':
                    print(f'hit a tree at index {path} in {line} for route {route}')
                    down_1_routes[route] = down_1_routes[route] + 1
            line_count = line_count + 1
    tree_counts = list(down_1_routes.values())
    tree_counts.append(tree_count_down_2)
    print(tree_counts)
    print(tree_count_down_2)
    return math.prod(tree_counts)



tree_count_pt_1 = get_tree_count_pt_1()
print(f'woulda hit {tree_count_pt_1} trees in part 1')

tree_count_pt_2 = get_tree_count_pt_2()
print(f'product of trees hit in part 2 is {tree_count_pt_2}')
