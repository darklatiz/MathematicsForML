from vector import Vector

'''
A ship travels with velocity given by [1,2], with current flowing 
in the direction given by [1,1] with respect to some co-ordinate axes.
What is the velocity of the ship in the direction of the current?

A.  The projection of the velocity into the current vector
'''

r = Vector([1,2])
s = Vector([1,1])
print("Projection of s onto r = {0}".format(s.scalar_projection(r)))
print("The Vector Projection of s onto r = {0}".format(s.vector_projection(r)))


'''
A ball travels with velocity given by [2,1], 
with wind blowing in the direction given by [3,−4] with respect to some co-ordinate axes.
What is the size of the velocity of the ball in the direction of the wind?
'''
ballVector = Vector([2,1])
windDirection = Vector([3,-4])
print("Projection of s onto r = {0}".format(ballVector.scalar_projection(windDirection)))


'''
Given vectors v=[−4,−3,8], b1=[1,2,3], b2=[−2,1,0] and b3=−3,−6,5] all written in the standard basis, 
what is v in the basis defined by b1, b2 and b3? 
You are given that b1, b2 and b3 are all pairwise orthogonal to each other.
'''
b1 = Vector([1,2,3])
b2 = Vector([-2,1,0])
b3 = Vector([-3,-6,5])
r = Vector([-4,-3,8])
nev = r.basis_change(b1, b2, b3)
print("Change Basis exercise: {0}".format(nev))
