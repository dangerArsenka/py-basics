#Introduction to programming: Task 3
#Tsadzikidze Arsen, FB-24, 26
print('Introduction to programming: Task 3')
print('Tsadzikidze Arsen, FB-24, 26')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"Vector: ({self.start_point.x}, {self.start_point.y}) -> ({self.end_point.x}, {self.end_point.y})"

    def length(self):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def multiply(self, scalar):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        new_dx = dx * scalar
        new_dy = dy * scalar
        new_end_point = Point(self.start_point.x + new_dx, self.start_point.y + new_dy)
        return Vector(self.start_point, new_end_point)

    def dot_product(self, other):
        dx1 = self.end_point.x - self.start_point.x
        dy1 = self.end_point.y - self.start_point.y
        dx2 = other.end_point.x - other.start_point.x
        dy2 = other.end_point.y - other.start_point.y
        return dx1 * dx2 + dy1 * dy2





