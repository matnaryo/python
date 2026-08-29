# definisi fungsi untuk menghitung luas trapesium
def luas_trapesium(a, b, t):
    return (a + b) * t / 2

# contoh pemakaian fungsi
# bisa diganti dengan input dari pengguna jika mau
sisi_atas = float(input("Masukkan panjang sisi atas (a): "))
sisi_bawah = float(input("Masukkan panjang sisi bawah (b): "))
tinggi = float(input("Masukkan tinggi trapesium (t): "))

hasil = luas_trapesium(sisi_atas, sisi_bawah, tinggi)
print(f"Luas trapesium dengan a={sisi_atas}, b={sisi_bawah}, t={tinggi} adalah: {hasil}")
