#!/usr/bin/python

import sys

from NFA import *
from Regex import *

if __name__ == "__main__":
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[2], "w")

    (regex, nfa) = prenexParse(fin.readline().strip().split())
    fin.close()

    fout.write(nfa.NFAtoDFA())
    fout.close()
