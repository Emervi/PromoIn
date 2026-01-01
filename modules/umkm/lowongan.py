import csv
import os
from modules.utils import clear_screen, apakah_int
from data.config import DATA_LOWONGAN
import data.session

def data_lowongan():
    if not os.path.exists(DATA_LOWONGAN):
        return []
    
    with open(DATA_LOWONGAN, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def simpan_lowongan(data_baru):
    file_ada = os.path.exists(DATA_LOWONGAN)
        
    with open(DATA_LOWONGAN, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
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
            
            print(f"\nLowongan #{lowongans[i]["lowongan_id"]}")
            print(f"Nama Produk       : {lowongans[i]["nama_produk"]}")
            print(f"Deskripsi         : {lowongans[i]["deskripsi_promosi"]}")
            print(f"Budget            : Rp {lowongans[i]["budget"]}")
            print(f"Syarat Followers  : {lowongans[i]["syarat_followers"]}")
            print(f"Status            : {lowongans[i]["status_lowongan"]}")
                    
    input("\nTekan ENTER untuk kembali...")

def buat_lowongan():
    
    clear_screen()
    print("\n====== BUAT LOWONGAN ======")
    
    lowongans = data_lowongan()
    
    # generate id baru untuk data yang baru
    if apakah_int(lowongans[-1]["lowongan_id"]):
        lowongan_id = int(lowongans[-1]["lowongan_id"]) + 1
    else:
        lowongan_id = 1
        
    umkm_id = data.session.USER_LOGIN["umkm_id"]
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
    
    data_baru = {
        "lowongan_id": lowongan_id,
        "umkm_id": umkm_id,
        "nama_produk": nama_produk,
        "deskripsi_promosi": deskripsi_promosi,
        "budget": budget,
        "syarat_followers": syarat_followers,
        "status_lowongan": status_lowongan
    }
    
    simpan_lowongan(data_baru)

    print("\n✅ Lowongan berhasil disimpan ✅")
    input("Tekan ENTER untuk kembali ke beranda...")
