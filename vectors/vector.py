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

vector1 = Vector([8.218,-9.341])
vector2 = Vector([-1.129,2.111])
vector3 = Vector([7.119,8.215])
vector4 = Vector([-8.223, 0.878])
vector5 = Vector([1.671, -1.012, -0.318])


print("Suma v1 + v2: %s" % (vector1 + vector2))
print("Suma v3 - v4: %s" % (vector3 - vector4))
print("Multiplication by scalar: %s" % vector5.multiply_by_scalar(7.41))

vec = Vector([-1,1,1])
print("Magnitude of the vector: %s" % vec.magnitude())
print("Direction vector: %s" % vec.direction_vector())


vector01 = Vector([-0.221, 7.437])
vector02 = Vector([8.813, -1.331, -6.247])

print("Magnitude of the vector01: %s" % vector01.magnitude())
print("Magnitude of the vector02: %s" % vector02.magnitude())
print("Direction of the vector01: %s" % vector01.direction_vector())
print("Direction of the vector02: %s" % vector02.direction_vector())

vector01 = Vector([5.581, -2.136])
vector02 = Vector([1.996, 3.108, -4.554])

print("Magnitude of the vector01: %s" % vector01.magnitude())
print("Magnitude of the vector02: %s" % vector02.magnitude())
print("Direction of the vector01: %s" % vector01.direction_vector())
print("Direction of the vector02: %s" % vector02.direction_vector())