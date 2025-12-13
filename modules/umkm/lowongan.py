import json
import os

from data.config import DATA_LOWONGAN

def load_lowongan():
    if not os.path.exists(DATA_LOWONGAN):
        return []
    with open(DATA_LOWONGAN, "r") as f:
        return json.load(f)

def save_lowongan(data):
    with open(DATA_LOWONGAN, "w") as f:
        json.dump(data, f, indent=4)


# Dashboard UMKM
def dashboard_umkm(user):
    """
    user = data UMKM hasil login dari temanmu
    contoh:
    user = { "id": "U001", "nama": "Bakso Jago" }
    """
    while True:
        print("\n=== DASHBOARD UMKM ===")
        print(f"Login sebagai: {user['nama']}")
        print("1. Buat Lowongan Promosi")
        print("2. Lihat Status Lowongan")
        print("3. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            buat_lowongan(user)
        elif pilih == "2":
            lihat_status(user)
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")


# Buat Lowongan Promosi
def buat_lowongan(user):
    print("\n=== BUAT LOWONGAN PROMOSI ===")

    nama_produk = input("Nama produk                 : ")
    deskripsi = input("Deskripsi promosi           : ")
    budget = input("Budget yang ditawarkan      : ")
    deadline = input("Deadline promosi (YYYY-MM-DD) : ")
    followers = input("Syarat minimal followers    : ")

    data = load_lowongan()

    id_baru = f"L{len(data)+1:03}"

    data.append({
        "id": id_baru,
        "umkm_id": user["id"], 
        "nama_produk": nama_produk,
        "deskripsi": deskripsi,
        "budget": budget,
        "deadline": deadline,
        "syarat_followers": followers,
        "status": "belum diambil"
    })

    save_lowongan(data)

    print("\nLowongan berhasil dibuat!")


# Lihat Status Lowongan
def lihat_status(user):
    print("\n=== STATUS LOWONGAN ===")

    data = load_lowongan()

    ada = False
    for d in data:
        if d["umkm_id"] == user["id"]:
            ada = True
            print(f"\nID: {d['id']}")
            print(f"Produk : {d['nama_produk']}")
            print(f"Budget : {d['budget']}")
            print(f"Deadline: {d['deadline']}")
            print(f"Status : {d['status']}")

    if not ada:
        print("Belum ada lowongan dari UMKM ini.")
