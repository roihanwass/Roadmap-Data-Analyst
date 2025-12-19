import time
import os
from datetime import datetime

# Interval cek (detik)
JEDA_WAKTU = 300  # 5 menit (Ganti jadi 60 kalau mau tiap 1 menit)

print("🤖 BOT PENJAGA AKTIF! Memantau folder...")
print(f"Akan melakukan Auto-Push setiap {JEDA_WAKTU} detik jika ada perubahan.")

while True:
    # 1. Cek status git
    # Kita pakai os.system buat jalanin perintah terminal diam-diam
    status = os.popen('git status --porcelain').read()
    
    if status:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Terdeteksi perubahan! Mengirim ke GitHub...")
        
        # Eksekusi perintah Git otomatis
        os.system('git add .')
        os.system('git commit -m "Auto-update by Bot Penjaga 🤖"')
        os.system('git push')
        
        print("✅ Berhasil Push! Cek Discord sekarang.")
    else:
        # Gak ada perubahan, bot tidur dulu
        pass
        
    time.sleep(JEDA_WAKTU)