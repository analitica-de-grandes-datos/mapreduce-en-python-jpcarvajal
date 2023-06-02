#! /usr/bin python3

import sys

if __name__ == '__main__':

    curkey = None
    suma=0
    cnt=0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            
            suma+=val
            cnt+=1

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/cnt))

            curkey = key
            suma = val
            cnt = 1


    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/cnt))