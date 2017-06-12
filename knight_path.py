# on a grid extending infinitely in ever direction,
# find the number a moves a knight takes to get to (x, y) from (0, 0)
# print a path of that length

def get_input():
    x, y = input("> ").split(" ")
    return [int(x), int(y)]

def possible_jumps(path):
    x, y = path[-1]
    return [
        path + [[x + 1, y + 2]],
        path + [[x - 1, y + 2]],
        path + [[x - 1, y - 2]],
        path + [[x + 1, y - 2]],
        path + [[x + 2, y + 1]],
        path + [[x + 2, y - 1]],
        path + [[x - 2, y + 1]],
        path + [[x - 2, y - 1]]
    ]

def checking_function(paths, dest):
    for path in paths:
        if path[-1] == dest:
            return path
    return False

def find_path(c_orig, c_dest):
    current_paths = [[c_orig]]
    squares_visited = [c_orig]
    while not checking_function(current_paths, c_dest):
        new_paths = []
        for path in current_paths:
            for p in possible_jumps(path):
                if p[-1] not in squares_visited:
                    squares_visited += [p[-1]]
                    new_paths += [p]
        current_paths += new_paths
    return checking_function(current_paths, c_dest)

coords = get_input()

solution = find_path([0, 0], coords)

print(f"Found a path of length {len(solution)}:")
print(solution)