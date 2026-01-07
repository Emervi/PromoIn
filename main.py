from modules.autentikasi.autentikasi import autentikasi_umkm, autentikasi_fv
from modules.utils import clear_screen

# DEBUG BROK
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.food_vlogger import data_fv
from modules.umkm.lowongan import data_lowongan, lamaran_masuk
from modules.umkm.lamaran import data_lamaran

while True:
    clear_screen()
    print("\n========== BERANDA ==========")
    print("Silakan memilih peran yang sesuai dengan anda.")
    print("[1] 🏪 UMKM")
    print("[2] 📸 Food Vlogger")
    print("[3] DEBUG")
    print("[0] Keluar Sistem")
    
    pilihan_user = int(input("> "))
    
    if pilihan_user == 1:
        
        if autentikasi_umkm() == "kill system":
            break
    
    elif pilihan_user == 2:
        
        if autentikasi_fv() == "kill system":
            break
    
    elif pilihan_user == 3:
        
        while True:
            pilihan = input("> ").strip().split()
            
            print(pilihan, len(pilihan))
            
            if not pilihan:
                print("KOSONG COK")
            
            elif not pilihan[0].isalpha():
                print("kata pertama hanya boleh huruf")
                
            elif len(pilihan) == 1:
                print("id tidak ada cok")
            
            elif not pilihan[1].isdigit():
                print("id bukan huruf")
            
            elif len(pilihan) > 2:
                print("kepanjangan cok")
                
            elif pilihan[0] == 'bukti':
                print(f"INI BUKTINYA untuk id {pilihan[1]}")
                
            elif pilihan[0] == 'bayar':
                print(f"BAYAR COK untuk id {pilihan[1]}")
                
            elif pilihan[0] == 'a':
                break
            
            else:
                print("UNKNOWN")
                
    else:
        break


