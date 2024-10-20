# Sebuah data nilai ujian matematika memiliki distribusi normal dengan mean 75 dan standar deviasi 10. 
# Hitunglah probabilitas mendapatkan nilai ujian matematika lebih dari 85 menggunakan Python!

# Output:

# Probabilitas nilai ujian matematika lebih dari 85: 0.34134474602599823

import scipy.stats as stats

# Mean dan standar deviasi
mean = 75
stddev = 10

# Nilai batas atas
nilai_atas = 85

# Hitung probabilitas
probabilitas = stats.norm.cdf(nilai_atas, mean, stddev)
print("Probabilitas nilai ujian matematika lebih dari 85:", probabilitas)
