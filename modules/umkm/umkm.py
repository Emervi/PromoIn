# mengimport library csv untuk mengelola file csv
import csv

# mengimport library os yang dapat menjalankan fungsi yang berhubungan dengan operating system
import os

# mengambil path data di dalam folder data/config
from data.config import DATA_UMKM

# function untuk mengambil data UMKM
def data_umkm():
    data = []
    
    if not os.path.exists(DATA_UMKM):
        return []
    
    with open(DATA_UMKM, mode="r", newline='') as f:
        reader = csv.reader(f)
        for baris in reader:
            data.append(baris)
            
    return data

# procedure untuk menyimpan data ke dalam file data UMKM
def simpan_umkm(data_user):
    with open(DATA_UMKM, mode="a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data_user)