Pertemuan 07 Fungsi Python

Nama: Alya Mutiara Marine
NIM: 2225250224
Kelas: 3A

Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program Python yang modular, mudah dibaca, dan dapat digunakan kembali.

Cara Menjalankan

Jalankan file Python melalui terminal VS Code dengan perintah berikut:

python latihan/01_salam.py
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
python praktik/utilitas_matematika.py

Struktur Fungsi

1. salam(): Menampilkan salam berdasarkan nama dan kelas.
2. luas_persegi_panjang(p, l): Menghitung luas persegi panjang menggunakan panjang dan lebar.
3. jumlah_n(n): Menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan.
4. statistik(data): Menghitung nilai minimum, maksimum, dan rata-rata dari kumpulan data.
5. demo(x): Menunjukkan perbedaan variabel lokal dan variabel di luar fungsi.
6. Fungsi utilitas matematika: Menghitung luas persegi panjang, luas segitiga, jumlah bilangan 1 sampai n, dan faktorial.

## Hasil Pengujian

### Latihan 1 - Fungsi Salam

 Input:  
 Nama = Intan Anugra Salsabila  
 Kelas = 3F   

 Hasil yang diharapkan:  
 Program menampilkan salam beserta nama dan kelas.

 Hasil aktual:  
 Halo, Intan Anugra Salsabila dari kelas 3F. Selamat belajar Python!

### Latihan 2 - Luas Persegi Panjang

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| p = 8, l = 5 | 40 | 40.0 |
| p = 2.5, l = 4 | 10 | 10.0 |
| p = 0, l = 7 | 0 | 0.0 |

### Latihan 3 - Jumlah 1 sampai n

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| n = 1 | 1 | 1 |
| n = 5 | 15 | 15 |
| n = 10 | 55 | 55 |
| n = 100 | 5050 | 5050 |

### Latihan 4 - Statistik Sederhana

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| Data = [70, 80, 65, 90, 75] | Minimum = 65<br>Maksimum = 90<br>Rata-rata = 76.0 | Minimum = 65.0<br>Maksimum = 90.0<br>Rata-rata = 76.0 |

### Latihan 5 - Eksperimen Scope

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| x = 10, demo(20) | x di dalam fungsi = 20<br>y = 25<br>x di luar fungsi = 10<br>hasil = 25 | di dalam fungsi: 20 25<br>di luar fungsi: 10 25 |

### Praktik 2 - Utilitas Matematika Modular

#### Pengujian 1 - Luas Persegi Panjang

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| p = 8, l = 5 | 40 | 40.0 |

#### Pengujian 2 - Luas Segitiga

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| a = 10, t = 6 | 30.0 | 30.0 |

#### Pengujian 3 - Jumlah 1 sampai n

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| n = 10 | 55 | 55 |

#### Pengujian 4 - Faktorial

| Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|
| n = 5 | 120 | 120 |
| n = 0 | 1 | 1 |

Refleksi

Setelah mengerjakan latihan, saya memahami bahwa fungsi dapat membuat program lebih terstruktur dan mengurangi pengulangan kode. Parameter digunakan untuk menerima data, sedangkan return digunakan untuk mengembalikan hasil perhitungan. Saya juga memahami bahwa variabel lokal hanya digunakan di dalam fungsi. Pengujian setiap program membantu memastikan hasil perhitungan sudah benar.