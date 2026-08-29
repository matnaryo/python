# Demo menggunakan print


def luasSegitiga(tinggi, alas):
    print("Luas segitiga :", alas * tinggi / 2)


hasil = luasSegitiga(10, 3)
print(hasil)

# Demo return


def luasTrapesium(atas, bawah, tinggi):
    return (atas + bawah) * tinggi / 2


hasil = luasTrapesium(3, 5, 6)
print(hasil)
