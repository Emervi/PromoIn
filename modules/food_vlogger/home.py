from modules.food_vlogger.lowongan import daftar_lowongan
from modules.utils import clear_screen

def beranda_fv():
    
    while True:
        
        clear_screen()
        print("\n===== BERANDA FOOD VLOGGER =====")
        print("1. Lihat lowongan")
        print("3. Lowongan Selesai ✅")
        print("0. Logout")
        print("Selamat datang, masih kosong cihuy!!")
        pilihan_user = int(input("> "))
        #diambil atau belum diambil 
        
        if pilihan_user == 1:
            daftar_lowongan()
        
        elif pilihan_user == 0:
            break
        
        elif pilihan_user == 3:
            lowongan_selesai()