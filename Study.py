


import random
lst = [random.randint(0,2) for _ in range(5)]
print("Исходный списк:", lst)
target_value = 0
print("Значение для перемещения:", target_value)
result = []
zero_count = 0
for x in lst:
    if x == target_value:
        zero_count += 1
    else:
        result.append(x)
result.extend([target_value] * zero_count)
print("Результат:", result)


