import csv
import os
from data.config import DATA_LOWONGAN, DATA_FOOD_VLOGGER, DATA_LAMARAN, DATA_UMKM
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.lamaran import data_lamaran,simpan_lamaran
from modules.bukti_promosi import data_bukti_promosi, simpan_bukti_promosi, update_bukti_promosi
from datetime import datetime
import data.session


def data_lowongan():
    if not os.path.exists(DATA_LOWONGAN):
        return []

    with open(DATA_LOWONGAN, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def simpan_lowongan(data_baru):
    file_exists = os.path.exists(DATA_LOWONGAN)

    with open(DATA_LOWONGAN, mode="a", encoding="utf-8", newline="") as file:
        fieldnames = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data_baru)

def update_lowongan(lowongans):
    with open(DATA_LOWONGAN, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = lowongans[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lowongans)
    

def daftar_lowongan():
    clear_screen()
    print("\n====== DAFTAR LOWONGAN ======")

    lowongans = data_lowongan()
    
    # mengambil seluruh data umkm
    umkms = data_umkm()
    
    # variable untuk menyimpan umkm_id yang ada pada lowongan
    nama_usaha_umkm = {}
    
    # mengambil umkm_id dan memasangkannya dengan nama_usaha
    for umkm in umkms:
        nama_usaha_umkm[umkm["umkm_id"]] = umkm["nama_usaha"]

    ada = False
    for i in range(0, len(lowongans)):
            
        if lowongans[i]["status_lowongan"] == "Belum Diambil":
            
            # mengubah data yang diterima menjadi integer
            int_budget = int(lowongans[i]['budget'])
            int_minimal_followers = int(lowongans[i]['minimal_followers'])
            
            # melakukan format angka menjadi ribuan
            formatted_budget = f"{int_budget:,}".replace(",", ".")
            formatted_min_followers = f"{int_minimal_followers:,}".replace(",", ".")
            
            # mengambil umkm_id yang ada pada lowongan
            umkm_id = lowongans[i]["umkm_id"]
            
            # mengecek apakah ada umkm_id di dalam data umkm
            if umkm_id in nama_usaha_umkm.keys():
                # jika ada maka nama_usaha akan sesuai dengan umkm_id yang ada di dalam data umkm
                nama_usaha = nama_usaha_umkm[umkm_id]
            else:
                nama_usaha = "-"
            
            print(f"\nLowongan Id #{lowongans[i]['lowongan_id']}")
            print(f"😋 Nama Produk                   : {lowongans[i]['nama_produk']}")
            print(f"🍴 Nama Usaha                    : {nama_usaha}")
            print(f"🔖 Kategori                      : {lowongans[i]['kategori']}")
            print(f"📃 Deskripsi                     : {lowongans[i]['deskripsi']}")
            print(f"💲 Budget                        : Rp {formatted_budget}")
            print(f"🤝 Minimal Followers             : {formatted_min_followers} Followers")
            print(f"⏳ Lama Batas Waktu Pengerjaan   : {lowongans[i]['batas_waktu_pengerjaan']} Hari")
            ada = True

    # jika tidak ada lowongan maka ini akan dijalankan
    if not ada:
        print("\n❌ Tidak ada lowongan tersedia ❌")
        input("\nTekan ENTER untuk kembali...")
        return

    pilihan = input("\nMasukan nomor lowongan yang ingin diambil (Tekan ENTER untuk kembali): ").strip()

    if pilihan == "":
        return

    if not pilihan.isdigit():
        print("❌ Input harus berupa angka.")
        input("Tekan ENTER untuk kembali...")
        return

    milih_lowongan(int(pilihan))


def milih_lowongan(pilihan):
    
    lowongans = data_lowongan()
    index = pilihan - 1

    if index < 0 or index >= len(lowongans):
        print("\n❌ Nomor lowongan tidak valid.")
        input("\nTekan ENTER untuk kembali...")
        return
    
    id_lowongan_asli = lowongans[index]["lowongan_id"].strip()

    lowongans[index]["status_lowongan"] = "Diambil"
    
    update_lowongan(lowongans)

    #id lamaran
    lamarans = data_lamaran()
    lamarans_valid = [l for l in lamarans if l.get("lamaran_id") and l.get("lamaran_id").strip()]

    if not lamarans_valid:
        id_baru = 1
    else:
    # Ambil ID terakhir dari data yang benar-benar valid
        id_baru = int(lamarans_valid[-1]["lamaran_id"]) + 1

    #akun fv yang ngelamar yang ambil session user yang login
    user_session = data.session.USER_LOGIN

    if not user_session:
        print("❌ Anda belum login!")
        input("Tekan ENTER untuk kembali...")
        return
    
    vlogger_id_login = str(user_session.get("vlogger_id", "")).strip()
    
    if not vlogger_id_login:
        print("❌ Tidak ditemukan ID vlogger.")
        input("Tekan ENTER untuk kembali...")
        return
    
    #tanggal lamaran
    tanggal_lamar = datetime.now().strftime("%d-%m-%Y")

    #status lamaran
    status = "Pending"

    data_baru = {
        "lamaran_id": id_baru,
        "lowongan_id": id_lowongan_asli,
        "vlogger_id": vlogger_id_login,
        "tanggal_lamar": tanggal_lamar,
        "status": status
    }

    simpan_lamaran(data_baru)

    print("\n✅ Lowongan berhasil dilamar, tunggu persetujuan dari UMKM!")
    input("\nTekan ENTER untuk kembali...")


def kolab():

    vlogger_id = data.session.USER_LOGIN["vlogger_id"]
    
    umkms = data_umkm()
    lamarans = data_lamaran()
    lowongans = data_lowongan()
    bukproms = data_bukti_promosi()
    lowongan_vlogger = []
    bukprom_vlogger = {}
    nama_usaha_umkm = {}
    
    # mengambil umkm_id dan memasangkannya dengan nama_usaha
    for umkm in umkms:
        nama_usaha_umkm[umkm["umkm_id"]] = umkm["nama_usaha"]
    
    for lamaran in lamarans:
        
        if lamaran["vlogger_id"] == vlogger_id and lamaran["status"] == "Disetujui":
            lowongan_vlogger.append(lamaran["lowongan_id"])
    
    for bukprom in bukproms:
        bukprom_vlogger[bukprom["lowongan_id"]] = bukprom
    
    while True:
        clear_screen()
        print("\n===== KOLABORASI SAYA =====")
        
        if not lowongan_vlogger:
            print("\n❌ Belum ada kolaborasi ❌")

        for lowongan in lowongans:
            
            # mengubah data yang diterima menjadi integer
            int_budget = int(lowongan['budget'])
            
            # melakukan format angka menjadi ribuan
            formatted_budget = f"{int_budget:,}".replace(",", ".")
            
            # variable untuk menyimpan status dari bukti promosi
            status_bukti = "Belum Ada"
            
            lowongan_id = lowongan["lowongan_id"]
            umkm_id = lowongan["umkm_id"]
            
            if lowongan_id in lowongan_vlogger:
                
                # mengecek apakah ada umkm_id di dalam data umkm
                if umkm_id in nama_usaha_umkm.keys():
                    # jika ada maka nama_usaha akan sesuai dengan umkm_id yang ada di dalam data umkm
                    nama_usaha = nama_usaha_umkm[umkm_id]
                else:
                    nama_usaha = "-"
                
                for bukprom in bukproms:
                    
                    if lowongan_id == bukprom["lowongan_id"]:
                        status_bukti = bukprom["status_verifikasi"]
                                
                if status_bukti == "Menunggu Peninjauan":
                    emoji = " 🕛"
                
                elif status_bukti == "Disetujui":
                    emoji = " ✅"
                    
                elif status_bukti == "Ditolak":
                    emoji = " ❌ (mohon perbaiki dan kirim ulang)"
                
                else:
                    emoji = " ❌"
                
                print(f"\nId Lowongan #{lowongan_id}")
                print(f"😋 Produk                   : {lowongan['nama_produk']}")
                print(f"🍴 UMKM                     : {nama_usaha}")
                print(f"💲 Anggaran                 : Rp {formatted_budget}")
                print(f"⏳ Deadline                 : {lowongan['batas_waktu_pengerjaan']} hari")
                print(f"📷 Bukti Promosi            : {status_bukti}{emoji}")
        
        while True:
            input_lowongan_id = input("\nMasukan id lowongan untuk mengirim bukti (Tekan ENTER untuk kembali): ")
            
            if not input_lowongan_id:
                break
            
            if not input_lowongan_id.isdigit():
                print("❌ Id hanya boleh angka ❌")
                continue
            
            if input_lowongan_id not in lowongan_vlogger:
                print("❌ Id tidak ditemukan ❌")
                continue
            break
        
        if not input_lowongan_id:
            break
        
        while True:
            link_bukti_promosi = input("Masukan link bukti promosi: ")
            
            if not link_bukti_promosi:
                print("❌ Bukti promosi tidak boleh kosong ❌")
                continue
            break
        
        if input_lowongan_id in bukprom_vlogger:
            
            for bukprom in bukproms:
                
                if input_lowongan_id == bukprom["lowongan_id"]:
                    
                    if bukprom["status_verifikasi"] == "Disetujui":
                        
                        print("\n❌ Bukti sudah disetujui, tidak dapat diubah ❌")
                        input("\nTekan ENTER untuk kembali...")
                        break
                        
                    else:
                        bukprom["status_verifikasi"] = "Menunggu Peninjauan"
                        bukprom["link_konten"] = link_bukti_promosi
            
                        update_bukti_promosi(bukproms)
                        
                        print("\n✅ Bukti berhasil di-update ✅")
                        input("\nTekan ENTER untuk kembali...")
                        break
            
        else:
            
            # generate id baru untuk data yang baru
            if len(bukproms) == 0:
                id_baru = 1
            else:
                id_baru = int(bukproms[-1]["bukti_id"]) + 1
            
            #tanggal upload bukti
            tanggal_upload = datetime.now().strftime("%d-%m-%Y")
            status_verifikasi = "Menunggu Peninjauan"
            
            data_bukti = {
                "bukti_id": id_baru,
                "lowongan_id": input_lowongan_id,
                "link_konten": link_bukti_promosi,
                "tanggal_upload": tanggal_upload,
                "status_verifikasi": status_verifikasi
            }
            
            simpan_bukti_promosi(data_bukti)
            
            print("\n✅ Bukti berhasil di-upload ✅")
            input("\nTekan ENTER untuk kembali...")
            break
