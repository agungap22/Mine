p={1,2,3,4,7,9,19}
q={5,12,16,17,7,9,19,6}
r={19,6,3,8}

print(p)
print(q)
print(r)

print ("Gabungan dari P dengan Q adalah", p.union(q))
print ("Gabungan dari P dengan R adalah", p.union(r))
print ("Gabungan dari Q dengan R adalah", q.union(r))
print ("Irisan dari gabungan P dengan Q dan gabungan Q dengan R adalah", p.union(q)&q.union(r))
print ('Sysmmetric difference dari gabungan Q dengan R dan gabungan P dengan Q',q.union(r).difference(p.union(q)))