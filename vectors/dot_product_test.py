from vector import Vector

v1 = Vector([1,3,4,2])
print("The dot product is {0}".format(v1.magnitude()))

v2 = Vector([-5,3,2,8])
v3 = Vector([1,2,-1,0])
print("Te dot product v2.v3 = {0}".format(v2.dot_product(v3)))

r = Vector([3,-4,0])
s = Vector([10,5,-6])
print("Projection of s onto r = {0}".format(s.scalar_projection(r)))
print("The Vector Projection of s onto r = {0}".format(s.vector_projection(r)))


a = Vector([3,0,4])
b = Vector([0,5,12])

ret1 = a + b
print("|a + b| = {0}".format(ret1.magnitude()))
maga = a.magnitude()
magb = b.magnitude()
print("|a|+ |b| = {0}".format(maga + magb))

b1 = Vector([2,1])
b2 = Vector([-2,4])
r = Vector([3,4])
nev = r.basis_change(b1, b2)
print("New basis: {0}".format(nev))