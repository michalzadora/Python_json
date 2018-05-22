# Class for possible figures, I have to define inner classes for sample shapes.

# or {"type": "square", "x": 150, "y": 100, "size": 80, "color": "(255,255,255)"}
class Square:
    def __init__(self, cord_x, cord_y, side, colour):
        self.x = cord_x
        self.y = cord_y
        self.side = side
        self.colour = colour

    def __str__(self):
        return "Square has middle: [" + str(self.x) + ", " + str(self.y) + "] and side: " + str(self.r)


class Circle:
    def __init__(self, cord_x, cord_y, radius, colour):
        self.x = cord_x
        self.y = cord_y
        self.r = radius
        self.colour = colour

    def __str__(self):
        return "Circle has middle: [" + str(self.x) + ", " + str(self.y) + "] and radius: " + str(self.r)


# {"type": "rectangle", "x": 100, "y": 50, "width": 200, "height": 50}
class Rectangle:
    def __init__(self, cord_x, cord_y, width, height, colour):
        self.x = cord_x
        self.y = cord_y
        self.width = width
        self.height = height
        self.colour = colour

    def __str__(self):
        return "Rectangle has middle: [" + str(self.x) + ", " + str(self.y) + "], width: " + str(
            self.width) + " and height: " + str(self.height)


# {"type": "point", "x": 1, "y": 0}
class Point:
    def __init__(self, cord_x, cord_y, colour):
        self.x = cord_x
        self.y = cord_y
        self.colour = colour

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"


# {"type": "polygon", "points": [[2,5], [3,14], [5,18], [11,18], [3,39]], "color": "blue"}
class Polygon:
    def __init__(self, points=None, colour=None):  # points - lists of obj class Point.
        if points is None:
            self.points = []
        else:
            # point is list of cordinations in 2D
            self.points = []
            [self.points.append(Point(point[0], point[1], colour)) for point in points]
        self.colour = colour

    def __str__(self):
        return "Polygon points: " + str([str(point) for point in self.points])
