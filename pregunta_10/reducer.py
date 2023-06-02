#! /usr/bin python3

import sys

if __name__ == '__main__':
    dicc={}
    lista=[]

    for line in sys.stdin:        
        key, value = line.split("\t")[0],line.split("\t")[1]
        value = value.strip("\n")
        for v in value.split(","):
            dicc.setdefault(v,[]).append(int(key))

    for key in dicc:
        lista.append([key, sorted(dicc[key])])

    lista = sorted(lista, key=lambda x: x[0])

    for i in lista:
        sys.stdout.write("{}\t{}\n".format(i[0], ",".join([str(n) for n in i[1]])))