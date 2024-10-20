# Seorang mahasiswa ingin menghitung nilai Z untuk nilai ujian matematika 80. 
# Data nilai ujian matematika memiliki mean 75 dan standar deviasi 10. 
# Hitunglah nilai Z menggunakan Python!

# Output:

# Nilai Z untuk nilai ujian matematika 80: 0.5

import scipy.stats as stats

# Nilai ujian matematika
nilai_ujian = 80

# Mean dan standar deviasi
mean = 75
stddev = 10

# Hitung nilai Z
nilai_z = stats.zscore(nilai_ujian, mean, stddev)
print("Nilai Z untuk nilai ujian matematika 80:", nilai_z)
