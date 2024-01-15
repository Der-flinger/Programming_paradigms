# Предположим, что нам хочется для любого массива чисел
# array и любого числа target узнать содержится ли target в array.
# Такую процедуру будем называть поиском.


def search_element(arr, target):
    for el in arr:
        if el == target:
            return True
    return False


print(search_element([1, 2, 3, 4, 5], 3))
