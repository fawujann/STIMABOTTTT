[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Greedy for Diamonds!

## Deskripsi Singkat 📌
Program ini merupakan bot otomatis untuk permainan pengumpulan diamond pada sebuah board. Bot menggunakan algoritma **greedy** yang selalu memilih langkah terbaik secara lokal berdasarkan **nilai diamond dan jarak** ke diamond tersebut.

Strategi greedy ini berprinsip pada pemilihan **diamond terdekat dengan nilai tertinggi** yang masih bisa diambil sesuai kapasitas penyimpanan (maksimal 5 item).

## Authors 🧟🧟
-  Muhammad Fauzan Naufal / 123140150
-  Muhammad Fatahillah Farid / 123140203
-  M. Reyshandi / 123140037

## Requirement dan Instalasi ⚙️
- Python 3.10 atau lebih baru
- Visual Studio Code
- Docker Dekstop
- OS: Windows / Linux / Mac  

## Cara Menjalankan Bot 💀

1. satu bot saja

    ```
    python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo
    ```

2. menjalankan beberapa bot bersamaan

   Windows

    ```
    ./run-bots.bat
    ```

   Linux / macOS

    ```
    ./run-bots.sh
    ```

    <b>Sebelum menjalankan skrip, pastikan untuk mengubah izin file shell script agar dapat dieksekusi~</b>

    ```
    chmod +x run-bots.sh
    ```
