import sqlite3

# Buka koneksi ke database yang sudah ada
conn = sqlite3.connect('data_balap.db')
cursor = conn.cursor()

# Kita hitung dulu total datanya ada berapa
cursor.execute("SELECT COUNT(*) FROM umamusume")
jumlah_data = cursor.fetchone()[0]

print(f"😱 Total Data saat ini: {jumlah_data} baris!")
print("-" * 30)

# Tampilkan SEMUA data (tanpa filter speed)
cursor.execute("SELECT * FROM umamusume")
hasil = cursor.fetchall()

for baris in hasil:
    print(baris)

conn.close()