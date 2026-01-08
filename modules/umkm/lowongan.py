import csv
import os
from modules.utils import clear_screen, apakah_int
from data.config import DATA_LOWONGAN, DATA_FOOD_VLOGGER, DATA_LAMARAN
from modules.umkm.lamaran import data_lamaran, update_lamaran
from modules.food_vlogger.food_vlogger import data_fv
from modules.bukti_promosi import data_bukti_promosi, tampilkan_bukti
from modules.pembayaran import data_pembayaran
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
        input("\nTekan ENTER untuk kembali ↩")
        return

    umkm_id_login = str(user_session.get("umkm_id", "")).strip()

    if not umkm_id_login:
        print("Silakan login terlebih dahulu.")
        input("\nTekan ENTER untuk kembali ↩")
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
                emoji = "✅" if status_low == "Diambil" else "❌"
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
        status_lowongan = "Belum Diambil"
        
        while True:
            nama_produk = input("Nama Produk: ").capitalize().strip()
            
            if not nama_produk:
                print("❌ Nama produk tidak boleh kosong ❌")
                continue

            # membatasi nama produk maksimal 10 kata
            if len(nama_produk.split()) > 10:
                print("❌ Nama produk maksimal 10 kata ❌")
                continue

            # membatasi nama produk minimum 3 karakter
            if len(nama_produk) < 3:
                print("❌ Nama produk minimal 3 karakter ❌")
                continue
            break
        
        while True:
            kategori = input("Kategori: ").capitalize().strip()
            
            if not kategori:
                print("❌ Kategori tidak boleh kosong ❌")
                continue
                
            # membatasi kategori maksimal 10 kata
            if len(kategori.split()) > 10:
                print("❌ Kategori maksimal 10 kata ❌")
                continue

            # mencegah kategori kurang dari 3 karakter
            if len(kategori) < 3:
                print("❌ Kategori minimal 3 karakter ❌")
                continue
            break
        
        while True:
            deskripsi = input("Deskripsi: ").strip()
            
            if not deskripsi:
                print("❌ Deskripsi tidak boleh kosong ❌")
                continue

            # membatasi deskripsi maksimal 255 kata
            if len(deskripsi.split()) > 255:
                print("❌ Deskripsi maksimal 255 kata ❌")
                continue
            break
        
        while True:
            budget = input("Anggaran Promosi (dalam Rupiah): ").strip()
            
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
            print("[1] Ya")
            print("[2] Buat ulang lowongan")
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
                input("\nTekan ENTER untuk kembali ke beranda...")
                break

            if konfirmasi == 2:
                break
            
        if konfirmasi == 1:
            break
        elif konfirmasi == 2:
            pass

def lamaran_masuk():
    umkm_id = data.session.USER_LOGIN['umkm_id']
    
    # mengambil sumber data
    lowongans = data_lowongan()
    fvs = data_fv()
    lamarans = data_lamaran()
    
    # untuk menyimpan data berdasarkan idnya sendiri
    lowongan_umkm = {}
    vlogger_list = {}
    lamaran_rows = []

    # === LOWONGAN ===
    for lowongan in lowongans:
        if lowongan['umkm_id'] == str(umkm_id):
            lowongan_umkm[lowongan['lowongan_id']] = lowongan

    # === VLOGGER ===
    for fv in fvs:
        vlogger_list[fv['vlogger_id']] = fv
    
    # === LAMARAN ===
    for lamaran in lamarans:
        if lamaran['lowongan_id'] in lowongan_umkm:
            lamaran_rows.append(lamaran)
    
    print("\n===== LAMARAN MASUK =====")    

    # jika tidak ada data lamaran untuk umkm ini
    if not lamaran_rows:
        print("\nBelum ada lamaran masuk.")
        input("\nTekan ENTER untuk kembali ↩")
        return
    
    for lamaran in lamaran_rows:
        lowongan = lowongan_umkm[lamaran['lowongan_id']]
        vlogger = vlogger_list[lamaran['vlogger_id']]

        status_lamaran = lamaran['status']
        emoji = "✅" if status_lamaran == "Disetujui" else "❌"
        
        print(f"""
Id Lamaran #{lamaran['lamaran_id']}
Vlogger    : {vlogger['nama']}
Produk     : {lowongan['nama_produk']}
Tanggal    : {lamaran['tanggal_lamar']}
Status     : {lamaran['status']} {emoji}
------------------------------
""")

    input_lamaran_id = input("Masukkan Lamaran ID untuk disetujui (ENTER untuk batal): ").strip()

    if not input_lamaran_id:
        return

    ditemukan = False

    for lamaran in lamaran_rows:
        if lamaran['lamaran_id'] == input_lamaran_id:
            if lamaran['status'] != 'Pending':
                print("Lamaran ini sudah diproses.")
                return
            lamaran['status'] = 'Disetujui'
            ditemukan = True
            break

    if not ditemukan:
        print("Lamaran ID tidak ditemukan ❌")
        return

    # === SIMPAN ULANG CSV ===
    update_lamaran(lamaran_rows)
    
    print("\n✅ Lamaran berhasil disetujui.")
    input("\nTekan ENTER untuk kembali...")


