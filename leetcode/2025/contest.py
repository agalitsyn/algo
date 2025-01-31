import os
import random
from datetime import datetime

EXCLUDES = ["template"]


def scan_files(root_dir):
    py_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for exclude in EXCLUDES:
            if exclude in dirnames:
                dirnames.remove(exclude)

        for filename in filenames:
            if dirpath != "." and filename.endswith(".py"):
                py_files.append(os.path.join(dirpath, filename))

    return py_files


def main():
    solutions = scan_files(".")
    themes2files = {}
    for file_path in solutions:
        theme = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
        if theme not in themes2files:
            themes2files[theme] = []
        themes2files[theme].append(file_path)

    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    themes = list(themes2files.keys())
    random.shuffle(themes)
    for theme in themes[:3]:
        files = themes2files[theme]
        print(f"Theme: {theme}")
        print(f"File: {random.choice(files)}")
        print()


if __name__ == "__main__":
    main()
