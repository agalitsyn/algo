MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


# iterate line by line
# parse game, get max values for each color, like {id red green blue }
# compare with task values and sum ID
def part1() -> None:
    res = 0
    with open("input.txt", "r") as f:
        for line in f:
            parts = line.split(":")
            print(f"DEBUG: {parts[0]}")

            title_parts = parts[0].split("Game")
            game_id = title_parts[1].strip()

            red_ok = False
            green_ok = False
            blue_ok = False

            red_scores = []
            green_scores = []
            blue_scores = []

            takes = [t.strip() for t in parts[1].split(";")]
            for t in takes:
                scores = [s.strip() for s in t.split(",")]
                for s in scores:
                    amount, color = [x for x in s.split(" ")]
                    amount = int(amount)
                    if color == "red":
                        red_scores.append(amount)
                    elif color == "green":
                        green_scores.append(amount)
                    elif color == "blue":
                        blue_scores.append(amount)

            print(f"DEBUG: max_red_scores: {max(red_scores)}")
            print(f"DEBUG: max_green_scores: {max(green_scores)}")
            print(f"DEBUG: max_blue_scores: {max(blue_scores)}")

            if max(red_scores) <= MAX_RED:
                red_ok = True
            if max(green_scores) <= MAX_GREEN:
                green_ok = True
            if max(blue_scores) <= MAX_BLUE:
                blue_ok = True

            print(f"DEBUG: red_ok: {red_ok}")
            print(f"DEBUG: green_ok: {green_ok}")
            print(f"DEBUG: blue_ok: {blue_ok}")

            if red_ok and green_ok and blue_ok:
                print(f"Game {game_id} is ok")
                res += int(game_id)

            print("=" * 80)

    print(res)


def part2():
    power = 0
    with open("input.txt", "r") as f:
        for game in f:
            game = game.split(": ")[1]
            max_number = {"red": 0, "green": 0, "blue": 0}
            for hand in game.split("; "):
                for subset in hand.split(", "):
                    n, color = subset.split()
                    max_number[color] = max(int(n), max_number[color])

            power += max_number["red"] * max_number["green"] * max_number["blue"]
    print(power)


if __name__ == "__main__":
    part1()
    part2()
