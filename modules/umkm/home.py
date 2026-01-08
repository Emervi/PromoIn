from modules.umkm.lowongan import buat_lowongan, daftar_lowongan, data_lowongan, lamaran_masuk, kolaborasi
from modules.umkm.lamaran import data_lamaran
from modules.utils import clear_screen
import data.session

def jumlah_lowongan(umkm_id):
    
    # sumber data
    lowongans = data_lowongan()
    
    # list untuk menghitung total lowongan umkm ini
    lowongan_saya = []
    
    for lowongan in lowongans:
        
        # mencari lowongan berdasarkan umkm yang sedang login
        if lowongan["umkm_id"] == str(umkm_id):
            
            # memasukan lowongan yang ada ke dalam variable
            lowongan_saya.append(lowongan)
    
    # mengembalikan total lowongan saya
    return len(lowongan_saya)



def jumlah_lamaran(umkm_id):
    
    # sumber data
    lowongans = data_lowongan()
    lamarans = data_lamaran()
    
    # variable untuk menyimpan id data
    lowongan_ids = []
    lamaran_ids = []
    
    for lowongan in lowongans:
        
        # mencari lowongan berdasarkan umkm yang sedang login
        if lowongan["umkm_id"] == str(umkm_id):
            
            # mengambil hanya lowongan_id saja
            lowongan_ids.append(lowongan["lowongan_id"])
    
    for lamaran in lamarans:
        
        # pengecekan kecocokan lowongan_id pada lamaran dengan lowongan_ids
        if lamaran["lowongan_id"] in lowongan_ids:
            
            # mengambil lamaran_id jika lowongan_id cocok dengan lowongan_ids
            lamaran_ids.append(lamaran["lamaran_id"])
            
    # mengembalikan total lamaran
    return len(lamaran_ids)



def beranda_umkm():
    
    umkm_id = data.session.USER_LOGIN["umkm_id"]
    nama_pemilik = data.session.USER_LOGIN["nama"]
    nama_usaha = data.session.USER_LOGIN["nama_usaha"]
    
    while True:
        clear_screen()
        print("\n====== BERANDA UMKM ======")
        print(f"Selamat datang {nama_pemilik}!, pemilik {nama_usaha}")
        print("[1] 📢 Buat Lowongan ")
        print(f"[2] 📝 Lihat Lowongan Saya ({jumlah_lowongan(umkm_id)}) ")
        print(f"[3] 📩 Lamaran Masuk ({jumlah_lamaran(umkm_id)})")
        print("[4] 🤝 Kolaborasi")
        print("[0] Logout")
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            buat_lowongan()

        elif pilihan_user == "2":
            daftar_lowongan()

        elif pilihan_user == "3":
            lamaran_masuk()

        elif pilihan_user == "4":
            kolaborasi()
        
        elif pilihan_user == "0":
            break    
