# after moving head, find tail within surrounding squares, move it if necessary

#    x -2 -1  0  1  2
#  y +---------------
# -2 |  x  .  .  .  x
# -1 |  .  x  x  x  .
#  0 |  .  x  H  x  .
#  1 |  .  x  x  x  .
#  2 |  x  .  .  .  x

# difference -> tail delta
# (-1, -2) -> ( 1,  1)
# ( 0, -2) -> ( 0,  1)
# ( 1, -2) -> (-1,  1)

# ( 2, -1) -> (-1,  1)
# ( 2,  0) -> (-1,  0)
# ( 2,  1) -> (-1, -1)

# ( 1,  2) -> (-1, -1)
# ( 0,  2) -> ( 0, -1)
# (-1,  2) -> ( 1, -1)

# (-2,  1) -> ( 1, -1)
# (-2,  0) -> ( 1,  0)
# (-2, -1) -> ( 1,  1)

# (-2, -2) -> ( 1,  1)
# ( 2, -2) -> (-1,  1)
# ( 2,  2) -> (-1, -1)
# (-2,  2) -> (1, -1)
from collections import defaultdict
from time import sleep
from utils.io import read

# add elementwise addition/sub operations with .+ to tuples you cowards
class Point(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return Point(*([sum(x) for x in zip(self, other)]))

    def __sub__(self, other):
        return self.__add__(-i for i in other)

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()


def direction(c: str) -> Point:
    match c:
        case "U":
            return Point(0, 1)
        case "D":
            return Point(0, -1)
        case "L":
            return Point(-1, 0)
        case "R":
            return Point(1, 0)
        case _:
            raise Exception("unknown direction", c)


differences_to_deltas = defaultdict(
    lambda: Point(0, 0),
    {
        Point(-1, -2): Point(1, 1),
        Point(0, -2): Point(0, 1),
        Point(1, -2): Point(-1, 1),
        Point(2, -1): Point(-1, 1),
        Point(2, 0): Point(-1, 0),
        Point(2, 1): Point(-1, -1),
        Point(1, 2): Point(-1, -1),
        Point(0, 2): Point(0, -1),
        Point(-1, 2): Point(1, -1),
        Point(-2, 1): Point(1, -1),
        Point(-2, 0): Point(1, 0),
        Point(-2, -1): Point(1, 1),
        Point(-2, -2): Point(1, 1),
        Point(2, -2): Point(-1, 1),
        Point(2, 2): Point(-1, -1),
        Point(-2, 2): Point(1, -1),
    },
)

tail_history_1 = defaultdict(int, {Point(0, 0): 1})
tail_history_2 = defaultdict(int, {Point(0, 0): 1})


def move(rope, direction, history):
    rope[0] += direction
    for i in range(1, len(rope)):
        rope[i] += differences_to_deltas[rope[i] - rope[i - 1]]

    history[rope[-1]] += 1


empty = [["." for _ in range(400)] for _ in range(400)]


rope1 = [Point(0, 0) for _ in range(2)]
rope2 = [Point(0, 0) for _ in range(10)]


# # map [-200, 200] -> [0, 400]
# from PIL import Image, ImageDraw


# def draw_rope(rope):
#     image = Image.new("RGB", (800, 800), "black")
#     draw = ImageDraw.Draw(image)

#     for x, y in tail_history_2.keys():
#         draw.rectangle(
#             (2 * x + 399, 2 * y + 399, 2 * x + 401, 2 * y + 401), fill="grey"
#         )

#     for (x, y) in rope:
#         draw.rectangle(
#             (2 * x + 399, 2 * y + 399, 2 * x + 401, 2 * y + 401), fill="white"
#         )

#     return image

# frames = []

input = read()
for line in input.splitlines():
    d, n = line.split(" ")
    d = direction(d)
    n = int(n)

    for _ in range(n):
        move(rope1, d, tail_history_1)
        move(rope2, d, tail_history_2)
        # frames.append(draw_rope(rope2))


print(len(tail_history_1))
print(len(tail_history_2))


# frame_one = frames[0]
# frame_one.save(
#     "worm.gif", format="GIF", append_images=frames, save_all=True, duration=20, loop=0
# )
