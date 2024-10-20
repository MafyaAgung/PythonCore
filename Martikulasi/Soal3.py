# Sebuah perusahaan memproduksi dua jenis produk A dan B. Probabilitas produk A cacat adalah 0.2 dan probabilitas produk B cacat adalah 0.3.
# Jika produk A cacat, probabilitas produk B cacat adalah 0.4. Jika produk A tidak cacat, probabilitas produk B cacat adalah 0.2.
# Hitunglah nilai harapan (expected value) dari jumlah produk cacat menggunakan Python!

# Output:
# Nilai harapan jumlah produk cacat: 0.44


import numpy as np

# Probabilitas produk A cacat
p_a_cacat = 0.2

# Probabilitas produk B cacat
p_b_cacat = 0.3

# Probabilitas produk B cacat jika A cacat
p_b_cacat_given_a_cacat = 0.4

# Probabilitas produk B cacat jika A tidak cacat
p_b_cacat_given_a_tidak_cacat = 0.2

# Hitung probabilitas kedua produk tidak cacat
p_tidak_cacat = (1 - p_a_cacat) * (1 - p_b_cacat)

# Hitung probabilitas salah satu produk cacat
p_satu_cacat = p_a_cacat * p_b_cacat_given_a_cacat + (1 - p_a_cacat) * p_b_cacat_given_a_tidak_cacat

# Hitung probabilitas kedua produk cacat
p_dua_cacat = p_a_cacat * p_b_cacat_given_a_cacat

# Hitung nilai harapan jumlah produk cacat
nilai_harapan = 0 * p_tidak_cacat + 1 * p_satu_cacat + 2 * p_dua_cacat
print("Nilai harapan jumlah produk cacat:", nilai_harapan)
