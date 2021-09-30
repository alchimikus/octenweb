# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
avr = sum(arr)/len(arr)
round_el = arr[0]
distance = ((arr[0]-avr)**2)**0.5
for el in arr:
    if distance > ((el-avr)**2)**0.5:
        distance = ((el-avr)**2)**0.5
        round_el = el
print(round_el)

