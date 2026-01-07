# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_BUKTI_PROMOSI
from modules.utils import clear_screen

# function untuk mengambil data bukti_promosi
def data_bukti_promosi():
    if not os.path.exists(DATA_BUKTI_PROMOSI):
        return []
    
    with open(DATA_BUKTI_PROMOSI, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# procedure untuk menyimpan data ke dalam file data bukti_promosi
def simpan_bukti_promosi(data_baru):
    file_ada = os.path.exists(DATA_BUKTI_PROMOSI)
        
    with open(DATA_BUKTI_PROMOSI, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)

# procedure untuk mengupdate data bukti_promosi
def update_bukti_promosi(data_baru):

    with open(DATA_BUKTI_PROMOSI, mode="w", newline='') as file:
        nama_kolom = data_baru[0].keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)        
        writer.writeheader()
        writer.writerows(data_baru)

def tampilkan_bukti(lowongan_id):
    
    bukproms = data_bukti_promosi()
    
    clear_screen()
    print(f"\n===== LIHAT BUKTI LOWONGAN #{lowongan_id} =====\n")
        
    for bukprom in bukproms:
        if bukprom["lowongan_id"] == str(lowongan_id):
            print(f"Link Bukti Konten: {bukprom["link_konten"]}\n")
    
    print("[1] Setujui")
    print("[2] Tolak")
    print("[0] Kembali")
    
    while True:
        pilihan = input("> ").strip()
        
        if not pilihan:
            print("❌ Perintah tidak boleh kosong ❌")
            continue
            
        if pilihan not in ("1", "2", "0"):
            print("❌ Inputan tidak valid ❌")
            continue
        
        break
    
    if pilihan == "1":
        for bukprom in bukproms:
            if bukprom["lowongan_id"] == str(lowongan_id):
                bukprom["status_verifikasi"] = "Disetujui"
        
        update_bukti_promosi(bukproms)
        return "setuju"
    
    if pilihan == "2":
        for bukprom in bukproms:
            if bukprom["lowongan_id"] == str(lowongan_id):
                bukprom["status_verifikasi"] = "Ditolak"
        
        update_bukti_promosi(bukproms)
        return "tolak"
        
    if pilihan == "0":
        return ""