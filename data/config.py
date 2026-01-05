DATA_ADMIN = "data/admin.csv"
DATA_AKUN_SOSMED = "data/akun_sosmed.csv"
DATA_BUKTI_PROMOSI = "data/bukti_promosi.csv"
DATA_FOOD_VLOGGER = "data/food_vlogger.csv"
DATA_LAMARAN = "data/lamaran.csv"
DATA_LOWONGAN = "data/lowongan.csv"
DATA_PEMBAYARAN = "data/pembayaran.csv"
DATA_PLATFORM = "data/platform.csv"
DATA_UMKM = "data/umkm.csv"

"""
Status lowongan:
- belum diambil (terbuka - pada saat lowongan baru dibuat / pada saat lamaran ditolak)
- diambil (berlangsung - pada saat lamaran disetujui oleh UMKM)
- selesai (pada saat lowongan sudah dibayarkan)

Status lamaran:
- terkirim (pada saat FV mengirim lamaran)
- disetujui (pada saat lamaran FV disetujui)
- ditolak (pada saat lamaran FV ditolak)

Status bukti:
- menunggu (pada saat FV dapet lowongan hingga FV menunggu verifikasi)
- disetujui (pada saat disetujui)
- ditolak (pada saat ditolak)
"""