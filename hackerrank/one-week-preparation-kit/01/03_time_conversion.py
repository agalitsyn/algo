#!/bin/python3

import os
from datetime import datetime


def timeConversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = timeConversion(s)
    fptr.write(result + "\n")
    fptr.close()
