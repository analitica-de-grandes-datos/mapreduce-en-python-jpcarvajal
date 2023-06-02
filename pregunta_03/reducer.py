#! /usr/bin python3

import sys

if __name__ == '__main__':
     
    dicc={}

    for line in sys.stdin:        
        key, value = line.split(" ")
        sys.stdout.write("{},{}\n".format(line.split(",")[1],line.split(",")[0]))