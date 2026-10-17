def luas_persegi_panjang(p, l):
    return p * l

# Meminta input angka dari pengguna lewat keyboard
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Menghitung dan menampilkan hasilnya
hasil = luas_persegi_panjang(panjang, lebar)
print("Luas persegi panjang adalah:", hasil)