import pandas as pd
import matplotlib.pyplot as plt

# --- 1. LOAD DATA DARI FILE EKSTERNAL ---
# Ini fungsi sakti: read_csv
# Python akan membaca file 'data_toko.csv' yang ada di folder sama
print("Sedang membaca file data...")
df = pd.read_csv('data_toko.csv')

# Cek dulu 5 data teratas (biar yakin datanya masuk)
print("Preview Data:")
print(df.head()) 
print("-" * 30)

# --- 2. TRANSFORMATION ---
# Hitung Total Omzet per transaksi
df['Total_Belanja'] = df['Harga'] * df['Qty']

# --- 3. ANALISIS (PIVOT TABLE) ---
# Studi Kasus: Kita ingin tahu Omzet berdasarkan KOTA
hasil_analisis = df.groupby('Kota')['Total_Belanja'].sum().sort_values(ascending=False)

print("Total Omzet per Kota:")
print(hasil_analisis)

# --- 4. VISUALISASI ---
# Kita percantik grafiknya dikit
plt.figure(figsize=(10, 6)) # Siapkan kanvas kosong

# Plotting bar chart
# color list: biar tiap batang warnanya beda (opsional, biar keren aja)
warna_warni = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
ax = hasil_analisis.plot(kind='bar', color=warna_warni, edgecolor='black')

plt.title('Total Penjualan Berdasarkan Kota', fontsize=16, fontweight='bold')
plt.xlabel('Kota', fontsize=12)
plt.ylabel('Total Omzet (Rupiah)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=0) # Biar nama kota tegak lurus

# Format angka di sumbu Y biar gak format ilmiah (1e6) tapi angka biasa
plt.ticklabel_format(style='plain', axis='y')

# Tampilkan
plt.tight_layout()
plt.show()

# --- 5. DEEP DIVE (DRILL DOWN) ---
print("\n" + "="*30)
print("ANALISIS KHUSUS JAKARTA")

# LOGIKA FILTERING:
# Bahasa manusianya: "Ambil df, dimana df kolom Kota isinya 'Jakarta'"
df_jakarta = df[df['Kota'] == 'Jakarta']

# Cek apakah datanya beneran cuma Jakarta?
print(df_jakarta.head())

# Mari kita cari Produk Terlaris KHUSUS di Jakarta
produk_jakarta = df_jakarta.groupby('Nama_Produk')['Total_Belanja'].sum().sort_values(ascending=False)

print("\nProduk Paling Laku di Jakarta:")
print(produk_jakarta)

# Visualisasi Mini (Pie Chart) biar variasi
plt.figure(figsize=(8, 8))
produk_jakarta.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Proporsi Penjualan di Jakarta')
plt.ylabel('') # Hilangkan tulisan label Y biar bersih
plt.show()