import data.session
from modules.umkm.lowongan.lowongan import buat_lowongan, lihat_lowongan

def beranda_umkm():
    while True:
        print("\n===== BERANDA UMKM =====")
        print("0. Logout")
        print("1. Buat Lowongan")
        print("2. Lihat Lowongan")
        print("Selamat datang, masih kosong cihuy!!")
        pilihan_user = int(input("> "))
        
        if pilihan_user == 0:
            print(data.session.USER_LOGIN)
            break

        elif pilihan_user == 1:
            buat_lowongan()

        elif pilihan_user == 2:
            lihat_lowongan()