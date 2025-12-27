import csv
import os
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN

def lowongan_berlangsung():
    clear_screen()
    print("\n====== Lowongan Berlangsung ======")

    if not os.path.exists(DATA_LOWONGAN):
        print("File lowongan tidak ditemukan.")
        input("Tekan ENTER untuk kembali...")
        return

    status = []

    with open(DATA_LOWONGAN, newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            status.append(row)

    for item in status:
        if item["status_lowongan"] == "diambil":
            print(f"Lowongan {item['nama_produk']} sedang berlangsung")

    input("Tekan ENTER untuk kembali...")
