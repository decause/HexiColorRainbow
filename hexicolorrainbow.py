#!/usr/bin/env python
#
# ..author: RemyD <remyd@civx.us>
# ..author: Ralph Bean <ralph.bean@gmail.com>
from fabulous.color import bold, bg256

# Here we use a lamda to generate rgb bitspans from 0 to 255
# Here we use color lab to generate a range of colors (in rgb format)
# we pass in Beginning Color, End Color, and how many values you'd like in the
# range Ultimately, there are 16 Million colors, and I'm not sure how my box
# will handle generating that many... we'll find out

print 'The HexiColorRainbow'

step = 1
bitspan = lambda: range(0, 256, step)


def print_color(r, g, b):
    pad = '                                  '
    pad2 = '                                     '
    print bold(bg256('#%.2x%.2x%.2x' % (r, g, b), '%s' % pad + ' #%.2x%.2x%.2x ' % (r, g, b) + '%s' % pad2))


f = open('hexcodes-full.txt', 'w')


from itertools import product
for r, g, b in product(bitspan(), bitspan(), bitspan()):
    f.write("%.2x%.2x%.2x" % (r, g, b) + '\n')
    print_color(r, g, b)
    #import time
    #time.sleep(.1)
f.close()
