import os

from lib import read_lines_from_file

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = os.getenv("DEBUG", False)


def part_1(data: list[str]) -> int:
    safe_reports = 0
    for line in data:
        items = [int(v) for v in line.split()]
        increasing = items[0] < items[1]
        decreasing = items[0] > items[1]
        if DEBUG:
            print(items, "increasing:", increasing, "decreasing:", decreasing)

        if increasing or decreasing:
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
                    # means there is no sense to continue, this lline is not valid
                    break

                prev = i

            if DEBUG:
                print(verdict, "\n")
            if verdict:
                safe_reports += 1

    return safe_reports


def part_2(data: list[str]) -> int:
    return 0


if __name__ == "__main__":
    file_path = os.path.join(CURRENT_DIR, "input.txt")
    if DEBUG:
        file_path = os.path.join(CURRENT_DIR, "example.txt")

    data = read_lines_from_file(file_path)

    res_1 = part_1(data)
    print("part 1:", res_1)

    res_2 = part_2(data)
    print("part 2:", res_2)
