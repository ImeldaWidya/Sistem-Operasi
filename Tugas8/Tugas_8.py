from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

a = int(input("masukkan batasan: "))

def cetak(i):
    for i in range(a):
        if i % 2 == 0:
           print(f"bilangan ganjil-{i+1}", "- ID Proses ", getpid())
        else : 
           print(f"bilangan genap-{i+1}", "- ID Proses ", getpid())
    sleep(1)

#Sekuensial
print("Sekuensial")
sekuensial_awal = time()

for i in range(1):
    cetak(i)
sekuensial_akhir = time()
print(" ")

#Multiprocessing Process
print("Multiprocessing.Process")
kumpulan_proses = []
proses_awal = time()

for i in range(1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
proses_akhir=time()
print(" ")

#Multiprocessing Pool
print("Multiprocessing.pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
pool_akhir=time()
print(" ")

#Perbandingan Waktu Eksekusi
print("Perbandingan Waktu eksekusi")
print("Sekuensial              : ",sekuensial_akhir - sekuensial_awal, "detik")
print("Multiprocessing.Process : ",proses_akhir - proses_awal, "detik")
print("Multiprocessing.Pool    : ",pool_akhir - pool_awal, "detik")

