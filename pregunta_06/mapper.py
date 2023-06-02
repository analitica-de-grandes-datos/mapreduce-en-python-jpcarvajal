#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line = line.split("   ")       
        sys.stdout.write("{}\t{}".format(line[0],line[2]))