#! /usr/bin python3

import sys

if __name__ == '__main__':

    curkey = None
    max = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:

            if val > max:
            
                max = val

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, max))

            curkey = key
            max = 0

    sys.stdout.write("{}\t{}\n".format(curkey, max))