import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, vector):
        if(self.dimension != vector.dimension):
            raise ValueError("Vectors must be the same lenght")

        res = []
        for i in range(self.dimension):
            res.append(self.coordinates[i] + vector.coordinates[i])
        return Vector(res)

    def __sub__(self, vector):
        if(self.dimension != vector.dimension):
            raise ValueError("Vectors must be the same lenght")

        res = []
        for i in range(self.dimension):
            res.append(self.coordinates[i] - vector.coordinates[i])
        return Vector(res)

    def multiply_by_scalar(self, scalar):
        res = []
        for i in range(self.dimension):
            res.append(scalar * self.coordinates[i])
        return Vector(res)
    
    def magnitude(self):
        res = 0
        for i in range(self.dimension):
            res += self.coordinates[i] ** 2
        return math.sqrt(res)
    
    def direction_vector(self):
        try:
            mag = self.magnitude()
            return self.multiply_by_scalar(1/mag)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the vector %s' % self.__str__)