def kolaborasi():
    
    umkm_id = data.session.USER_LOGIN['umkm_id']

    # mengambil sumber data
    lowongans = data_lowongan()
    fvs = data_fv()
    lamarans = data_lamaran()
    bukproms = data_bukti_promosi()
    pembayarans = data_pembayaran()
    
    # variable untuk menyimpan data yang sesuai
    lowongan_umkm = {}
    vlogger_list = {}
    bukti_list = {}
    pembayaran_list = {}
    kolaborasis = []

    # === LOWONGAN UMKM ===
    for lowongan in lowongans:
        if lowongan['umkm_id'] == str(umkm_id):
            lowongan_umkm[lowongan['lowongan_id']] = lowongan
    
    # === FOOD VLOGGER ===
    for fv in fvs:
        vlogger_list[fv['vlogger_id']] = fv['nama']
    
    # === BUKTI PROMOSI ===
    for bukprom in bukproms:
        
        if bukprom['lowongan_id'] in lowongan_umkm:
            bukti_list[bukprom['lowongan_id']] = bukprom
    
    # === PEMBAYARAN ===
    for pembayaran in pembayarans:
        
        if pembayaran['lowongan_id'] in lowongan_umkm:
            pembayaran_list[pembayaran['lowongan_id']] = pembayaran
    
    # === LAMARAN ===
    for lamaran in lamarans:
        if (
            lamaran['status'] == 'Disetujui' and
            lamaran['lowongan_id'] in lowongan_umkm
        ):
            # kolaborasis berisi data lamaran yang memiliki status = "Disetujui" dan lowongannya milik umkm ini
            kolaborasis.append(lamaran)

    while True:
        clear_screen()
        print("\n===== KOLABORASI SAYA =====")
            
        if not kolaborasis:
            print("\n❌ Belum ada kolaborasi.")
            input("\nTekan ENTER untuk kembali...")
            return

        for kolab in kolaborasis:
            lowongan = lowongan_umkm[kolab['lowongan_id']]
            nama_vlogger = vlogger_list.get(kolab['vlogger_id'], '-')
            
            # penetapan status bukti
            cek_bukti = bukti_list.get(kolab['lowongan_id'], '-')
            if cek_bukti == '-':
                status_bukti = "Belum Ada ❌"
            else:
                status_verifikasi = bukti_list[kolab['lowongan_id']]['status_verifikasi']
                
                if status_verifikasi == 'Menunggu Peninjauan':
                    emoji = "🕛"
                elif status_verifikasi == 'Disetujui':
                    emoji = "✅"
                elif status_verifikasi == 'Ditolak':
                    emoji = "❌"
                    
                status_bukti = f"{status_verifikasi} {emoji}"
            
            # penetapan status pembayaran
            cek_pembayaran = pembayaran_list.get(kolab['lowongan_id'], '-')
            if cek_pembayaran == '-':
                status_pembayaran = 'Belum Lunas ❌'
            else:
                status_pembayaran = 'Lunas ✅'

            print(f"\nId Lowongan #{lowongan['lowongan_id']}")
            print(f"Produk            : {lowongan['nama_produk']}")
            print(f"Vlogger           : {nama_vlogger}")
            print(f"Anggaran          : Rp {lowongan['budget']}")
            print(f"Deadline          : {lowongan['batas_waktu_pengerjaan']} hari")
            print(f"Status Bukti      : {status_bukti}")
            print(f"Status Pembayaran : {status_pembayaran}")
            print("------------------------------")
        
        print("\nPerintah yang tersedia: ")
        print("- bukti <spasi> <id lowongan> -> Melihat bukti")
        print("- bayar <spasi> <id lowongan> -> Membayar lowongan")
        print("- exit                        -> Kembali ke beranda")
        
        while True:
            perintah = input("> ").strip().split()
                    
            if not perintah:
                print("❌ Perintah tidak boleh kosong ❌")
                continue
            
            if not perintah[0].isalpha():
                print("❌ Perintah tidak valid ❌")
                continue
            
            if perintah[0] == "exit":
                break
            
            if len(perintah) == 1:
                print("❌ Id tidak ada ❌")
                continue
            
            if not perintah[1].isdigit():
                print("❌ Id hanya boleh angka ❌")
                continue
            
            if len(perintah) > 2:
                print("❌ Perintah terlalu panjang ❌")
                continue
            
            if perintah[1] not in lowongan_umkm:
                print("❌ Id tidak ditemukan ❌")
                continue
            
            if perintah[0] not in ('bayar', 'bukti'):
                print("❌ Perintah tidak ditemukan ❌")
                continue
            
            break
        
        if perintah[0] == 'bukti':
            input_lowongan_id = perintah[1]
            
            hasil_bukti = tampilkan_bukti(input_lowongan_id)
            
            if hasil_bukti == "setuju":
                print("\n✅ Bukti berhasil disetujui ✅")
                
            elif hasil_bukti == "tolak":
                print("\n✅ Bukti berhasil ditolak ✅")
            
            input("\nTekan ENTER untuk kembali...")
                    
        if perintah[0] == 'bayar':
            print(f"BAYAR COK untuk id {perintah[1]}")
            
            input("\nTekan ENTER untuk kembali...")
            break
        
        if perintah[0] == "exit":
            break