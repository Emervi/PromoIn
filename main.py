from modules.autentikasi.autentikasi import autentikasi_umkm, autentikasi_fv
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.food_vlogger import data_fv
from modules.utils import clear_screen
from modules.umkm.lowongan import data_lowongan

while True:
    clear_screen()
    print("\n========== BERANDA ==========")
    print("Silakan memilih peran yang sesuai dengan anda.")
    print("[1] 🏪 UMKM")
    print("[2] 📸 Food Vlogger")
    print("[3] Daftar UMKM (DEBUG)")
    print("[4] Daftar Food Vlogger (DEBUG)")
    print("[5] Daftar Lowongan (DEBUG)")
    print("[6] Fitur Bayar FV (DEBUG)")
    print("[0] Keluar Sistem")
    
    pilihan_user = int(input("> "))
    
    if pilihan_user == 1:
        
        if autentikasi_umkm() == "kill system":
            break
    
    elif pilihan_user == 2:
        
        
        if autentikasi_fv() == "kill system":
            break
    
    elif pilihan_user == 3:
        umkms = data_umkm()
        print("Panjang data UMKM: ", len(umkms))
        for umkm in umkms:
            print(umkm)
        input("ENTER")
        break

    elif pilihan_user == 4:
        fvs = data_fv()
        for fv in fvs:
            print(fv)
    
    elif pilihan_user == 5:
        lowongans = data_lowongan()
        umkms = data_umkm()
        
        umkm_ids = {}
        
        for umkm in umkms:
            umkm_ids[umkm["umkm_id"]] = umkm["nama_usaha"]
                    
        print(f"DATA UMKK IDS{umkm_ids}")
        for i in range(0, len(lowongans)):
            
            if lowongans[i]["status_lowongan"] == "belum diambil":
                print(f"\n#{lowongans[i]["lowongan_id"]}")
                
                umkm_id = lowongans[i]["umkm_id"]
                
                if umkm_id in umkm_ids.keys():
                    nama_usaha = umkm_ids[umkm_id]
                else:
                    nama_usaha = "kosong atau dihapus"
                    
                print(f"Nama Usaha: {nama_usaha}")
                
        input("ENTER")
    
    else:
        break


