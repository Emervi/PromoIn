import csv
import os
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN
from data.config import DATA_FOOD_VLOGGER

import data.session

def data_vlogger():
    if not os.path.exists(DATA_FOOD_VLOGGER):
        return []

    with open(DATA_FOOD_VLOGGER, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def lowongan_berlangsung():
    clear_screen()
    print("\n====== Lowongan Berlangsung ======")
    
    food_vlogger = data_vlogger()

    if not os.path.exists(DATA_LOWONGAN):
        print("File lowongan tidak ditemukan.")
        input("Tekan ENTER untuk kembali...")
        return

    status = []

    with open(DATA_LOWONGAN, newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            status.append(row)

    user_session = data.session.USER_LOGIN
    if not user_session:
        print("❌ Anda belum login!")
        input("\nTekan ENTER untuk kembali...")
        return
    
    vlogger_id_login = str(user_session.get("vlogger_id", "")).strip()

    if not vlogger_id_login:
        print("Silakan login terlebih dahulu.")
        input("\nTekan ENTER untuk kembali...")
        return
    
    for i in range(0, len(food_vlogger)):
        id_di_csv = str(food_vlogger[i].get("vlogger_id", "")).strip()

    for item in status:
        if item["status_lowongan"] == "diambil" and id_di_csv == vlogger_id_login:
            print(f"Lowongan {item['nama_produk']} sedang berlangsung")
        else:
            print("Belum memilih lowongan")

    input("Tekan ENTER untuk kembali...")
