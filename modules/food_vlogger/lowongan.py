import csv
import os
from data.config import DATA_LOWONGAN

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
