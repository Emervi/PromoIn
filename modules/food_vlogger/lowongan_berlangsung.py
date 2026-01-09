import csv
import os
from modules.utils import clear_screen
from data.config import DATA_LAMARAN, DATA_LOWONGAN
import data.session

def lowongan_berlangsung():
    clear_screen()
    print("\n====== LOWONGAN BERLANGSUNG ======")

    if not os.path.exists(DATA_LAMARAN) or not os.path.exists(DATA_LOWONGAN):
        print("\n❌ Data tidak ditemukan.")
        input("\nTekan ENTER untuk kembali...")
        return

    map_produk = {}
    with open(DATA_LOWONGAN, newline="", encoding="utf-8") as csv_low:
        reader_low = csv.DictReader(csv_low)
        for row in reader_low:
            # Pasang lowongan_id dengan nama_produk
            map_produk[row["lowongan_id"]] = row["nama_produk"]

    status_lamaran = []
    with open(DATA_LAMARAN, newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            status_lamaran.append(row)

    user_session = data.session.USER_LOGIN
    if not user_session:
        print("❌ Anda belum login!")
        input("\nTekan ENTER untuk kembali...")
        return
    
    vlogger_id_login = str(user_session.get("vlogger_id", "")).strip()
    
    ada = False 
    for item in status_lamaran:
        vlogger_id_item = str(item.get("vlogger_id", "")).strip()

        id_low_lamaran = item.get("lowongan_id")
        nama_produk = map_produk.get(id_low_lamaran, "Produk Tidak Diketahui")

        if item["status"] == "Pending" and vlogger_id_item == vlogger_id_login:
            print(f"\n✅ Lowongan '{nama_produk}' sedang berlangsung")
            ada = True
            
    if not ada:
        print("❌ Anda belum memilih lowongan.")

    input("\nTekan ENTER untuk kembali...")
