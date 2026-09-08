class Mobil:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f"Mobil {self.merk} ({self.tahun}) - Warna: {self.warna}")

# Aplikasi
if __name__ == "__main__":
    mobil1 = Mobil("Toyota", 2020, "Merah")
    mobil1.tampilkan_info()

    mobil2 = Mobil("Honda", 2019, "Hitam")
    mobil2.tampilkan_info()
