import json

from crud.umkm_crud import load_umkm, register_umkm, login_umkm
from crud.food_vlogger_crud import load_fv, register_fv

SISTEM = True
HALAMAN_HOME = True
HALAMAN_REGISTER = False
HALAMAN_LOGIN = False
HALAMAN_BERANDA = False

while SISTEM:
    
    umkms = load_umkm()
    for data in umkms:
        print(data)
        print(data["password"])
        
    while HALAMAN_HOME:
        print("\n===== BERANDA =====")
        print("1. Register")
        print("2. Login")
        print("0. Keluar Sistem")
        pilihan_beranda = int(input("Masukan pilihan anda: "))
        
        if pilihan_beranda == 1:
            HALAMAN_REGISTER = True
            HALAMAN_HOME = False
            print("gis")

        elif pilihan_beranda == 2:
            HALAMAN_LOGIN = True
            HALAMAN_HOME = False
            print("gin")
            
        elif pilihan_beranda == 0:
            SISTEM = False
            HALAMAN_HOME = False
            print("out")
            
        else:
            print("Pilihan tidak tersedia.")

    while HALAMAN_REGISTER:
        print("\n===== REGISTER =====")
        print("1. Register UMKM")
        print("2. Register Food Vlogger")
        print("3. Login")
        print("0. Keluar Sistem")
        pilihan_user = int(input("Masukan pilihan anda: "))
        
        if pilihan_user == 1:
            register_umkm()
            HALAMAN_REGISTER = False
            HALAMAN_LOGIN = True
            
        elif pilihan_user == 2:
            register_fv()
            HALAMAN_REGISTER = False
            HALAMAN_LOGIN = True
        
        elif pilihan_user == 3:
            HALAMAN_REGISTER = False
            HALAMAN_LOGIN = True
            
        elif pilihan_user == 0:
            SISTEM = False
            break
        
        else:
            print("Pilihan tidak tersedia.")

    while HALAMAN_LOGIN:
        print("\n===== LOGIN =====")
        print("1. Login UMKM")
        print("2. Login Food Vlogger")
        print("3. Register")
        print("0. Keluar Sistem")
        pilihan_user = int(input("Masukan pilihan anda: "))
        
        if pilihan_user == 1:
            
            if login_umkm():
                print("Hai")
            else:
                print("GAGAL NJAY")
        
        elif pilihan_user == 2:
            pass
        
        elif pilihan_user == 3:
            HALAMAN_REGISTER = True
            HALAMAN_LOGIN = False
            
        elif pilihan_user == 0:
            SISTEM = False
            break
        
        else:
            print("Pilihan tidak tersedia.")
    
    while HALAMAN_BERANDA:
        print("SELAMAT DATANG UMKM!")
        
    print("KOCAK BANGET!")
