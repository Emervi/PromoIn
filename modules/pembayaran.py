# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_PEMBAYARAN

# function untuk mengambil data pembayaran
def data_pembayaran():
    if not os.path.exists(DATA_PEMBAYARAN):
        return []
    
    with open(DATA_PEMBAYARAN, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# procedure untuk menyimpan data ke dalam file data pembayaran
def simpan_pembayaran(data_baru):
    file_ada = os.path.exists(DATA_PEMBAYARAN)
        
    with open(DATA_PEMBAYARAN, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)

# procedure untuk mengupdate data pembayaran
def update_pembayaran(data_baru):

    with open(DATA_PEMBAYARAN, mode="w", newline='') as file:
        nama_kolom = data_baru[0].keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)        
        writer.writeheader()
        writer.writerows(data_baru)