#!bin/bash

nilai1=60
nilai2=80

let jumlah=$nilai1+$nilai2
kurang='expr $x - $y'
kali=$(($nilai1*$nilai2))
bagi=$(($nilai1/$nilai2))
mod=$(($nilai1%$nilai2))

printf"Berapakah $nilai1+$nilai2?"
read jawab

if [ $jawab == $jumlah ]
then 
 echo "Benar"
else
 echo "Salah"
fi
