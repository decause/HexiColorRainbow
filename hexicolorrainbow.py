#!/usr/bin/python
from colorlab import Color, color_range
from fabulous.color import *


print 'The hexicolor rainbow'
# Here we use color lab to generate a range of colors (in rgb format)
# we pass in Beginning Color, End Color, and how many values you'd like in the
# range Ultimately, there are 16 Million colors, and I'm not sure how my box
# will handle generating that many... we'll find out
# colors = list(color_range(Color(255, 255, 255), Color(0, 0, 0), 16000000))
colors = list(color_range(Color(255, 255, 255), Color(0, 0, 0), 13))

# Create a file called 'hexcodes.txt' to write each hex value to
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

for color in colors:
    print color

for code in ["highlight256((255, 0, 0), ' lorem ipsum ')"]:
    print "hex colors " + "%-42s %s" % (code, eval(code))

for code in ["bold(fg256('red', ' lorem ipsum '))",
             "bold(bg256('#ff0000', ' lorem ipsum '))",
             "highlight256((255, 0, 0), ' lorem ipsum ')",
             "highlight256('#09a', ' lorem ipsum ')",
             "highlight256('green', ' lorem ipsum ')",
             "highlight256('magenta', ' lorem ipsum ')",
             "highlight256('indigo', ' lorem ipsum ')",
             "highlight256('orange', ' lorem ipsum ')",
             "highlight256('orangered', ' lorem ipsum ')"]:
    print "%-42s %s" % (code, eval(code))
print ''
