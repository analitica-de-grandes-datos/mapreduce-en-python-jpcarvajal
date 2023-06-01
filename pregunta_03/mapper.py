#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line=line.strip()
        sys.stdout.write("{},{}\n".format(line.split(",")[1],line.split(",")[0]))