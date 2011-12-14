#!/usr/bin/env python
#
# ..author: RemyD <remyd@civx.us>
from colorlab import Color, color_range
from fabulous.color import *


print 'The HexiColorRainbow'
# Here we use color lab to generate a range of colors (in rgb format)
# we pass in Beginning Color, End Color, and how many values you'd like in the
# range Ultimately, there are 16 Million colors, and I'm not sure how my box
# will handle generating that many... we'll find out
# colors = list(color_range(Color(255, 255, 255), Color(0, 0, 0), 16000000))
#
#
# This is complicated, as it will give you a range between 2 colors, but there
# are 3 ranges of numbers within those colors...
# I guess I could do all the combinations?
# The non-color range way would probably make more sense, creating hexcodes by hand
#
# white-> black
# colors = list(color_range(Color(255, 255, 255), Color(0, 0, 0), 255))
#
# reds
# colors = list(color_range(Color(255, 0, 0), Color(0, 0, 0), 255))
#
# greens
# colors = list(color_range(Color(0, 255, 0), Color(0, 0, 0), 255))
#
# blues
# colors = list(color_range(Color(0, 0, 255), Color(0, 0, 0), 255))
#
# red -> green
# red_green_colors = list(color_range(Color(255, 0, 0), Color(0, 255, 0), 13))
#
# red -> blue
# red_blue_colors = list(color_range(Color(255, 0, 0), Color(0, 0, 255), 13))
#
# green -> red
# green_red_colors = list(color_range(Color(0, 255, 0), Color(255, 0, 0), 13))
#
# green -> blue
# green_blue_colors = list(color_range(Color(0, 255, 0), Color(0, 0, 255), 13))
#
# blue -> red
# blue_red_colors = list(color_range(Color(0, 0, 255), Color(255, 0, 0), 13))
#
# blue -> green
# blue_green_colors = list(color_range(Color(0, 0, 255), Color(0, 255, 0), 13))
#
#
# TODO: Display the all inclusive hexidecimal sequence from 0-16777216
#
# TODO: Check each hexcode for a proper color name definition
#       If so, then print it out next to the hexcode, in the proper color
#
colors = list(color_range(Color(0, 255, 0), Color(0, 0, 0), 255))

# Create a file called 'hexcodes.txt' to record each hex value
f = open('hexcodes.txt', 'w')

# For each color in my list of colors...
for color in colors:
    # convert the rgb to hex
    hexcolor = color.ashex()
    # write the hex value to our hexcodes.txt file
    f.write(hexcolor + '\n')
    # print the hexcode, highlighted with the color it represents (awesome)
    for code in ["bold(bg256('#" + "%s" % hexcolor + "', ' " + "%s" %
                 hexcolor + " '))"]:
        print "hex colors " + "%-42s %s" % (code, eval(code))
f.close()

# Show the variety of ways fabulous will print for you
#for code in ["bold(fg256('red', ' lorem ipsum '))",
#             "bold(bg256('#ff0000', ' lorem ipsum '))",
#             "highlight256((255, 0, 0), ' lorem ipsum ')",
#             "highlight256('#09a', ' lorem ipsum ')",
#             "highlight256('orangered', ' lorem ipsum ')"]:
#    print "%-42s %s" % (code, eval(code))
#print ''

print "%s" % len(colors) + " Shades"
