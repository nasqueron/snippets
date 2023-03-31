#!/usr/bin/env python3

#   -------------------------------------------------------------
#   
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
import sys


#   -------------------------------------------------------------
#   Application entry point
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def run(foo):
    pass


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc < 2:
        print(f"Usage: {sys.argv[0]} <foo>", file=sys.stderr)
        sys.exit(1)

    run(sys.argv[1])
