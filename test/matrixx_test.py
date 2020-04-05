from matrixx.matriz import Matrixx

m = [[1,2,3], [4,5,6]]
m01 = [[7,8], [9,10], [11,12]]
m1 = Matrixx(m)
m2 = Matrixx(m01)
res = m1*m2
mres = Matrixx(res)
print(m1)
print("MAtrix multiplication resukt: {0}".format(mres))

print("Another sample")
mm =  [[3,4,2]]
mm1 = [[13,9,7,15],[8,7,4,6],[6,4,0,3]]
m1 = Matrixx(mm)
m2 = Matrixx(mm1)
r = m1 * m2
mres = Matrixx(r)
print(mres)

print("El orden de los factores aqui si importa m1 X m2")
m1 = Matrixx([[1,2],[3,4]])
m2 = Matrixx([[2,0],[1,2]])
print(Matrixx(m1 * m2))

print("m1 x m2")
print(Matrixx(m2 * m1))

print("Identity Matrix")
identity = Matrixx([[1,0,0],[0,1,0],[0,0,1]])
m01 = Matrixx([[7,8,9], [10,11,12], [12,13,14]])
print("identity x m1")
print(Matrixx(identity * m01))
print("m1 x identity")
print(Matrixx(m01 * identity))
