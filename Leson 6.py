#  6.1
# import string
#
# letters = input ("Enter Letters:")
# item = ("-")
# two_letters = letters.split(item)
# first_latter = string.ascii_letters.index(two_letters[0])
# second_latter = string.ascii_letters.index(two_letters[1])
# result= string.ascii_letters [first_latter:second_latter+1]
# print ("Result:", result)
#
# # 6.2
# seconds = int(input("Enter seconds:"))
#
# is_valid = True
#
# if seconds < 0 or seconds >= 8640000:
#    print("Значение не доступно. Повторите попытку до 8640000")
#    is_valid = False
#
# minute = seconds // 60
# seconds = seconds % 60
#
# hours = minute // 60
# minute = minute % 60
#
# day = hours // 24
# hours = hours % 24
#
# seconds_str = str(seconds).zfill(2)
# minute_str = str(minute).zfill(2)
# hours_str = str(hours).zfill(2)
# time_string = f"{hours_str}:{minute_str}:{seconds_str}"
#
# print(day, "днiв,", time_string)

# 6.3
# user_digit = input("Enter a number: ")
#
# while int(user_digit) > 9:
#     result = 1
#
#     for i in user_digit:
#         digit = int(i)
#         result *= digit
#
#     user_digit = str(result)
#
# print(user_digit)