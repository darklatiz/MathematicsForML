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
