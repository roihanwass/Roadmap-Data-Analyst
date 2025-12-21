import sqlite3

conn = sqlite3.connect('data_balap.db')
cursor = conn.cursor()

print("🔌 Koneksi berhasil!")

# --- TAMBAHAN BARU: RESET ULANG ---
# Hapus tabel lama kalau ada (Biar gak duplikat terus)
cursor.execute("DROP TABLE IF EXISTS umamusume")
print("🧹 Tabel lama berhasil dibuang (Reset).")
# ----------------------------------

# Baru bikin tabel lagi
cursor.execute('''
    CREATE TABLE IF NOT EXISTS umamusume (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        tipe_lari TEXT,
        speed INTEGER
    )
''')
print("📦 Tabel 'umamusume' baru siap!")

# Isi data (Sekarang aman, pasti cuma masuk sekali)
data_kuda = [
    ('Mejiro Ardan', 'Medium', 85),
    ('Special Week', 'Long', 90),
    ('Silence Suzuka', 'Short', 98),
    ('Gold Ship', 'Long', 88),
    ('Tokai Teio', 'Medium', 92)
]

for kuda in data_kuda:
    cursor.execute(f"INSERT INTO umamusume (nama, tipe_lari, speed) VALUES (?, ?, ?)", kuda)

conn.commit()
print(f"✅ Berhasil memasukkan {len(data_kuda)} data bersih.")

# Cek hasil
cursor.execute("SELECT * FROM umamusume")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)

conn.close()
print("🔌 Koneksi ditutup.")