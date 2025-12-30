import csv
import os
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN


def data_lowongan():
    if not os.path.exists(DATA_LOWONGAN):
        return []

    with open(DATA_LOWONGAN, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def simpan_lowongan(data_baru):
    file_exists = os.path.exists(DATA_LOWONGAN)

    with open(DATA_LOWONGAN, mode="a", encoding="utf-8", newline="") as file:
        fieldnames = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data_baru)


def daftar_lowongan():
    clear_screen()
    print("\n====== DAFTAR LOWONGAN ======")

    lowongans = data_lowongan()

    if not lowongans:
        print("Belum ada lowongan.")
        input("Tekan ENTER untuk kembali...")
        return

    tersedia = False
    for i, row in enumerate(lowongans, start=1):
        if row["status_lowongan"] == "belum diambil":
            tersedia = True
            print(f"\nLowongan #{i}")
            print(f"Nama Produk       : {row['nama_produk']}")
            print(f"Deskripsi         : {row['deskripsi_promosi']}")
            print(f"Budget            : Rp {row['budget']}")
            print(f"Syarat Followers  : {row['syarat_followers']}")

    if not tersedia:
        print("\nSemua lowongan sudah diambil.")
        input("Tekan ENTER untuk kembali...")
        return

    pilihan = input("\nPilih nomor lowongan yang ingin diambil (ENTER untuk kembali): ").strip()

    if pilihan == "":
        return

    if not pilihan.isdigit():
        print("Input harus berupa angka.")
        input("Tekan ENTER untuk kembali...")
        return

    milih_lowongan(int(pilihan))


def milih_lowongan(pilihan):
    lowongans = data_lowongan()
    index = pilihan - 1

    if index < 0 or index >= len(lowongans):
        print("Nomor lowongan tidak valid.")
        input("Tekan ENTER untuk kembali...")
        return

    if lowongans[index]["status_lowongan"] != "belum diambil":
        print("Lowongan sudah diambil.")
        input("Tekan ENTER untuk kembali...")
        return

    lowongans[index]["status_lowongan"] = "diambil"

    with open(DATA_LOWONGAN, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = lowongans[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lowongans)

    print("Lowongan berhasil diambil!")
    input("Tekan ENTER untuk kembali...")
