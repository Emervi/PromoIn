def beranda_fv():
    while True:
        print("\n===== DASHBOARD FOOD VLOGGER =====")
        print("1. Home")
        print("2. Konten")
        print("3. Daftar Lowongan")
        print("4. Settings")
        print("0. Logout")
        print("Selamat datang, masih kosong cihuy!!")
        pilihan_user = int(input("> "))
        #diambil atau belum diambil 
        if pilihan_user == 0:
            break
        elif pilihan_user == 1:
            print("--Home--")
            break
    
        elif pilihan_user == 2:
            print("--Konten--")
            break
    
        elif pilihan_user == 3:
            print("--Daftar Lowongan--")
            break
    
        elif pilihan_user == 4:
            print("--Settings--")
            break

        else:
            print("Error!")
            break
