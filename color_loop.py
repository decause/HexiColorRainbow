#!/usr/bin/env python
# author: Ralph Bean <ralph.bean@gmail.com>

step = 8
# step = 1  # for finer resolution in the color-space
bitspan = lambda: range(0, 255, step)


def print_color(r, g, b):
    print "%.2x%.2x%.2x" % (r, g, b)

# You could do this one way, by generating every single combination of red,
# green, and blue like this
for r in bitspan():
    for g in bitspan():
        for b in bitspan():
            print_color(r, g, b)

# Or you could write it tightly with the following.  This outputs the same
# thing as the above four-line block.
from itertools import product
for r, g, b in product(bitspan(), bitspan(), bitspan()):
    print_color(r, g, b)
