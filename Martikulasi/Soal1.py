# Sebuah toko online menjual laptop dengan harga sebagai berikut:

# Rp 5.000.000, Rp 6.000.000, Rp 7.000.000, Rp 8.000.000, Rp 9.000.000
# Hitunglah mean, median, dan mode harga laptop tersebut menggunakan Python!

# Output:

# Mean harga laptop: 7000000.0
# Median harga laptop: 7000000.0
# Mode harga laptop: 0

import pandas as pd

# Buat dataframe dari data harga laptop
data = pd.DataFrame({
    "Harga": [5000000, 6000000, 7000000, 8000000, 9000000]
})

# Hitung mean
mean_harga = data["Harga"].mean()
print("Mean harga laptop:", mean_harga)

# Hitung median
median_harga = data["Harga"].median()
print("Median harga laptop:", median_harga)

# Hitung mode
mode_harga = data["Harga"].mode()
print("Mode harga laptop:", mode_harga)
