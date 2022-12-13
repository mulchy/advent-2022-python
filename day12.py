from collections import deque
from typing import List


alphabet = "abcdefghijklmnopqrstuvwxyz"
height = {c: height for (height, c) in enumerate(alphabet, 1)}


def neighbors(grid: List[List[int]], point):
    x, y = point
    return [
        (x + i, y + j)
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if reachable(grid, (x, y), (x + i, y + j))
    ]


def in_bounds(grid: List[List[int]], point):
    x, y = point
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def reachable(grid, source, dest):
    source_x, source_y = source
    dest_x, dest_y = dest
    if not in_bounds(grid, dest):
        return False

    source_height = height[grid[source_y][source_x]]

    dest_height = height[grid[dest_y][dest_x]]
    return dest_height - source_height <= 1


def run(input: str, starting_locations):
    grid = []
    sources = []

    for y, line in enumerate(input.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c in starting_locations:
                sources.append((x, y))
                row.append("a")
            elif c == "E":
                dest = (x, y)
                row.append("z")
            else:
                row.append(c)
        grid.append(row)

    length = min(
        map(
            len,
            filter(
                lambda x: x is not None, [bfs(grid, source, dest) for source in sources]
            ),
        )
    )
    print(length)


def bfs(grid, source, dest):
    q = deque([])
    visited = set([source])
    q.append(source)

    previous = {}

    while q:
        v = q.pop()
        if v == dest:
            prev = previous[v]
            path = [prev]
            while prev != source:
                prev = previous[prev]
                path.append(prev)
            path.reverse()
            return path

        for n in neighbors(grid, v):
            if not n in visited:
                visited.add(n)
                previous[n] = v
                q.appendleft(n)


if __name__ == "__main__":
    with open("input/day12.txt") as f:
        input = "".join(f.readlines())

    run(input, ["S"])
    run(input, ["S", "a"])
