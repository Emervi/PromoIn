import csv
import os
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN

def data_lowongan():
    data = []
    
    if not os.path.exists(DATA_LOWONGAN):
        return []
    
    with open(DATA_LOWONGAN, mode="r", newline='') as file:
        reader = csv.reader(file)
        for baris in reader:
            data.append(baris)
    
    return data

def simpan_lowongan(data_baru):
    with open(DATA_LOWONGAN, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_baru)

def daftar_lowongan():
    
    clear_screen()
    print("\n====== DAFTAR LOWONGAN ======")
    
    lowongans = data_lowongan()
    
    if len(lowongans) == 1:
        print("Belum ada lowongan")
        
    else:
        for i in range(len(lowongans)):
            
            if i == 0: continue
            
            if lowongans[i][6] == "belum diambil":
                print(f"\nLowongan #{lowongans[i][0]}")
                print(f"Nama Produk       : {lowongans[i][2]}")
                print(f"Deskripsi         : {lowongans[i][3]}")
                print(f"Budget            : Rp {lowongans[i][4]}")
                print(f"Syarat Followers  : {lowongans[i][5]}")

    pilihan = input("\nMasukan nomor lowongan yang ingin dilamar (Tekan ENTER untuk kembali): ").strip()
    
    if pilihan == "":
        return
    else:
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






    

