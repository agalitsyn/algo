import os

from utils import read_lines_from_file

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = os.getenv("DEBUG", False)


def part_1(data: list[str]) -> int:
    return 0


def part_2(data: list[str]) -> int:
    return 0


if __name__ == "__main__":
    file_path = os.path.join(CURRENT_DIR, "input.txt")
    if DEBUG:
        file_path = os.path.join(CURRENT_DIR, "example.txt")

    data = read_lines_from_file(file_path)

    res_1 = part_1(data)
    print("part 1:", res_1, "\n")

    res_2 = part_2(data)
    print("part 2:", res_2)
