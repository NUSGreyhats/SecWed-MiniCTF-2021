from Crypto.Util.number import long_to_bytes

p = 111833273634764077547826364583790448222771931155060022657164482300040395018031
a1 = 107202531498478870888976956508359914255255598414892142692550690678522116273360
a2 = 108748406654538196233423392697025176082318689897915763241182607773495156802918
a3 = 82880793737069650951471433567164749812917560053478104874894344176499230265315

x,y,z = PolynomialRing(ZZ,['x','y','z']).gens()

f1 = (x**2 + y**2 + z**2) - a1
f2 = (x**3 + y**3 + z**3) - a2
f3 = (x**4 + y**4 + z**4) - a3

f = f1.resultant(f2, y).resultant(f1.resultant(f3, y), x)
poly = f.univariate_polynomial().change_ring(GF(p))
for root in poly.roots():
    m = int(root[0])
    print(long_to_bytes(m))