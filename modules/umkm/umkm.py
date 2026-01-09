# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_UMKM

# function untuk mengambil data UMKM
def data_umkm():
    if not os.path.exists(DATA_UMKM):
        return []
    
    with open(DATA_UMKM, mode="r", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# procedure untuk menyimpan data ke dalam file data UMKM
def simpan_umkm(data_baru):
    file_ada = os.path.exists(DATA_UMKM)
        
    with open(DATA_UMKM, mode="a", newline='') as file:
        nama_kolom = data_baru.keys()
        writer = csv.DictWriter(file, fieldnames=nama_kolom)
        
        if not file_ada:
            writer.writeheader()
            
        writer.writerow(data_baru)