#! /usr/bin python3

import sys
import math

if __name__ == '__main__':

    curkey = None

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            if val > max:
            
                max = val
            
            if val < min:

                min = val

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))

            curkey = key
            max = val
            min = val


    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))