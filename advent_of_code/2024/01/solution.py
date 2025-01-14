import os

from utils import read_lines_from_file

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = os.getenv("DEBUG", False)


def part_1(data: list[str]) -> int:
    left_sorted: list[int] = []
    right_sorted: list[int] = []
    for line in data:
        num1, num2 = line.split()
        left_sorted.append(int(num1))
        right_sorted.append(int(num2))
    left_sorted.sort()
    right_sorted.sort()

    res = 0
    for idx, left in enumerate(left_sorted):
        right = right_sorted[idx]
        curr_res = abs(left - right)
        if DEBUG:
            print(left, right, curr_res)
        res += curr_res
    return res


def part_2(data: list[str]) -> int:
    left_data: list[int] = []
    right_data: list[int] = []

    for line in data:
        num1, num2 = line.split()
        left_data.append(int(num1))
        right_data.append(int(num2))

    res = 0
    for l in left_data:
        right_data_with_score: dict[int, int] = {}
        for r in right_data:
            if l == r:
                if r not in right_data_with_score:
                    right_data_with_score[l] = 1
                    continue
                right_data_with_score[l] += 1
        if DEBUG:
            print(right_data_with_score)

        if l in right_data_with_score:
            score = right_data_with_score[l]
            res += l * score
    return res


if __name__ == "__main__":
    file_path = os.path.join(CURRENT_DIR, "input.txt")
    if DEBUG:
        file_path = os.path.join(CURRENT_DIR, "example.txt")
    data = read_lines_from_file(file_path)
    res_1 = part_1(data)
    print("part 1:", res_1)
    res_2 = part_2(data)
    print("part 2:", res_2)
