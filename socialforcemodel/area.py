class Area:
    """ Area class for the Social Force Model.

    The area class is a rectangle defined by two x,y points and is used to
    define spawn and target areas in the Social Force Model.
    """

    def __init__(self, start, end):
        if start[0] > end[0]:
            temp = start[0]
            start[0] = end[0]
            end[0] = temp

        if start[1] > end[1]:
            temp = start[1]
            start[1] = end[1]
            end[1] = temp

        self.start = start
        self.end = end

    def height(self):
        """ Get the height (y-dimension) of the area. """
        return abs(self.end[1] - self.start[1])

    def width(self):
        """ Get the width (x-dimension) of the area. """
        return abs(self.end[0] - self.start[0])

    def in_area(self, position):
        return (position[0] >= self.start[0] and position[0] <= self.end[0] and
                position[1] >= self.start[1] and position[1] <= self.end[1])

    def get_closest_point(self, position):
        new_target = [0.0, 0.0]
        new_target[0] = min(max(position[0], self.start[0]), self.end[0])
        new_target[1] = min(max(position[1], self.start[1]), self.end[1])
        return new_target
