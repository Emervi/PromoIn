import csv
import os
from data.config import DATA_LOWONGAN

def lihat_lowongan():
    print("\n====== DAFTAR LOWONGAN ======")

    file_path = DATA_LOWONGAN

    if not os.path.isfile(file_path):
        print("Belum ada lowongan")
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
                print(f"Deskripsi         : {row['deskripsi_promosi']}")
                print(f"Budget            : {row['budget']}")
                print(f"Syarat Followers  : {row['syarat_followers']}")
                print(f"Status            : {row['status_lowongan']}")
    
    pilihan = input("\nPilih nomor lowongan (ENTER untuk kembali): ")

    if pilihan == "":
        return 

    milih_lowongan(int(pilihan))

def milih_lowongan(pilihan):
    file_path = DATA_LOWONGAN

    if not os.path.isfile(file_path):
        print("Belum ada lowongan.")
        return

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    index = pilihan - 1

    if index < 0 or index >= len(data):
        print("Lowongan tidak valid.")
        return

    if data[index]["status_lowongan"] != "belum diambil":
        print("Lowongan sudah diambil.")
        return

    data[index]["status_lowongan"] = "diambil"

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("Lowongan berhasil diambil!")
    input("Tekan ENTER untuk kembali...")