import os
import re

from utils import read_lines_from_file

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = os.getenv("DEBUG", False)


def part_1(data: list[str]) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, "".join(data))
    result = sum(int(x) * int(y) for x, y in matches)
    return result


def part_2(data: list[str]) -> int:
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, "".join(data))

    enabled = True
    result = 0

    for inst in instructions:
        match inst[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                result += int(inst[1]) * int(inst[2])

    return result


if __name__ == "__main__":
    file_path = os.path.join(CURRENT_DIR, "input.txt")
    if DEBUG:
        file_path = os.path.join(CURRENT_DIR, "example.txt")

    data = read_lines_from_file(file_path)

    res_1 = part_1(data)
    print("part 1:", res_1, "\n")

    res_2 = part_2(data)
    print("part 2:", res_2)
