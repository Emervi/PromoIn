import json
from data.config import DATA_UMKM

def load_umkm():
    with open(DATA_UMKM, "r") as f:
        return json.load(f)

def save_umkm(data):
    with open(DATA_UMKM, "w") as f:
        json.dump(data, f, indent=4)

def register_umkm():
    data = load_umkm()
    
    # input umkm baru
    nama = input("Masukan nama anda: ")
    email = input("Masukan email anda: ")
    password = input("Masukan password anda: ")
    
    # generate id baru untuk data
    id_baru = data[-1]["id"] + 1 if data else 1
    
    data_baru = {
        "id": id_baru,
        "nama": nama,
        "email": email,
        "password": password
    }
    
    data.append(data_baru)
    save_umkm(data)

def login_umkm():
    umkms = load_umkm()
    
    email = input("Masukan email: ")
    password = input("Masukan password: ")
    
    for umkm in umkms:
        print(umkm)
        print(email)
        print(password)
        
        if email == umkm["email"] and password == umkm["password"]:
            print(email == umkm["email"])
            print(password == umkm["password"])
            print("BENER NJAY")
            return True
        elif email != umkm["email"] or password != umkm["password"]:
            return print("Email atau password yang dimasukan salah.")