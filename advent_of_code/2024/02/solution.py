import os

from utils import read_lines_from_file

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = os.getenv("DEBUG", False)


def is_safe(items: list[int]) -> bool:
    increasing = items[0] < items[1]
    decreasing = items[0] > items[1]
    if not (increasing or decreasing):
        return False

    if DEBUG:
        print(
            "items",
            [x for x in items],
            "increasing",
            increasing,
            "decreasing",
            decreasing,
        )

    verdict = False
    prev = items[0]
    for i in items[1:]:
        verdict = False

        # filter out lines like `86441`
        if i == prev:
            break

        diff = abs(i - prev)
        if DEBUG:
            print(i, "prev =", prev, "diff =", diff)

        # check increasing and decreasing constantly and check adjacent levels
        if increasing and i > prev and diff >= 1 and diff <= 3:
            verdict = True
        elif decreasing and i < prev and diff >= 1 and diff <= 3:
            verdict = True
        else:
            # means there is no sense to continue, this line is not valid
            return False

        prev = i

    if DEBUG:
        print(verdict, "\n")
    return verdict


def part_1(data: list[str]) -> int:
    res = 0
    for line in data:
        items = [int(v) for v in line.split()]
        if is_safe(items):
            res += 1
    return res


def part_2(data: list[str]) -> int:
    res = 0
    for line in data:
        items = [int(v) for v in line.split()]
        if is_safe(items):
            res += 1
        else:
            for i in range(len(items)):
                extra = items[:i] + items[i + 1 :]
                if is_safe(extra):
                    res += 1
                    break

    return res


if __name__ == "__main__":
    file_path = os.path.join(CURRENT_DIR, "input.txt")
    if DEBUG:
        file_path = os.path.join(CURRENT_DIR, "example.txt")

    data = read_lines_from_file(file_path)

    res_1 = part_1(data)
    print("part 1:", res_1, "\n")

    res_2 = part_2(data)
    print("part 2:", res_2)
