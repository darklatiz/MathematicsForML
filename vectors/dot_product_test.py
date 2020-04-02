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

b1 = Vector([1,1])
b2 = Vector([1,-1])
r = Vector([5,-1])
nev = r.basis_change(b1, b2)
print("Change Basis exercise 01: {0}".format(nev))

b1 = Vector([3,4])
b2 = Vector([4,-3])
r = Vector([10,-5])
nev = r.basis_change(b1, b2)
print("Change Basis exercise 02: {0}".format(nev))

b1 = Vector([-3,1])
b2 = Vector([1,3])
r = Vector([2,2])
nev = r.basis_change(b1, b2)
print("Change Basis exercise 03: {0}".format(nev))


b1 = Vector([2,1,0])
b2 = Vector([1,-2,-1])
b3 = Vector([-1,2,-5])
r = Vector([1,1,1])
nev = r.basis_change(b1, b2, b3)
print("Change Basis exercise 04: {0}".format(nev))


b1 = Vector([1,0,0,0])
b2 = Vector([0,2,-1,0])
b3 = Vector([0,1,2,0])
b4 = Vector([0,0,0,3])
r = Vector([1,1,2,3])
nev = r.basis_change(b1, b2, b3, b4)
print("Change Basis exercise 04: {0}".format(nev))
