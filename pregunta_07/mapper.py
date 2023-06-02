#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line = line.split("   ") 
        line[2]=line[2].strip("\n").strip("\t")
        sys.stdout.write("{}\t{}\t{}\n".format(line[0],line[2], line[1]))