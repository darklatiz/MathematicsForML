from vector import Vector

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