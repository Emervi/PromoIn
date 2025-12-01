import json

from crud.umkm_crud import load_umkm
from crud.food_vlogger_crud import load_fv

umkms = load_umkm()
fvs = load_fv()

for data in umkms:
    print(data)

for data in fvs:
    print(data)