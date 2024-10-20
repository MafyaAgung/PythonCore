#
# Complete the 'diff_letters' function below.
#
# The function is expected to return a INTEGER.
# The function accepts LIST INTEGER list as parameter.
#

def maksimum_keuntungan_barang(object_input):
    # Write your code here
    # extract input
    kapasitas = object_input[0]
    list_bobot = [item[0] for item in object_input[1]]
    list_value = [item[1] for item in object_input[1]]

    n_item = len(list_value)

    # insialisasi index untuk kombinasi
    list_index = list(range(n_item))
    list_index_kombinasi = []

    # buat kombinasi dari list index
    # contoh: index=[1, 2, 3]. maka hasilnya adalah [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    def backtrack(start, path):
        list_index_kombinasi.append(path)
        for i in range(start, n_item):
            backtrack(i + 1, path + [list_index[i]])

    backtrack(0, [])

    # filter list_index_kombinasi berdasarkan bobotnya
    list_index_kombinasi_filtered = []
    for index_kombinasi in list_index_kombinasi:
        # ekstrak bobot dari setiap item index_Kombinasi, lalu hitung totalnya
        list_bobot_kombinasi = [list_bobot[index] for index in index_kombinasi]
        sum_bobot_kombinasi = sum(list_bobot_kombinasi)

        # jika total bobot <= kapasitas, masukan ke dalam list_index_filtered
        if sum_bobot_kombinasi <= kapasitas:
            list_index_kombinasi_filtered.append(index_kombinasi)

    # hitung hasil dengan mengkalkulasikan kombinasi item apa saja yang memiliki nilai paling besar
    hasil = 0
    for index_kombinasi in list_index_kombinasi_filtered:
        # ekstrak value dari setiap item index_Kombinasi_filtered, lalu hitung totalnya
        list_value_kombinasi = [list_value[index] for index in index_kombinasi]
        sum_value_kombinasi = sum(list_value_kombinasi)

        # jika total value > hasil, jadikan total value sebagai hasil
        if sum_value_kombinasi > hasil:
            hasil = sum_value_kombinasi

    return hasil

