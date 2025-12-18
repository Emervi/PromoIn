import csv
import os
from modules.utils import clear_screen, apakah_int
from data.config import DATA_LOWONGAN
import data.session

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
            
            print(f"\nLowongan #{lowongans[i][0]}")
            print(f"Nama Produk       : {lowongans[i][2]}")
            print(f"Deskripsi         : {lowongans[i][3]}")
            print(f"Budget            : Rp {lowongans[i][4]}")
            print(f"Syarat Followers  : {lowongans[i][5]}")
            print(f"Status            : {lowongans[i][6]}")
                    
    input("\nTekan ENTER untuk kembali...")

def buat_lowongan():
    
    clear_screen()
    print("\n====== BUAT LOWONGAN ======")
    
    lowongans = data_lowongan()
    
    # generate id baru untuk data yang baru
    if apakah_int(lowongans[-1][0]):
        lowongan_id = int(lowongans[-1][0]) + 1
    else:
        lowongan_id = 1
        
    umkm_id = data.session.USER_LOGIN[0]
    status_lowongan = "belum diambil"
    
    while True:
        nama_produk = input("Nama Produk: ").strip()
        
        if not nama_produk:
            print("❌ Nama Produk tidak boleh kosong ❌")
            continue
        break
    
    while True:
        deskripsi_promosi = input("Deskripsi: ").strip()
        
        if not deskripsi_promosi:
            print("❌ Deskripsi tidak boleh kosong ❌")
            continue
        break
    
    while True:
        budget = input("Budget: ").strip()
        
        if not budget:
            print("❌ Budget tidak boleh kosong ❌")
            continue
        
        if not apakah_int(budget):
            print("❌ Budget bukan angka ❌")
            continue
        break
    
    while True:
        syarat_followers = input("Syarat Followers: ").strip()
        
        if not syarat_followers:
            print("❌ Syarat Followers tidak boleh kosong ❌")
            continue
        
        if not apakah_int(syarat_followers):
            print("❌ Syarat Followers bukan angka ❌")
            continue
        break
    
    data_baru = [
        lowongan_id,
        umkm_id,
        nama_produk,
        deskripsi_promosi,
        budget,
        syarat_followers,
        status_lowongan
    ]
    
    simpan_lowongan(data_baru)

    print("\n✅ Lowongan berhasil disimpan ✅")
    input("Tekan ENTER untuk kembali ke beranda...")
