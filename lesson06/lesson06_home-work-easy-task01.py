# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.x1 = coordinates[0][0]
        self.x2 = coordinates[1][0]
        self.x3 = coordinates[2][0]
        self.y1 = coordinates[0][1]
        self.y2 = coordinates[1][1]
        self.y3 = coordinates[2][1]

    def add_coordinate(self, new_coordinate):
        if len(self.coordinates) < 3:
            self.coordinates.append(new_coordinate)
        else:
            raise IOError("Apex of the triangle cannot be more than 3")

    def area(self):
        result = 0.5 * ( (self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3) )
        return abs(result)


coordinates = [[1, 1], [2, 3], [3, 2]]

t = Triangle(coordinates)
print(t.area())

