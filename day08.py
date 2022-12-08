from utils.io import read

input = read()

grid = []
for line in input.splitlines():
    row = []
    grid.append(row)
    for tree in line:
        row.append(int(tree))


def pprint_grid(grid, row=None, column=None):
    clear = "\033[2J"
    green = "\033[92m"
    red = "\033[91m"
    off = "\033[0m"

    height = len(grid)
    width = len(grid[0])

    print(clear, end=None)

    for i in range(height):
        for j in range(width):
            if i == row and j == column:
                print(f"{green}{grid[i][j]}{off}", end="")
            elif i == row or j == column:
                print(f"{red}{grid[i][j]}{off}", end="")
            else:
                print(grid[i][j], end="")
        print()


def look_left(grid, i, j):
    return [grid[i][col] for col in range(j - 1, -1, -1)]


def look_right(grid, i, j):
    width = len(grid[0])
    return [grid[i][col] for col in range(j + 1, width)]


def look_up(grid, i, j):
    return [grid[row][j] for row in range(i - 1, -1, -1)]


def look_down(grid, i, j):
    height = len(grid)
    return [grid[row][j] for row in range(i + 1, height)]


def count_visible_trees(grid) -> int:

    # iterate through interior of grid
    # at each point, look in all four directions
    # if in any direction all other trees are smaller, tree is visible

    height = len(grid)
    width = len(grid[0])

    visible_trees = 2 * width + 2 * height - 4

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            tree = grid[i][j]
            # pprint_grid(grid, i, j)

            visible = any(
                [
                    all(
                        True if other_tree < tree else False
                        for other_tree in look_left(grid, i, j)
                    ),
                    all(
                        True if other_tree < tree else False
                        for other_tree in look_right(grid, i, j)
                    ),
                    all(
                        True if other_tree < tree else False
                        for other_tree in look_up(grid, i, j)
                    ),
                    all(
                        True if other_tree < tree else False
                        for other_tree in look_down(grid, i, j)
                    ),
                ]
            )

            if visible:
                visible_trees += 1
    return visible_trees


print(count_visible_trees(grid))


def scenic_sore(grid, i, j) -> int:
    return (
        len(list(visible_trees(grid, i, j, look_left)))
        * len(list(visible_trees(grid, i, j, look_right)))
        * len(list(visible_trees(grid, i, j, look_up)))
        * len(list(visible_trees(grid, i, j, look_down)))
    )


def visible_trees(grid, i, j, fn):
    for other_tree in fn(grid, i, j):
        if other_tree <= grid[i][j]:
            yield other_tree
        if other_tree >= grid[i][j]:
            break


def scenic_scores(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield scenic_sore(grid, i, j)


def best_scenic_score(grid):
    return max(scenic_scores(grid))


print(best_scenic_score(grid))
