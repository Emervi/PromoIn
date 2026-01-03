from modules.umkm.umkm import data_umkm, simpan_umkm
from modules.umkm.home import beranda_umkm
from modules.food_vlogger.food_vlogger import data_fv, simpan_fv
from modules.food_vlogger.home import beranda_fv
from modules.utils import clear_screen, apakah_int, input_password, format_email
import data.session



# ======================================== UMKM ========================================
def autentikasi_umkm():
    
    while True:
        clear_screen()
        print("\n===== LOGIN & REGISTER UMKM =====")
        print("1. Register UMKM")
        print("2. Login UMKM")
        print("9. Kembali")
        print("0. Keluar Sistem")
        pilihan_user = int(input("> "))
        
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
                autentikasi_umkm()
                
        elif pilihan_user == 9:
            break
        
        elif pilihan_user == 0:
            return "kill system"
        
        else:
            print("❌ Pilihan tidak valid ❌")



def register_umkm():
    
    clear_screen()
    print("\n===== REGISTER UMKM =====")
    
    # mengambil data umkm yang ada pada file umkm.csv
    umkms = data_umkm()
    email_umkms = [] # inisialisasi list untuk email umkm
    
    # mengambil semua email umkm dan masukan ke dalam email_umkms
    for umkm in umkms:
        email_umkms.append(umkm["email"])
    
    # meminta input nama usaha
    while True:
        input_nama_usaha = input("Nama Usaha: ").capitalize().strip()
        
        # mengecek jika nama usaha kosong
        if not input_nama_usaha:
            print("❌ Nama usaha tidak boleh kosong ❌")
            continue
        
        # mengecek format nama usaha
        if '@' in input_nama_usaha or '.' in input_nama_usaha:
            print("❌ Format nama usaha keliru ❌")
            continue
        break
    
    # meminta input nama
    while True:
        input_nama = input("Nama: ").capitalize().strip()
        
        # mengecek jika nama kosong
        if not input_nama:
            print("❌ Nama tidak boleh kosong ❌")
            continue
        
        # mengecek jika nama hanya mengandung huruf dan angka
        if not input_nama.replace(" ", "").isalnum():
            print("❌ Nama hanya boleh mengandung huruf dan angka ❌")
            continue

        if '@' in input_nama or '.' in input_nama:
            print("❌ Format nama keliru ❌")
            continue
        break
    
    # meminta input email
    while True:
        input_email = input("Email: ").lower().strip()
        
        # mengecek format email
        if format_email(input_email) == False:
            continue
        
        # mengecek jika email sudah terdaftar
        if input_email in email_umkms:
            print("❌ Email sudah terdaftar ❌")
            continue
        break
    
    # meminta input password
    while True:
        input_password_user = input_password("Password: ").strip()
        
        # mengecek jika password kosong
        if not input_password_user:
            print("❌ Password tidak boleh kosong ❌")
            continue
        
        # mengecek panjang password
        if len(input_password_user) < 8:
            print("❌ Panjang password kurang dari 8 karakter ❌")
            continue
        
        konfirmasi_password = input_password("Konfirmasi Password: ").strip()

        # mengecek password dengan konfirmasi password
        if input_password_user != konfirmasi_password:
            print("❌ Konfirmasi password tidak cocok ❌")
            continue
        break
    
    # generate id baru untuk data yang baru
    if len(umkms) == 0:
        id_baru = 1
    else:
        id_baru = int(umkms[-1]["umkm_id"]) + 1        
                                
    # memuat data akun
    data_baru = {
        "umkm_id": id_baru,
        "nama": input_nama,
        "email": input_email,
        "password": input_password_user,
        "alamat": "-",
        "lokasi": "-",
        "nama_usaha": input_nama_usaha,
        "deskripsi_usaha": "-"
    }
    
    # menyimpan data akun
    simpan_umkm(data_baru)
    data.session.USER_LOGIN = data_baru
    
    print("\n✅ Akun Berhasil Dibuat ✅")
    input("\nTekan ENTER untuk lanjut ke halaman beranda...")
    
    return True



def login_umkm():
    
    while True:
        clear_screen()
        print("\n===== LOGIN UMKM =====")
        
        # mengambil data umkm yang ada pada file umkm.csv
        umkms = data_umkm()
                
        # meminta input email
        while True:
            input_email = input("Email: ").lower().strip()
            
            # mengecek jika email kosong
            if not input_email:
                print("❌ Email tidak boleh kosong ❌")
                continue
            
            # mengecek format email
            if format_email(input_email) == False:
                continue         
            break
        
        # meminta input password
        while True:
            input_password_user = input_password("Password: ").strip()

            if not input_password_user:
                print("❌ Password tidak boleh kosong ❌")
                continue
            if len(input_password_user) < 8:
                print("❌ Panjang password kurang dari 8 karakter ❌")
                continue
            break
        
        for umkm in umkms:
            
            if input_email == umkm["email"] and input_password_user == umkm["password"]:
                
                data.session.USER_LOGIN = umkm
                
                print("\n✅ Login Berhasil ✅")
                input("\nTekan ENTER untuk lanjut ke halaman beranda...")
                return True
        
        # ketika email atau password yang dimasukan user salah
        print("\n❌ Email atau password salah, silakan masukan ulang ❌")
        
        print("\n1. Kembali ke halaman Login & Register UMKM")
        print("*. Tekan ENTER untuk lanjut mengisi form login")
        
        lanjut_isi = input("> ")
        
        if apakah_int(lanjut_isi):
            lanjut_isi = int(lanjut_isi)
            
            if lanjut_isi == 1:
                return False
        else:
            pass


