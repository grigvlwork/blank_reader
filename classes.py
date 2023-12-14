class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Area:
    def __init__(self, points=None):
        if points is None:
            points = set()
        self.points = points

    def get_width(self):
        if len(self.points) == 0:
            return 0
        return max(p.x for p in self.points) - min(p.x for p in self.points)

    def get_height(self):
        if len(self.points) == 0:
            return 0
        return max(p.y for p in self.points) - min(p.y for p in self.points)

    def add_point(self, x, y):
        self.points.add(Point(x, y))

    def near(self, x, y):
        for p in self.points:
            if abs(p.x - x) == 1 or abs(p.y - y) == 1:
                return True
        return False
