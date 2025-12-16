from modules.food_vlogger.lowongan import lihat_lowongan

def beranda_fv():
    while True:
        print("\n===== BERANDA FOOD VLOGGER =====")
        print("0. Logout")
        print("1. Lihat lowongan")
        print("Selamat datang, masih kosong cihuy!!")
        pilihan_user = int(input("> "))
        
        if pilihan_user == 0:
            break

        elif pilihan_user == 1:
            lihat_lowongan()