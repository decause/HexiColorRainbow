from colorlab import Color, color_range, ashex


def colors():
    #
    x = list(color_range(Color(255, 255, 255), Color(0, 0, 0), 3))
    print x.ashex()
