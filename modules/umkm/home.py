from modules.umkm.lowongan import buat_lowongan, daftar_lowongan, data_lowongan
from modules.utils import clear_screen
import data.session

def beranda_umkm():
    
    while True:
        clear_screen()
        print("\n====== BERANDA UMKM ======")
        print("1. Buat Lowongan")
        print("2. Lihat Lowongan")
        print("3. Lamaran Masuk")
        print("4. Cek Akun (DEBUG)")
        print("5. Cek Lowongan (DEBUG)")
        print("0. Logout")
        pilihan_user = int(input("> "))
        
        if pilihan_user == 1:
            buat_lowongan()

        elif pilihan_user == 2:
            daftar_lowongan()
        
        elif pilihan_user == 4:
            print(data.session.USER_LOGIN)
            input("ENTER")
            
        elif pilihan_user == 5:
            lowongans = data_lowongan()
            
            lowongan_kosong = []
            
            for low in lowongans:
                if low[6] == "belum diambil":
                    print(low)
                    # lowongan_kosong.append(low)
                # print(low)
                # print(low[6])
                # print(lowongan_kosong)
            input("ENTER")
        
        elif pilihan_user == 0:
            break    
