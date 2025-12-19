import pandas as pd

# 1. MEMBUAT DATA (Mirip input data manual di Excel)
# Kita pakai format 'Dictionary' (Key: Value)
data_transaksi = {
    'Tanggal': ['10-Jan', '10-Jan', '11-Jan', '11-Jan', '12-Jan', '12-Jan', '13-Jan', '13-Jan'],
    'Nama_Produk': [
        'Keyboard Mekanik', 'Mouse Gaming RGB', 'Mousepad XL', 'Headset Bluetooth',
        'Keyboard Mekanik', 'Stand Laptop', 'Mouse Gaming RGB', 'Headset Bluetooth'
    ],
    'Harga_Satuan': [
        350000, 150000, 50000, 250000,
        350000, 75000, 150000, 250000
    ],
    'Qty': [2, 1, 5, 1, 1, 3, 4, 2]
}

# 2. KONVERSI KE DATAFRAME (Excel-nya Python)
df = pd.DataFrame(data_transaksi)

# Ceritanya kita hitung kolom baru 'Total_Omzet' (Mirip rumus perkalian Excel)
# Rumus: Kolom Harga * Kolom Qty
df['Total_Omzet'] = df['Harga_Satuan'] * df['Qty']

# Tampilkan data mentah dulu biar yakin
print("=== DATA TRANSAKSI ===")
print(df)
print("\n" + "="*30 + "\n")

# 3. THE MAGIC: PIVOT TABLE (Group By)
# Pertanyaan: Produk apa yang omzetnya paling besar?
# Syntax: df.groupby('Kolom_Pengelompokan')['Kolom_Yang_Dihitung'].rumus()
hasil_pivot = df.groupby('Nama_Produk')['Total_Omzet'].sum().sort_values(ascending=False)

print("=== HASIL PIVOT (OMZET PER PRODUK) ===")
print(hasil_pivot)

# --- BAGIAN BARU: VISUALISASI ---
import matplotlib.pyplot as plt

# Judul Grafik
print("Sedang membuat grafik...")

# Membuat Bar Chart dari hasil pivot
# kind='bar' artinya grafik batang
# color='teal' biar warnanya cakep dikit
ax = hasil_pivot.plot(kind='bar', color='teal', figsize=(10, 6))

# Aksesoris biar cantik (Judul, Label)
plt.title('Total Omzet Penjualan per Produk', fontsize=14)
plt.xlabel('Nama Produk', fontsize=12)
plt.ylabel('Total Rupiah (Juta)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) # Garis bantu tipis-tipis
plt.xticks(rotation=45) # Miringin tulisan bawah biar gak tabrakan

# Tampilkan Jendela Gambar
plt.show()