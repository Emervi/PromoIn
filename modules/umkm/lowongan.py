import csv
import os
from data.config import DATA_LOWONGAN

def buat_lowongan():
    print("\n====== BUAT LOWONGAN ======")

    nama_produk = input("Nama Produk: ")
    deskripsi = input("Deskripsi: ")
    budget = input("Budget: ")
    syarat_followers = input("Syarat Followers: ")
    status_lowongan = "belum diambil"

    # Path ke file CSV (DARI CONFIG)
    file_path = DATA_LOWONGAN

    # Cek apakah file sudah ada
    file_exists = os.path.isfile(file_path)

    # Pastikan folder data ada
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Buka file CSV
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = [
            "nama_produk",
            "deskripsi",
            "budget",
            "syarat_followers",
            "status_lowongan"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "nama_produk": nama_produk,
            "deskripsi": deskripsi,
            "budget": budget,
            "syarat_followers": syarat_followers,
            "status_lowongan": status_lowongan
        })

    print("\n✅ Lowongan berhasil disimpan!")
    input("Tekan ENTER untuk kembali ke beranda...")


def lihat_lowongan():
    print("\n====== DAFTAR LOWONGAN ======")

    file_path = DATA_LOWONGAN

    if not os.path.isfile(file_path):
        print("Belum ada lowongan.")
        input("Tekan ENTER untuk kembali...")
        return

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        data = list(reader)

        if not data:
            print("Belum ada lowongan.")
        else:
            for i, row in enumerate(data, start=1):
                print(f"\nLowongan #{i}")
                print(f"Nama Produk       : {row['nama_produk']}")
                print(f"Deskripsi         : {row['deskripsi']}")
                print(f"Budget            : {row['budget']}")
                print(f"Syarat Followers  : {row['syarat_followers']}")
                print(f"Status            : {row['status_lowongan']}")

    input("\nTekan ENTER untuk kembali...")