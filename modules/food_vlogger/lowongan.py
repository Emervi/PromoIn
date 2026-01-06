import csv
import os
from data.config import DATA_LOWONGAN, DATA_FOOD_VLOGGER, DATA_LAMARAN, DATA_UMKM
from modules.utils import clear_screen
from data.config import DATA_LOWONGAN
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.lamaran import data_lamaran,simpan_lamaran
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
            
        if lowongans[i]["status_lowongan"] == "belum diambil":
            
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
            
            print(f"\nLowongan #{lowongans[i]['lowongan_id']}")
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
        print("\n❌ Tidak ada lowongan tersedia.")
        input("\nTekan ENTER untuk kembali...")
        return

    pilihan = input("\nPilih nomor lowongan yang ingin diambil (ENTER untuk kembali): ").strip()

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

    id_lowongan_asli = lowongans[index]["lowongan_id"].strip()

    if index < 0 or index >= len(lowongans):
        print("❌ Nomor lowongan tidak valid.")
        input("Tekan ENTER untuk kembali...")
        return

    if lowongans[index]["status_lowongan"] != "belum diambil":
        print("Lowongan sudah diambil.")
        input("Tekan ENTER untuk kembali...")
        return

    lowongans[index]["status_lowongan"] = "diambil"
    
    with open(DATA_LOWONGAN, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = lowongans[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lowongans)

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

    print("✅ Lowongan berhasil diambil, Tunggu persetujuan dari UMKM!")
    input("Tekan ENTER untuk kembali...")


def kolaborasi():
    vlogger_id = data.session.USER_LOGIN['vlogger_id']

    lowongan_list = {}
    vlogger_list = {}
    umkm_list = {}
    kolaborasi = []

    # === LOWONGAN ===
    with open(DATA_LOWONGAN, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lowongan_list[row['lowongan_id']] = row

    # === FOOD VLOGGER ===
    with open(DATA_FOOD_VLOGGER, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vlogger_list[row['vlogger_id']] = row['nama']

    # === UMKM ===
    with open(DATA_UMKM, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            umkm_list[row['umkm_id']] = row['nama_usaha']

    # === LAMARAN ===
    with open(DATA_LAMARAN, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        all_rows = list(reader)

    if 'status_bukti' not in fieldnames:
        fieldnames.append('status_bukti')

    if 'link_bukti' not in fieldnames:
        fieldnames.append('link_bukti')

    for row in all_rows:
        if row['status'] == 'Disetujui' and row['vlogger_id'] == str(vlogger_id):
            kolaborasi.append(row)

    clear_screen()
    print("\n===== KOLABORASI SAYA =====")

    if not kolaborasi:
        print("Belum ada kolaborasi, silakan tunggu persetujuan dari UMKM!")
        input("\nENTER untuk kembali...")
        return

    for item in kolaborasi:
        lowongan = lowongan_list[item['lowongan_id']]
        umkm_nama = umkm_list.get(lowongan['umkm_id'], '-')
        status_bukti = item.get('status_bukti', '')

        print(f"""
😋 Produk       : {lowongan['nama_produk']}
🍴 UMKM         : {umkm_nama}
💲 Anggaran     : Rp{lowongan['budget']}
⏳ Deadline     : {lowongan['batas_waktu_pengerjaan']} hari
""")

        if status_bukti == 'Menunggu Persetujuan':
            print("Status Bukti : Menunggu Persetujuan 🕛")
        elif status_bukti == 'Disetujui':
            print("Status Bukti : Disetujui ✅")
        else:
            print("[1] Upload Bukti")
            print("[0] Lewati")

            pilihan = input("> ")
            if pilihan == '1':
                link = input("Masukkan link bukti promosi: ").strip()
                if link:
                    item['link_bukti'] = link
                    item['status_bukti'] = 'Menunggu Persetujuan'
                    print("Bukti berhasil diupload ✅, menunggu persetujuan dari UMKM 🕛.")

    # === SIMPAN CSV ===
    with open(DATA_LAMARAN, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    input("\nENTER untuk kembali...")




    
    

