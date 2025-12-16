from modules.autentikasi.autentikasi import autentikasi_umkm, autentikasi_fv
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.food_vlogger import data_fv
from modules.utils import clear_screen

while True:
    clear_screen()
    print("\n========== BERANDA ==========")
    print("Silakan memilih peran yang sesuai dengan anda.")
    print("1. UMKM")
    print("2. Food Vlogger")
    print("3. Daftar UMKM (DEBUG)")
    print("4. Daftar Food Vlogger (DEBUG)")
    print("0. Keluar Sistem")
    
    pilihan_user = int(input("> "))
    
    if pilihan_user == 1:
        
        if autentikasi_umkm() == "kill system":
            break
    
    elif pilihan_user == 2:
        
        if autentikasi_fv() == "kill system":
            break
    
    elif pilihan_user == 3:
        umkms = data_umkm()
        for umkm in umkms:
            print(umkm)

    elif pilihan_user == 4:
        fvs = data_fv()
        for fv in fvs:
            print(fv)
    
    else:
        break