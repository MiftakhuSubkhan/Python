
s1 = int(input("Masukkan setoran minggu ke-1: "))

s2 = int(input("Masukkan setoran minggu ke-2: "))
s3 = int(input("Masukkan setoran minggu ke-3: "))

# Cek validitas input
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid")
else:
    # Hitung total setoran
    total = s1 + s2 + s3

    # Menentukan kategori total
    if total <= 300000:
        print("rendah")
    elif total <= 600000:
        print("sedang")
    else:
        print("tinggi")
