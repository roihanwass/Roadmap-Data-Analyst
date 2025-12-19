import pandas as pd
import matplotlib.pyplot as plt

print("Mulai Menganalisis...")

# BUG 1: Hati-hati sama nama file. Pastikan sesuai sama yang ada di foldermu.
df = pd.read_csv('data_toko.csv') 

# BUG 2: Pandas itu sensitif banget sama huruf besar/kecil di nama kolom.
# Kita mau filter khusus transaksi di 'Bandung'
df_bandung = df[df['Kota'] == 'Bandung']

# BUG 3: Kita mau cari Rata-rata (mean) Harga barang di Bandung
# Ingat, setelah groupby harus ada fungsi agregasi-nya (sum, mean, count, dll)
# Dan fungsi itu harus dipanggil sebagai 'method' (pakai tanda kurung)
hasil = df_bandung.groupby('Nama_Produk')['Harga'].mean()

print("Hasil Rata-rata Harga di Bandung:")
print(hasil)

# BUG 4: Visualisasi
# Perhatikan cara memanggil fungsi show
plt.figure(figsize=(8, 5))
hasil.plot(kind='barh', color='orange') # 'barh' itu horizontal bar (ini bener kok)
plt.title('Rata-rata Harga Produk di Bandung')

plt.show()  # Pastikan ini dipanggil dengan tanda kurung