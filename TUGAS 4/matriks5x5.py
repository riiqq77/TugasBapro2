nested_list_1 = [
    [7, 2, 5, 4, 5],
    [6, 4, 2, 5, 9],
    [3, 1, 4, 3, 8],
    [4, 3, 2, 1, 5],
    [5, 4, 3, 2, 1]
]
nested_list_2 = [
    [9, 5, 2, 4, 3],
    [2, 1, 3, 4, 5],
    [3, 2, 1, 4, 5],
    [7, 6, 3, 1, 5],
    [6, 4, 1, 9, 1]
]
# Hasil perkalian matriks akan disimpan di nested_list_3
nested_list_3 = []
for i in range(5):
    row = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += nested_list_1[i][k] * nested_list_2[k][j]
        row.append(total)
    nested_list_3.append(row)

print(nested_list_3)