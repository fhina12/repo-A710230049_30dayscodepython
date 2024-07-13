import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv("data_penjualan.csv")

# Menghitung total penjualan per produk
total_per_produk = data.groupby("produk")["harga_satuan"].sum()

# Menampilkan 5 produk dengan penjualan terbanyak
print(total_per_produk.nlargest(5))

# Menghitung total keuntungan
keuntungan = data["harga_jual"] - data["harga_satuan"]
total_keuntungan = keuntungan.sum()
print(f"Total keuntungan: Rp{total_keuntungan}")
