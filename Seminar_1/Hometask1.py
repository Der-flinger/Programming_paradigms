# Для разогрева на первое домашнее задание будет каноническая задача сортировки списка
# Задача №1 Дан список целых чисел numbers. Необходимо написать в
# императивном стиле процедуру для сортировки чисел в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.
# Задача №2 Написать точно такую же процедуру, но в декларативном стиле

# Императивный стиль решения
def array_sorting_imp(array):
    circle = True
    while circle == True:
        circle = False
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                circle = True
    print(array)

# Декларативный стиль решения
def array_sorting_dec(array):
    list.sort(array)
    print(array)

array1 = [12, 4, 43, 2, 56767, 343, 4, 5, -34, 1]
array2 = [5,34,0,-2,-32,78,55,5,3,1,0,-23,2111,-22222]
array_sorting_imp(array1)
array_sorting_dec(array2)
