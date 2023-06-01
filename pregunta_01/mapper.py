#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:

        sys.stdout.write("{}\t1\n".format(line.split(",")[2]))