# ======================================== FOOD VLOGGER (FV) ========================================
def autentikasi_fv():
    
    while True:
        clear_screen()
        print("\n===== LOGIN & REGISTER FOOD VLOGGER =====")
        print("1. Register Food Vlogger")
        print("2. Login Food Vlogger")
        print("9. Kembali")
        print("0. Keluar Sistem")
        pilihan_user = int(input("> "))
        
        if pilihan_user == 1:
            akun_fv = register_fv()
            
            if akun_fv:
                beranda_fv()
            else:
                register_fv()
            
        elif pilihan_user == 2:
            akun_fv = login_fv()
            
            if akun_fv:
                beranda_fv()
            else:
                autentikasi_fv()
                
        elif pilihan_user == 9:
            break
        
        elif pilihan_user == 0:
            return "kill system"
        
        else:
            print("❌ Pilihan tidak valid ❌")



def register_fv():
    
    clear_screen()
    print("\n===== REGISTER FOOD VLOGGER =====")
    
    # mengambil data food vlogger yang ada pada file food_vlogger.csv
    fvs = data_fv()
    email_fvs = [] # inisialisasi list untuk email food vlogger
    
    # mengambil semua email food vlogger dan masukan ke dalam email_fvs
    for fv in fvs:
        email_fvs.append(fv["email"])
        
    # meminta input nama
    while True:
        input_nama = input("Nama: ").capitalize().strip()
        
        # mengecek jika nama kosong
        if not input_nama:
            print("❌ Nama tidak boleh kosong ❌")
            continue
        
        if '@' in input_nama or '.' in input_nama:
            print("❌ Format nama keliru ❌")
            continue
        break
    
    # meminta input email
    while True:
        input_email = input("Email: ").lower().strip()
        
        # mengecek format email
        if format_email(input_email) == False:
            continue
        
        # mengecek jika email sudah terdaftar
        if input_email in email_fvs:
            print("❌ Email sudah terdaftar ❌")
            continue
        break
        
    # meminta input password
    while True:
        input_password_user = input_password().strip()

        # mengecek jika password kosong
        if not input_password_user:
            print("❌ Password tidak boleh kosong ❌")
            continue
        
        # mengecek panjang password
        if len(input_password_user) < 8:
            print("❌ Panjang password kurang dari 8 karakter ❌")
            continue
    
        konfirmasi_password = input_password("Konfirmasi Password: ").strip()

        # mengecek password dengan konfirmasi password
        if input_password_user != konfirmasi_password:
            print("❌ Konfirmasi password tidak cocok ❌")
            continue
        break
    
    # generate id baru untuk data yang baru
    if len(fvs) == 0:
        id_baru = 1
    else:
        id_baru = int(fvs[-1]["vlogger_id"]) + 1
                                 
    # memuat data akun
    data_baru = {
        "vlogger_id": id_baru,
        "nama": input_nama,
        "email": input_email,
        "password": input_password_user
    }
    
    # menyimpan data akun
    simpan_fv(data_baru)
    data.session.USER_LOGIN = data_baru
    
    print("\n✅ Akun Berhasil Dibuat ✅")
    input("\nTekan ENTER untuk lanjut ke halaman beranda...")
    
    return True

    



def login_fv():
    
    while True:
        clear_screen()
        print("\n===== LOGIN FOOD VLOGGER =====")
        
        # mengambil data food vlogger yang ada pada file foof_vlogger.csv
        fvs = data_fv()
                
        # meminta input email
        while True:
            input_email = input("Email: ").lower().strip()
            
            # mengecek jika email kosong
            if not input_email:
                print("❌ Email tidak boleh kosong ❌")
                continue
            
            # mengecek format email
            if format_email(input_email) == False:
                continue            
            break
        
        # meminta input password
        while True:
            input_password_user = input_password("Password: ").strip()

            # mengecek jika password kosong
            if not input_password_user:
                print("❌ Password tidak boleh kosong ❌")
                continue
            
            # mengecek panjang password
            if len(input_password_user) < 8:
                print("❌ Panjang password kurang dari 8 karakter ❌")
                continue
            break
                
        for fv in fvs:
            
            if input_email == fv["email"] and input_password_user == fv["password"]:
                
                data.session.USER_LOGIN = fv
                
                print("\n✅ Login Berhasil ✅")
                input("\nTekan ENTER untuk lanjut ke halaman beranda...")
                return True
        
        # ketika email atau password yang dimasukan user salah
        print("\n❌ Email atau password salah, silakan masukan ulang ❌")
        
        print("\n1. Kembali ke halaman Login & Register UMKM")
        print("*. Tekan ENTER untuk lanjut mengisi form login")
        
        lanjut_isi = input("> ")
        
        if apakah_int(lanjut_isi):
            lanjut_isi = int(lanjut_isi)
            
            if lanjut_isi == 1:
                return False
        else:
            pass
