#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:
        mes=line.split("   ")[1][5:7]
        sys.stdout.write("{}\t1\n".format(mes))    