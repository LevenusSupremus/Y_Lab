n = 5
matrix = []
H = 0
PathLenght = 0
row = []
col = []
res = []
result = []
StartMatrix = []
# В листах ниже храним индексы
for i in range(n):
    row.append(i)
    col.append(i)
    
# кастомный Min для поиска с игнорированием по индексу
def Min(lst, myindex):
    return min(x for idx, x in enumerate(lst) if idx != myindex)

# Для удаления из матрицы элементов
def Delete(matrix, index1, index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix

# Расчёт пути между точками
def cp(fp, sp):
    return ((sp[0] - fp[0]) ** 2
            + (sp[1] - fp[1]) ** 2) ** 0.5

# Вводим матрицу
points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
for point_ind in range(len(points)):
    matrix.append([])
    for a_point in points:
        matrix[point_ind].append(cp(points[point_ind], a_point))
# Копируем начальное состояние матрицы на будущее
for i in range(n):
    StartMatrix.append(matrix[i].copy())
# Присваеваем главной диагонали float(inf)
for i in range(n):
    matrix[i][i] = float('inf')
while True:
    # Вычитаем минимальный элемент в строках
    for i in range(len(matrix)):
        min_row = min(matrix[i])
        min_column = min(row[i] for row in matrix)
        H += min_row + min_column
        for j in range(len(matrix)):
            matrix[i][j] -= min_row
            matrix[j][i] -= min_column
    # Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
    NullMax = 0
    index1 = 0
    index2 = 0
    tmp = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                tmp = Min(matrix[i], j)+Min((row[j] for row in matrix), i)
                if tmp >= NullMax:
                    NullMax = tmp
                    index1 = i
                    index2 = j

    # Находим нужный нам путь, записываем его в res и удаляем все ненужное
    res.append(row[index1]+1)
    res.append(col[index2]+1)
    oldIndex1 = row[index1]
    oldIndex2 = col[index2]
    if oldIndex2 in row and oldIndex1 in col:
        NewIndex1 = row.index(oldIndex2)
        NewIndex2 = col.index(oldIndex1)
        matrix[NewIndex1][NewIndex2] = float('inf')
    del row[index1]
    del col[index2]
    matrix = Delete(matrix, index1, index2)
    if len(matrix) == 1:
        break
# Выстраиваем путь
for i in range(0, len(res)-1, 2):
    if res.count(res[i]) < 2:
        result.append(res[i])
        result.append(res[i+1])
for i in range(0, len(res)-1, 2):
    for j in range(0, len(res)-1, 2):
        if result[len(result)-1] == res[j]:
            result.append(res[j])
            result.append(res[j+1])
path = []
# Расчитываем путь
for i in range(0, len(result)-1, 2):
    if i == len(result)-2:
        PathLenght += StartMatrix[result[i]-1][result[i+1]-1]
        path.append(PathLenght)
        PathLenght += StartMatrix[result[i+1]-1][result[0]-1]
    else:
        PathLenght += StartMatrix[result[i]-1][result[i+1]-1]
    path.append(PathLenght)

path.append(path[-1])
S = []
[S.append(s) for s in result if s not in S]

print(points[0], end=' -> ')
for i in range(5):
    print(f'{points[S[i]-1]}[{path[i]}]', end=f'{" -> " if i!=4 else ""}')
print(f" = {path[-1]}")
