# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы

def get_matrix(n, m, value):     # функция с параметрами
    matrix = []                  # пустой список внутри функции
    for i in range(n):           # внешний цикл  для кол-ва строк матрицы, n повторов.
        list_ = []               # пустой список внутри цикла
        for j in range(m):       # внутренний цикл для кол-ва столбцов матрицы, m повторов.
            list_.append(value)  # пополняeт ранее добавленный пустой список значениями value.
        matrix.append(list_)     # пополняет список списком
    return matrix                # возвращает значения параметров

print(get_matrix(2, 3, 6) + get_matrix(1, 4, 6))
print(get_matrix(3, 4, 8))
print(get_matrix(4, 5, 12))

