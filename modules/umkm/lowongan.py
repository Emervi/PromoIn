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
        reader = csv.DictReader(file)
        for baris in reader:
            data.append(baris)
    
    return data

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
    print("\n====== DAFTAR LOWONGAN SAYA ======")

    lowongans = data_lowongan()
    umkm_id_login = data.session.USER_LOGIN.get("umkm_id")

    if not umkm_id_login:
        print("Silakan login terlebih dahulu.")
        input("\nTekan ENTER untuk kembali...")
        return

    ada = False
    for i in range(1, len(lowongans)):
        if lowongans[i]["umkm_id"] == umkm_id_login:
            print(f"\nLowongan #{lowongans[i]['lowongan_id']}")
            print(f"Nama Produk       : {lowongans[i]['nama_produk']}")
            print(f"Deskripsi         : {lowongans[i]['deskripsi_promosi']}")
            print(f"Budget            : Rp {lowongans[i]['budget']}")
            print(f"Syarat Followers  : {lowongans[i]['syarat_followers']}")
            print(f"Status            : {lowongans[i]['status_lowongan']}")
            ada = True

    if not ada:
        print("\nKamu belum memiliki lowongan.")

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
        budget = input("Anggaran Promosi: ").strip()
        
        if not budget:
            print("❌ Anggaran tidak boleh kosong ❌")
            continue
        
        if not apakah_int(budget):
            print("❌ Anggaran bukan angka ❌")
            continue
        break
    
    while True:
        syarat_followers = input("Minimal Followers: ").strip()
        
        if not syarat_followers:
            print("❌ Minimal Followers tidak boleh kosong ❌")
            continue
        
        if not apakah_int(syarat_followers):
            print("❌ Minimal Followers bukan angka ❌")
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


def lamaran_masuk():
    print("Food Vlogger: Lazzuardi Langga Duta Wijaya")
    print("Melamar untuk: Batagor")
    print("")
    print("saya tertarik")
    print("Diajukan pada 01/01/2026, 14.43")
    print("")
    print("Setujui Lamaran? jika setuju input id yang sesuai")

    input("\nTekan ENTER untuk kembali...")


def kolaborasi(): 
    print("Batagor")
    print("Dengan Lazzuardi Langga Duta Wijaya")
    print("Anggaran: Rp. 600.000")
    print("Status Pembayaran: Menunggu")
    print("Hubungi No. dibawah untuk info lebih lanjut: 0895378060487")
    print("Menunggu Bukti")

    input("\nTekan ENTER untuk kembali...")

