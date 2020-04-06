from matrixx.matriz import Matrixx

m = [[1,2,3], [4,5,6]]
m01 = [[7,8], [9,10], [11,12]]
m1 = Matrixx(m)
m2 = Matrixx(m01)
res = m1*m2
print("MAtrix multiplication resukt: {0}".format(res))

print("Another sample")
mm =  [[3,4,2]]
mm1 = [[13,9,7,15],[8,7,4,6],[6,4,0,3]]
m1 = Matrixx(mm)
m2 = Matrixx(mm1)
r = m1 * m2
print(r)

print("El orden de los factores aqui si importa m1 X m2")
m1 = Matrixx([[1,2],[3,4]])
m2 = Matrixx([[2,0],[1,2]])
print(m1 * m2)

print("m1 x m2")
print(m2 * m1)

print("----------------------------")
print("Identity Matrix ************")
identity = Matrixx([[1,0,0],[0,1,0],[0,0,1]])
m01 = Matrixx([[7,8,9], [10,11,12], [12,13,14]])
print("identity x m1")
print(identity * m01)
print("m1 x identity")
print(m01 * identity)

print("----------------------------")
print("Matriz Equality ***********")
m3 = Matrixx([[1,2,3],[4,5,6]])
m4 = Matrixx([[1,2,3],[4,5,6]])
print("m3 == m4 ? {0}".format(m3 == m4))

m3 = Matrixx([[1,2],[4,5]])
m4 = Matrixx([[1,2,3],[4,5,6]])
print("m3 == m4 ? {0}".format(m3 == m4))

print("----------------------------")
print("Matrix Addition ***********")
try:
    r = m3 + m4
except Exception as ex:
    print("Error in matriz addition: {0}".format(ex))

m3 = Matrixx([[1,2,3],[4,5,6]])
m4 = Matrixx([[1,2,3],[4,5,6]])
r = m3 + m4
print(r)

print("----------------------------")
print("Matrix Multiplication by Scalar ***********")
m3 = Matrixx([[1,2,3],[4,5,6]])
print(m3.scalar_multiplication(0.5))
print(m3.scalar_multiplication(2.5))
print(m3.scalar_multiplication(0.001))

print("-------------------------------------------")
print("Matrix Transpose **************************")
t = m3.transpose()
print(t)
print(t.transpose())
