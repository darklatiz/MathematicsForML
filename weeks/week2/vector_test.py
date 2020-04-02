from vectors.vector import Vector
import math

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

print("\n\n Dot product and angle *******************")
vectora = Vector([1,1,-1])
vectorb = Vector([1,-1,1])
print("Dot product a.b = %s" % vectora.dot_product(vectorb))
rad, angle = vectora.angle(vectorb)
print("Angle between a and b, Rad= {0} , Angle= {1}".format(rad, angle))

vectorc = Vector([7.887,4.138])
vectord = Vector([-8.802,6.776])
print("\nDot product c.d = %s" % vectorc.dot_product(vectord))

vectore = Vector([-5.955,-4.904,-1.874])
vectorf = Vector([-4.496, -8.755, 7.103])
print("\nDot product e.f = %s" % vectore.dot_product(vectorf))

vectorx = Vector([3.183, -7.627])
vectorz = Vector([-2.668, 5.319])
radxz, anglexz = vectorx.angle(vectorz)
print("Radians between x.z {0}".format(radxz))

vectory = Vector([7.35, 0.221, 5.188])
vectorr = Vector([2.751, 8.259, 3.985])
radyr, angleyr = vectory.angle(vectorr)
print("Angle between y.r {0}".format(angleyr))

print("\n\n Orthoganility and Parallelism")

vs = Vector([-7.579,-7.88])
vr = Vector([22.737, 23.64])
print("\nAre orthogonal? {0}".format(vs.is_orthogonal(vr)))
print("Are Parallel? {0}".format(vs.is_parallel(vr)))

vs = Vector([-2.029,9.97, 4.172])
vr = Vector([-9.231, -6.639, -7.245])
print("\nAre orthogonal? {0}".format(vs.is_orthogonal(vr)))
print("Are Parallel? {0}".format(vs.is_parallel(vr)))

vs = Vector([-2.328, -7.284, -1.214])
vr = Vector([-1.821, 1.072, -2.94])
print("\nAre orthogonal? {0}".format(vs.is_orthogonal(vr)))
print("Are Parallel? {0}".format(vs.is_parallel(vr)))

vs = Vector([2.118, 4.827])
vr = Vector([0,0])
print("\nAre orthogonal? {0}".format(vs.is_orthogonal(vr)))
print("Are Parallel? {0}".format(vs.is_parallel(vr)))
