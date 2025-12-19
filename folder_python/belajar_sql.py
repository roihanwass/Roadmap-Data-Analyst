import pandas as pd
import sqlite3 # Library untuk koneksi ke database SQL

# --- BAGIAN 1: PERSIAPAN (Simulasi Server) ---
# Kita baca data CSV yang tadi
df = pd.read_csv('data_toko.csv')

# Kita buat Database bohongan bernama 'toko_komputer.db'
conn = sqlite3.connect('toko_komputer.db')

# Kita masukkan data CSV tadi ke dalam Database menjadi tabel bernama 'transaksi'
# if_exists='replace' artinya kalau tabelnya udah ada, timpa aja.
df.to_sql('transaksi', conn, if_exists='replace', index=False)

print("Database berhasil dibuat! Sekarang saatnya SQL beraksi...")
print("="*50)

# --- BAGIAN 2: MENULIS SQL (THE REAL DEAL) ---

# Misi: Tampilkan Penjualan yang Quantity-nya di atas 3 unit
# Bahasa SQL: "SELECT (semua) FROM (tabel transaksi) WHERE (Qty > 3)"

query_sql = """
SELECT * FROM transaksi 
WHERE Qty > 3
"""

# Eksekusi Query lewat Pandas
hasil_sql = pd.read_sql_query(query_sql, conn)

print("HASIL QUERY SQL (Qty > 3):")
print(hasil_sql)

print("="*50)

# --- TANTANGAN SQL KEDUA ---
# Misi: Berapa total duit yang didapat dari Surabaya?
# SQL punya fungsi SUM() mirip Excel

query_total = """
SELECT Kota, SUM(Harga * Qty) as Total_Omzet
FROM transaksi
WHERE Kota = 'Surabaya'
GROUP BY Kota
"""

hasil_total = pd.read_sql_query(query_total, conn)

print("HASIL SQL AGGREGATION:")
print(hasil_total)

# Tutup koneksi biar sopan
conn.close()