import scipy.stats as stats

# Data berat badan sebelum
berat_badan_sebelum = [75, 82, 68, 90, 85]

# Data berat badan sesudah
berat_badan_sesudah = [70, 78, 65, 85, 80]

# Hitung selisih berat badan
selisih_berat_badan = [berat_badan_sebelum[i] - berat_badan_sesudah[i] for i in range(len(berat_badan_sebelum))]

# Lakukan t-test berpasangan
t_statistic, p_value = stats.ttest_ind(selisih_berat_badan, [0] * len(selisih_berat_badan))

# Menampilkan hasil
print("Nilai t-statistic:", t_statistic)
print("Nilai p-value:", p_value)
