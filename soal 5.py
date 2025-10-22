import os
import csv
import json
import logging

# 1. Setup logging sederhana
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

try:
    # 2. Membuat folder "data" jika belum ada
    os.makedirs("data", exist_ok=True)
    logging.info("Mulai proses rekap presensi...")

    # 3. Menulis file CSV presensi
    data_presensi = [
        ["nim", "nama", "hadir_uts"],
        ["2301", "Andi", 1],
        ["2302", "Budi", 0],
        ["2303", "Citra", 1]
    ]

    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data_presensi)
    logging.info("File CSV berhasil dibuat.")

    # 4. Membaca file CSV dan menghitung ringkasan
    total = 0
    hadir = 0
    with open("data/presensi.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row["hadir_uts"] == "1":
                hadir += 1

    # Hitung persentase kehadiran
    persentase = (hadir / total) * 100

    # Simpan ke file JSON
    ringkasan = {
        "total_mahasiswa": total,
        "jumlah_hadir": hadir,
        "persentase_hadir": persentase
    }

    with open("data/ringkasan.json", "w") as f:
        json.dump(ringkasan, f, indent=4)

    logging.info("Ringkasan berhasil disimpan ke file JSON.")

except Exception as e:
    logging.error(f"Gagal memproses data: {e}")
