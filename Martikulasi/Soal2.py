# Dua variabel X dan Y memiliki data sebagai berikut:

# X = [1, 2, 3, 4, 5]
# Y = [2, 4, 5, 3, 6]
# Hitunglah kovariansi antara variabel X dan Y menggunakan Python!

# Output:

# Kovariansi antara X dan Y: 1.0


import numpy as np

# Hitung kovariansi
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 3, 6]

cov_xy = np.cov(X, Y)[0, 1]
print("Kovariansi antara X dan Y:", cov_xy)

