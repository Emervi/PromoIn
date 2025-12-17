from modules.food_vlogger.lowongan import lihat_lowongan
from modules.utils import clear_screen

def beranda_fv():
    
    while True:
        clear_screen()
        print("\n===== BERANDA FOOD VLOGGER =====")
        print("0. Logout")
        print("1. Lihat lowongan")
        print("Selamat datang, masih kosong cihuy!!")
        pilihan_user = int(input("> "))
        #diambil atau belum diambil 
        if pilihan_user == 0:
            break

        elif pilihan_user == 1:
            lihat_lowongan()
        