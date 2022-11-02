#!/bin/bash

# Mendeklarasikan Fungsi
nama() {
    echo "Siapa namamu?"
    read nama
}
npm() {
    echo "Sebutkan npm mu"
    read npm
    echo -e "hai $nama dengan mpm $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

# Memanggil Fungsi 
nama
npm
