#!/bin/bash

# Mendeklarasikan Fungsi
p() {
 echo -n "Masukkan Panjang : "
 read p
}
l() {
 echo -n  "Masukkan Lebar : "
 read l
}
luas() {
    let luas=$p*$l
    echo "Luas Persegi Panjang : $luas "
}

# Memanggil Fungsi 
p
l
luas 
