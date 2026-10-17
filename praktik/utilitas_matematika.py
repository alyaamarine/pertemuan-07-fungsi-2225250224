print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n dengan while agar harus positif
while n <= 0:
    n = int(input("Banyak suku n: "))

set_total = 0
list_suku = []

# Loop for untuk menghitung suku dan akumulasi total
for i in range(0, n):
    suku = a + i * d
    set_total += suku
    
    # Menghilangkan .0 jika angka bulat agar rapi sesuai Test Case
    if suku.is_integer():
        list_suku.append(str(int(suku)))
    else:
        list_suku.append(str(suku))

# Menampilkan hasil sesuai spesifikasi kriteria
print("Suku:", ", ".join(list_suku))
print(f"Jumlah: {set_total:.1f}" if set_total.is_integer() else f"Jumlah: {set_total:.2f}")