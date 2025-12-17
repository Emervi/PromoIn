from modules.umkm.umkm import data_umkm, simpan_umkm
from modules.umkm.home import beranda_umkm
from modules.food_vlogger.food_vlogger import data_fv, simpan_fv
from modules.food_vlogger.home import beranda_fv
from modules.utils import clear_screen, apakah_int
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
                
        elif pilihan_user == 9:
            break
        
        elif pilihan_user == 0:
            return "kill system"
        
        else:
            print("Pilihan tidak ditemukan.")



def register_umkm():
    
    clear_screen()
    print("\n===== REGISTER UMKM =====")
    
    # mengambil data umkm yang ada pada file umkm.csv
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
    data.session.USER_LOGIN = data_baru
    
    print("\n✅ Akun Berhasil Dibuat ✅")
    input("\nTekan ENTER untuk lanjut ke halaman beranda...")
    
    return True



def login_umkm():
    
    data_salah = None
    
    while True:
        clear_screen()
        print("\n===== LOGIN UMKM =====")
        
        # mengambil data umkm yang ada pada file umkm.csv
        umkms = data_umkm()
        
        # menampilkan pemberitahuan jika email atau password salah
        if data_salah:
            print("❌ Email atau password salah, silakan masukkan ulang ❌")
            data_salah = False        
        
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
        
        for umkm in umkms:
            
            if input_email == umkm[2] and input_password == umkm[3]:
                
                data.session.USER_LOGIN = umkm
                input("\nTekan ENTER untuk lanjut ke halaman beranda...")
                return True
        
        data_salah = True



# ======================================== FOOD VLOGGER (FV) ========================================
def autentikasi_fv():
    
    while True:
        clear_screen()
        print("\n===== LOGIN & REGISTER FOOD VLOGGER =====")
        print("1. Register Food Vlogger")
        print("2. Login Food Vlogger")
        print("9. Kembali")
        print("0. Keluar Sistem")
        pilihan_user = int(input("Masukan pilihan anda: "))
        
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
                login_fv()
                
        elif pilihan_user == 9:
            break
        
        elif pilihan_user == 0:
            return "kill system"
        
        else:
            print("Pilihan tidak ditemukan.")



def register_fv():
    
    clear_screen()
    print("\n===== REGISTER FOOD VLOGGER =====")
    
    # mengambil data food vlogger yang ada pada file food_vlogger.csv
    fvs = data_fv()
    email_fvs = [] # inisialisasi list untuk email food vlogger
    
    # mengambil semua email food vlogger dan masukan ke dalam email_fvs
    for fv in fvs:
        email_fvs.append(fv[2])
        
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
        if input_email in email_fvs:
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
        
        while True:
            konfirmasi_password = input("Konfirmasi Password: ").strip()

        # mengecek password dengan konfirmasi password
            if input_password != konfirmasi_password:
                print("❌ Konfirmasi password tidak cocok ❌")
            else:
                break
        break
    
    # generate id baru untuk data yang baru
    if apakah_int(fvs[-1][0]):
        id_baru = int(fvs[-1][0]) + 1
    else:
        id_baru = 1
                                
    # memuat data akun
    data_baru = [id_baru, input_nama, input_email, input_password]
    
    # menyimpan data akun
    simpan_fv(data_baru)
    data.session.USER_LOGIN = data_baru
    
    print("✅ Akun Berhasil Dibuat ✅")
    input("\nTekan ENTER untuk lanjut ke halaman beranda...")
    
    return True



def login_fv():
    
    data_salah = None
    
    while True:
        clear_screen()
        print("\n===== LOGIN FOOD VLOGGER =====")
        
        # mengambil data food vlogger yang ada pada file foof_vlogger.csv
        fvs = data_fv()
        
        # menampilkan pemberitahuan jika email atau password salah
        if data_salah:
            print("❌ Email atau password salah, silakan masukan ulang ❌")
            data_salah = False
        
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
                
        for fv in fvs:
            
            if input_email == fv[2] and input_password == fv[3]:
                
                data.session.USER_LOGIN = fv
                input("\nTekan ENTER untuk lanjut ke halaman beranda...")
                return True
            
        data_salah = True