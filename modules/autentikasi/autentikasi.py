import json

from modules.umkm.umkm import data_umkm, simpan_umkm
from modules.umkm.home import beranda_umkm

def cek_ketersedian_email(email):
    pass



def apakah_int(nilai):
    try:
        int(nilai)
        return True
    
    except ValueError:
        return False



def pilih_peran():
    print(data_umkm())
    
    print("\n===== BERANDA =====")
    print("Silakan memilih peran yang sesuai dengan anda.")
    print("1. UMKM")
    print("2. Food Vlogger")
    print("0. Keluar Sistem")
    pilihan_user = int(input("Masukan pilihan anda: "))
    
    if pilihan_user == 1:
        return "UMKM"
    
    elif pilihan_user == 2:
        return "FV"
    
    else:
        return 0



def autentikasi_umkm():
    
    while True:
        print("\n===== LOGIN & REGISTER UMKM =====")
        print("1. Register UMKM")
        print("2. Login UMKM")
        print("9. Kembali")
        print("0. Keluar Sistem")
        pilihan_user = int(input("Masukan pilihan anda: "))
        
        if pilihan_user == 1:
            akun_umkm = register_umkm()
            
            if akun_umkm:
                beranda_umkm()
            else:
                register_umkm()
            
        elif pilihan_user == 2:
            akun_umkm = login_umkm()
            
            if akun_umkm:
                beranda_umkm()
            else:
                login_umkm()
        
        elif pilihan_user == 3:
            pass
        
        elif pilihan_user == 9:
            break
        
        elif pilihan_user == 0:
            return "kill system"
        
        else:
            print("Pilihan tidak ditemukan.")



def register_umkm():
    
    while True:
        print("\n===== REGISTER UMKM =====")
        
        # mengambil data umkm yang ada pada file umkm.json
        umkms = data_umkm()
        email_umkms = [] # inisialisasi list untuk email umkm
        
        # mengambil semua email umkm dan masukan ke dalam email_umkms
        for umkm in umkms:
            email_umkms.append(umkm[2])
            
        # meminta input nama
        while True:
            input_nama = input("Nama: ").capitalize().strip()
            
            # mengecek jika nama kosong
            if not input_nama:
                print("❌ Nama tidak boleh kosong ❌")
                continue
            break
        
        # meminta input email
        while True:
            input_email = input("Email: ").lower().strip()
            
            # mengecek jika email kosong
            if not input_email:
                print("❌ Email tidak boleh kosong ❌")
                continue
            
            # mengecek format email
            if '@' not in input_email or '.' not in input_email:
                print("❌ Format email salah ❌")
                continue
            
            # mengecek jika email sudah terdaftar
            if input_email in email_umkms:
                print("❌ Email sudah terdaftar ❌")
                continue
            break
        
        # meminta input password
        while True:
            input_password = input("Password: ").strip()
            
            # mengecek jika password kosong
            if not input_password:
                print("❌ Password tidak boleh kosong ❌")
                continue
            
            # mengecek panjang password
            if len(input_password) < 8:
                print("❌ Panjang password kurang dari 8 karakter ❌")
                continue
            
            konfirmasi_password = input("Konfirmasi Password: ").strip()

            # mengecek password dengan konfirmasi password
            if input_password != konfirmasi_password:
                print("❌ Konfirmasi password tidak cocok ❌")
                continue
            break
        
        # generate id baru untuk data yang baru
        if apakah_int(umkms[-1][0]):
            id_baru = int(umkms[-1][0]) + 1
        else:
            id_baru = 1
                                    
        # memuat data akun
        data_baru = [id_baru, input_nama, input_email, input_password]
        
        # menyimpan data akun
        simpan_umkm(data_baru)
        print("✅ Akun Berhasil Dibuat ✅")
        return True



def login_umkm():
    
    while True:
        print("\n===== LOGIN UMKM =====")
        
        # mengambil data umkm yang ada pada file umkm.json
        umkms = data_umkm()
        
        # meminta input email
        while True:
            input_email = input("Email: ").lower().strip()
            
            # mengecek jika email kosong
            if not input_email:
                print("❌ Email tidak boleh kosong ❌")
                continue
            
            # mengecek format email
            if '@' not in input_email or '.' not in input_email:
                print("❌ Format email salah ❌")
                continue            
            break
        
        # meminta input password
        while True:
            input_password = input("Password: ").strip()
            
            # mengecek jika password kosong
            if not input_password:
                print("❌ Password tidak boleh kosong ❌")
                continue
            
            # mengecek panjang password
            if len(input_password) < 8:
                print("❌ Panjang password kurang dari 8 karakter ❌")
                continue
            break
        
        print("Email: ", input_email)
        print("Password: ", input_password)
        
        for umkm in umkms:
            
            if input_email == umkm[2] and input_password == umkm[3]:
                return True
            
        print("❌ Email atau password salah ❌")