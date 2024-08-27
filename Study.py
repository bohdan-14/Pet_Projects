



# target_value = 0
# print("Значение для перемещения:", target_value)
# result = []
# zero_count = 0
# for x in lst:
#     if x == target_value:
#         zero_count += 1
#     else:
#         result.append(x)
# result.extend([target_value] * zero_count)
# print("Результат:", result)
# import random
lst = [1,3,5]
if not lst:
    result = 0
else:
    sum_even_indices = 0
    for i in range(0, len(lst), 2):
        sum_even_indices += lst[i]
    result = sum_even_indices * lst[-1]
print(result)





