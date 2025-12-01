import json

from crud.umkm_crud import load_umkm

umkms = load_umkm()

for data in umkms:
    print(data)