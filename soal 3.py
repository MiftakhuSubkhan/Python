def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkos kirim berdasarkan kota, berat, dan opsi asuransi.
    """
    # Tarif dasar per kota
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000,
        "Yogyakarta": 13000
    }

    # Ambil tarif dasar sesuai kota, default 0 jika kota tidak ditemukan
    ongkir = tarif_dasar.get(kota, 0) + (2000 * berat_kg)

    # Tambah biaya asuransi jika True
    if asuransi:
        ongkir += 3000

    return ongkir


# Contoh pemanggilan fungsi:
print("Ongkir ke Jakarta (2 kg, tanpa asuransi):", hitung_ongkir(2, "Jakarta"))
print("Ongkir ke Surabaya (3 kg, pakai asuransi):", hitung_ongkir(3, "Surabaya", asuransi=True))
