from modules.autentikasi.autentikasi import autentikasi_umkm, autentikasi_fv
from modules.utils import clear_screen

# DEBUG BROK
from modules.umkm.umkm import data_umkm
from modules.food_vlogger.food_vlogger import data_fv
from modules.umkm.lowongan import data_lowongan, lamaran_masuk
from modules.umkm.lamaran import data_lamaran

while True:
    clear_screen()
    print("\n========== BERANDA ==========")
    print("Silakan memilih peran yang sesuai dengan Anda.")
    print("[1] 🏪 UMKM")
    print("[2] 📸 Food Vlogger")
    print("[0] 🚪 Keluar Sistem")
    
    while True:
        pilihan_user = input("> ")
        
        if not pilihan_user:
            print("❌ Input tidak boleh kosong ❌")
            continue
        
        if pilihan_user not in ("1", "2", "0"):
            print("❌ Input tidak valid ❌")
            continue
        break
    
    if pilihan_user == "1":
        if autentikasi_umkm() == "kill system":
            break
    
    if pilihan_user == "2":
        if autentikasi_fv() == "kill system":
            break
    
    if pilihan_user == "0":
        print("\nTerima Kasih Telah Menggunakan Aplikasi PromoIn! 🥰😘😍")
        break
    
    if pilihan_user not in ("0", "1", "2"):
        print("❌ Pilihan tidak valid ❌")
        continue


