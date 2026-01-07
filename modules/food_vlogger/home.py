from modules.food_vlogger.lowongan import daftar_lowongan, kolaborasi
from modules.food_vlogger.lowongan_berlangsung import lowongan_berlangsung
from modules.utils import clear_screen
import data.session

def beranda_fv():
    
    while True:
        
        nama_fv = data.session.USER_LOGIN["nama"]
        
        clear_screen()
        print("\n===== BERANDA FOOD VLOGGER =====")
        print(f"Selamat datang {nama_fv}!")
        print("[1] 📢 Lihat lowongan ")
        # print("[2] 🕛 Lowongan Berlangsung ")
        print("[2] 🤝 Kolaborasi ")
        print("[0] Logout")
        pilihan_user = int(input("> "))
        
        if pilihan_user == 1:
            daftar_lowongan()
        
        elif pilihan_user == 2:
            kolaborasi()
        
        elif pilihan_user == 0:
            break