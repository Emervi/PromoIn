from modules.autentikasi.autentikasi import autentikasi_umkm
from modules.umkm.umkm import data_umkm

while True:

    # debug untuk melihat data umkm
    # umkms = data_umkm()
    # print(umkms)
    
    print("\n========== BERANDA ==========")
    print("Silakan memilih peran yang sesuai dengan anda.")
    print("1. UMKM")
    print("2. Food Vlogger")
    print("0. Keluar Sistem")
    
    pilihan_user = int(input("> "))
    
    if pilihan_user == 1:
        
        if autentikasi_umkm() == "kill system":
            break
    
    # ISI UNTUK AUTENTIKASI FOOD VLOGGER (FV)
    elif pilihan_user == 2:
        pass
    
    elif pilihan_user == 3:
        pass
    
    else:
        break