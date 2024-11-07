def hitung(A, B, C):
    rata_rata = (A+B+C) / 3
    return rata_rata

A = float(input("Masukkan Nilai A: "))
B = float(input("Masukkan Nilai B: "))
C = float(input("Masukkan Nilai C: "))

jumlah = hitung(A, B, C)
print("Rata-rata dari 3 nilai:", jumlah)