# Lambda function adalah function yang tidak bernama. Biasa disebut juga anonymous function. Adalah function yang disimpan langsung dalam variabel
x = lambda a: a + 10
print(x(5))

angka = input("Masukkan sebuah angka: ")
angka = int(angka)
print((lambda x: (x % 2 and "Angka Ganjil" or "Angka Genap"))(angka))

# Contoh 2
pegawai = [
    {"nama": "Andi", "umur": 30, "menikah": True},
    {"nama": "Suneo", "umur": 45, "menikah": False},
    {"nama": "Abdullah", "umur": 14, "menikah": True},
]
# urutkan berdasarkan umur

pegawai.sort(key=lambda x: x["umur"])

for p in pegawai:
    print(p)

pegawai.sort(key=lambda x: len(x["nama"]))
for p in pegawai:
    print(p)

# contoh 3
barang = [
    {"nama": "Suzuki", "harga": 100000},
    {"nama": "Honda", "harga": 250000},
    {"nama": "Kawasaki", "harga": 500000},
]
# seleksi barang di atas 200000
mahal = list(filter(lambda z: z["harga"] > 200000, barang))

for barang in mahal:
    print(barang)


# contoh 4

produk = [
    {"mobil": "Subaru", "harga": 150000},
    {"mobil": "Ford", "harga": 175000},
    {"mobil": "Hyundai", "harga": 300000},
]

diskon = list(
    map(lambda y: {"mobil": y["mobil"], "harga": int(y["harga"] * 0.85)}, produk)
)

print(diskon)
