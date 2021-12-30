from collections import namedtuple

class Rect:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def intersecting_rectangle(r1: Rect, r2: Rect):


    def is_intersecting(r1: Rect, r2: Rect):
        return r1.x + r1.width >= r2.x and r1.x <= r2.x + r2.width\
               and r1.y + r1.height >= r2.y and r1.y <= r2.y + r2.height

    if not is_intersecting(r1, r2):
        return Rect(0, 0, -1, -1)
    else:
        return Rect(
            max(r1.x, r2.x),
            max(r1.y, r2.y),
            min(r1.x+r1.width, r2.x+r2.width) - max(r1.x, r2.x),
            min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y)
        )

