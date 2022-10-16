#!/bin/bash

echo "banyak nilai yang akan di masukkan:"
read IPK

jumlah=0;
IPK_Mahasiswa=0;

for ((i=1; i < IPK; i++))
do
        echo "nilai ke $i: "
        read tulis[$i]
        let jumlah=$jumlah+${tulis[i]};
        let IPK_Mahasiswa=$jumlah/$IPK;
done

echo "IPS Mahasiswa: " $jumlah/$IPK
echo "IPK Mahasiswa: " $IPK_Mahasiswa
