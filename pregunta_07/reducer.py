#! /usr/bin python3

import sys

if __name__ == '__main__':

    lines=[]
    for line in sys.stdin:        
        line=line.strip()
        line=line.split("\t")
        line[1]=int(line[1])
        lines.append(line)

    lines=sorted(lines,key=lambda x: (x[0],x[1]))
    for line in lines:
        sys.stdout.write("{}   {}   {}\n".format(line[0],line[2], line  [1]))