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
    print("\n====== DAFTAR LOWONGAN SAYA ======")

    lowongans = data_lowongan()
    

    user_session = data.session.USER_LOGIN
    if not user_session:
        print("❌ Anda belum login!")
        input("\nTekan ENTER untuk kembali...")
        return

    umkm_id_login = str(user_session.get("umkm_id", "")).strip()

    if not umkm_id_login:
        print("Silakan login terlebih dahulu.")
        input("\nTekan ENTER untuk kembali...")
        return

    ada = False
    for i in range(0, len(lowongans)):
        id_di_csv = str(lowongans[i].get("umkm_id", "")).strip()
        
        if id_di_csv == umkm_id_login:
            try:
                # Mengubah data yang diterima menjadi integer
                int_budget = int(lowongans[i]['budget'])
                key_followers = 'minimal_followers' if 'minimal_followers' in lowongans[i] else 'syarat_followers'
                int_minimal_followers = int(lowongans[i][key_followers])
                
                # Melakukan format angka menjadi ribuan
                formatted_budget = f"{int_budget:,}".replace(",", ".")
                formatted_min_followers = f"{int_minimal_followers:,}".replace(",", ".")
                
                print(f"\nLowongan #{lowongans[i]['lowongan_id']}")
                print(f"Nama Produk       : {lowongans[i]['nama_produk']}")

                desc_key = 'deskripsi' if 'deskripsi' in lowongans[i] else 'deskripsi_promosi'
                print(f"Deskripsi         : {lowongans[i][desc_key]}")
                print(f"Budget            : Rp {formatted_budget}")
                print(f"Minimal Followers : {formatted_min_followers} Followers")
                
                status_low = lowongans[i]['status_lowongan']
                emoji = "✅" if status_low == "diambil" else "❌"
                print(f"Status            : {status_low} {emoji}")
                
                ada = True
            except (ValueError, KeyError) as e:
                continue

    if not ada:
        print("\nKamu belum memiliki lowongan.")
        print(f"(ID Anda: {umkm_id_login}, Data diperiksa: {len(lowongans)} baris)")

    input("\nTekan ENTER untuk kembali...")


def buat_lowongan():
    
    while True:
        clear_screen()
        print("\n====== BUAT LOWONGAN ======")
        
        lowongans = data_lowongan()
        
        # generate id baru untuk data yang baru
        if len(lowongans) == 0:
            lowongan_id = 1
        else:
            lowongan_id = int(lowongans[-1]["lowongan_id"]) + 1        
            
        umkm_id = data.session.USER_LOGIN["umkm_id"]
        status_lowongan = "belum diambil"
        
        while True:
            nama_produk = input("Nama Produk: ").capitalize().strip()
            
            if not nama_produk:
                print("❌ Nama Produk tidak boleh kosong ❌")
                continue
            break
        
        while True:
            kategori = input("Kategori: ").capitalize().strip()
            
            if not kategori:
                print("❌ Kategori tidak boleh kosong ❌")
                continue
            break
        
        while True:
            deskripsi = input("Deskripsi: ").strip()
            
            if not deskripsi:
                print("❌ Deskripsi tidak boleh kosong ❌")
                continue
            break
        
        while True:
            budget = input("Anggaran Promosi: ").strip()
            
            if not budget:
                print("❌ Anggaran Promosi tidak boleh kosong ❌")
                continue
            
            if not apakah_int(budget):
                print("❌ Anggaran Promosi bukan angka ❌")
                continue
            
            budget = int(budget)
            
            if budget < 25000:
                print("❌ Anggaran Promosi minimal Rp 25.000 ❌")
                continue
            
            break
        
        while True:
            minimal_followers = input("Minimal Followers: ").strip()
            
            if not minimal_followers:
                print("❌ Minimal Followers tidak boleh kosong ❌")
                continue
            
            if not apakah_int(minimal_followers):
                print("❌ Minimal Followers bukan angka ❌")
                continue
            
            minimal_followers = int(minimal_followers)
            
            if minimal_followers < 1000:
                print("❌ Minimal Followers paling sedikitnya 1000 ❌")
                continue
            
            break
        
        while True:
            batas_waktu_lowongan = input("Lama Lowongan Tayang (Hari): ").strip()
            
            if not batas_waktu_lowongan:
                print("❌ Lama Lowongan Tayang tidak boleh kosong ❌")
                continue
            
            if not apakah_int(batas_waktu_lowongan):
                print("❌ Lama Lowongan Tayang bukan angka ❌")
                continue
            
            batas_waktu_lowongan = int(batas_waktu_lowongan)
            
            if batas_waktu_lowongan <= 0 or batas_waktu_lowongan > 30:
                print("❌ Lama Lowongan Tayang tidak boleh lebih dari 30 hari ❌")
                continue
            
            break
        
        while True:
            batas_waktu_pengerjaan = input("Lama Batas Waktu Pengerjaan (Hari): ").strip()
            
            if not batas_waktu_pengerjaan:
                print("❌ Lama Batas Waktu Pengerjaan tidak boleh kosong ❌")
                continue
            
            if not apakah_int(batas_waktu_pengerjaan):
                print("❌ Lama Batas Waktu Pengerjaan bukan angka ❌")
                continue
            
            batas_waktu_pengerjaan = int(batas_waktu_pengerjaan)
            
            if batas_waktu_pengerjaan <= 0 or batas_waktu_pengerjaan > 30:
                print("❌ Lama Waktu Pengerjaan tidak boleh lebih dari 30 hari ❌")
                continue
            
            break
        
        while True:
            print("Apakah data lowongan yang dimasukan sudah benar?")
            print("1. Ya")
            print("2. Buat ulang lowongan")
            konfirmasi = input("> ").strip()
            
            if not konfirmasi:
                print("❌ Inputan tidak boleh kosong ❌")
                continue
            
            if not apakah_int(konfirmasi):
                print("❌ Inputan harus berupa angka ❌")
                continue
            
            konfirmasi = int(konfirmasi)
            
            if konfirmasi not in [1, 2]:
                print("❌ Pilihan hanya 1 atau 2 ❌")
                continue
                            
            if konfirmasi == 1:
                data_baru = {
                    "lowongan_id": lowongan_id,
                    "umkm_id": umkm_id,
                    "nama_produk": nama_produk,
                    "deskripsi": deskripsi,
                    "budget": budget,
                    "minimal_followers": minimal_followers,
                    "status_lowongan": status_lowongan,
                    "kategori": kategori,
                    "batas_waktu_lowongan": batas_waktu_lowongan,
                    "batas_waktu_pengerjaan": batas_waktu_pengerjaan,
                }
                
                simpan_lowongan(data_baru)

                print("\n✅ Lowongan berhasil disimpan ✅")
                input("Tekan ENTER untuk kembali ke beranda...")
                break

            if konfirmasi == 2:
                break
            
        if konfirmasi == 1:
            break
        elif konfirmasi == 2:
            pass

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

