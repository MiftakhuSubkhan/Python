

def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan nama hari.
    """
    # Data jadwal dalam bentuk dictionary
    jadwal = {
        "Senin": ["Algoritma", "Kalkulus"],
        "Selasa": ["Basis Data", "Jaringan Komputer"],
        "Rabu": ["Pemrograman Python", "Sistem Operasi"],
        "Kamis": ["PBO", "Statistika"],
        "Jumat": ["Kewirausahaan"]
    }

    # Cek apakah hari yang dimasukkan ada di data
    if hari in jadwal:
        print(f"Jadwal hari {hari}: {', '.join(jadwal[hari])}")
    else:
        print("Hari tidak ditemukan")

# Contoh pemanggilan fungsi
jadwal_hari("Rabu")
jadwal_hari("Minggu")