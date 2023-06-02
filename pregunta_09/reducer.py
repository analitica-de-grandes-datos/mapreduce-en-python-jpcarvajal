#! /usr/bin python3

import sys

if __name__ == '__main__':

    lines=[]
    for line in sys.stdin:        
        line=line.strip()
        line=line.split("\t")
        line[2]=int(line[2])
        lines.append(line)

    lines=sorted(lines,key=lambda x: (x[2]))
    for i in range(6):
        sys.stdout.write("{}   {}   {}\n".format(lines[i][0],lines[i][1], lines[i][2]))