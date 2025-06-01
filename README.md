[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Greedy for Diamonds!

## Deskripsi Singkat 📌
Program ini merupakan bot otomatis untuk permainan pengumpulan diamond pada sebuah board. Bot menggunakan algoritma **greedy** yang selalu memilih langkah terbaik secara lokal berdasarkan **nilai diamond dan jarak** ke diamond tersebut.

Strategi greedy ini berprinsip pada pemilihan **diamond terdekat dengan nilai tertinggi** yang masih bisa diambil sesuai kapasitas penyimpanan (maksimal 5 item).

## Authors 🧟🧟
-  Muhammad Fauzan Naufal / 123140150
-  Muhammad Fatahillah Farid / 123140203
-  M. Reyshandi / 123140037

  

## Cara Menjalankan Bot 💀

1. To run one bot

    ```
    python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo
    ```

2. To run multiple bots simultaneously

    For Windows

    ```
    ./run-bots.bat
    ```

    For Linux / (possibly) macOS

    ```
    ./run-bots.sh
    ```

    <b>Before executing the script, make sure to change the permission of the shell script to enable executing the script (for linux/macOS)</b>

    ```
    chmod +x run-bots.sh
    ```


## Credits 🪙

This repository is adapted from https://github.com/Etimo/diamonds2

Some code in this repository is adjusted to fix some issues in the original repository and to adapt to the requirements of Algorithm Strategies course (IF2211), Informatics Undergraduate Program, ITB.

©️ All rights and credits reserved to [Etimo](https://github.com/Etimo)
