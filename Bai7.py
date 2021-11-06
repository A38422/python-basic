import math

class Polygon:
    def __init__(self, edge1, edge2, edge3):
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3
    def print_polygon(self):
        print(self.edge1)
        print(self.edge2)
        print(self.edge3)

class Triangle(Polygon):
    def perimeter(self):
        return self.edge1 + self.edge2 + self.edge3
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.edge1) * (p - self.edge2) * (p - self.edge3))

tri = Triangle(3, 4, 5)
tri.print_polygon()
print("Chu vi: " + str(tri.perimeter()))
print("Dien tich: " + str(round(tri.area(), 2)))