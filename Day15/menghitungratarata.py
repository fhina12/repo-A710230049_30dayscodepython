# Program untuk menghitung rata-rata
jumlah = 0
n = 0

while True:
  angka = float(input("Masukkan angka (masukkan 0 untuk berhenti): "))
  if angka == 0:
    break
  jumlah += angka
  n += 1

if n == 0:
  print("Tidak ada data yang dimasukkan")
else:
  rata_rata = jumlah / n
  print("Rata-rata:", rata_rata)
