from __future__ import annotations
from collections import deque
from functools import reduce
from operator import mul
from re import search, MULTILINE
from typing import Deque, List


class Monkey:
    def __init__(self, items: Deque[int], operation: function, test: function) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0

    def turn(self, other_monkeys: List[Monkey], divide: bool = True):
        while self.items:
            item = self.items.popleft()
            item = self.inspect(item)
            if divide:
                item = item // 3
            index = self.test(item)
            item = item % 9699690
            other_monkeys[index].throw(item)

    def inspect(self, item):
        self.inspected += 1
        return self.operation(item)

    def throw(self, item):
        self.items.append(item)

    def __str__(self) -> str:
        return f"items:{self.items}, inspected:{self.inspected}"

    def __repr__(self) -> str:
        return self.__str__()


def parse(s: str) -> Monkey:
    items = deque(
        map(int, search(r"Starting items: (.*)$", s, MULTILINE).group(1).split(","))
    )
    operation = search(r"Operation: new = (.*)$", s, MULTILINE).group(1)
    divisor = int(search(r"Test: divisible by (.*)$", s, MULTILINE).group(1))
    if_true = int(search(r"If true: throw to monkey (.*)$", s, MULTILINE).group(1))
    if_false = int(search(r"If false: throw to monkey (.*)$", s, MULTILINE).group(1))

    return Monkey(
        items,
        lambda old: eval(operation),
        lambda x: if_true if x % divisor == 0 else if_false,
    )


def part1(input):
    run(input, 20, True)


def part2(input):
    run(input, 10000, False)


def run(input, rounds, divide=True):
    monkeys = []
    for group in input.split("\n\n"):
        monkeys.append(parse(group))

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.turn(monkeys, divide)

    print(reduce(mul, sorted(monkey.inspected for monkey in monkeys)[-2:]))


if __name__ == "__main__":
    with open("input/day11.txt") as f:
        input = "".join(f.readlines())

    part1(input)
    part2(input)
