from functools import cmp_to_key


def compare(left, right, level=0):
    match (left, right):
        case ([], []):
            return None
        case ([], [_, *_]):
            return -1
        case ([_, *_], []):
            return 1
        case ([l, *l_rest], [r, *r_rest]):
            match (l, r):
                case (int(l), int(r)):
                    if l < r:
                        return -1
                    if l > r:
                        return 1

                    return compare(l_rest, r_rest, level + 1)

                case (list(l), list(r)):
                    ans = compare(l, r, level + 1)
                    if ans is not None:
                        return ans
                    return compare(l_rest, r_rest, level + 1)

                case (int(l), list(r)):
                    ans = compare([l], r, level + 1)
                    if ans is not None:
                        return ans
                    return compare(l_rest, r_rest, level + 1)

                case (list(l), int(r)):
                    ans = compare(l, [r], level + 1)
                    if ans is not None:
                        return ans
                    return compare(l_rest, r_rest, level + 1)

        case _:
            raise Exception("unhandled case!", left, right)


def run(input):
    groups = input.split("\n\n")

    total = 0
    for i, group in enumerate(groups, 1):
        left, right = group.splitlines()

        # this is fine
        left = eval(left)
        right = eval(right)

        if compare(left, right) == -1:
            total += i

    print(total)

    evaled = [eval(line) for line in input.splitlines() if line] + [[[2]], [[6]]]
    ordered = sorted(evaled, key=cmp_to_key(compare))
    print((ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1))


if __name__ == "__main__":
    with open("input/day13.txt") as f:
        input = "".join(f.readlines())

    run(input)
