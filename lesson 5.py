

5.1
text = input("Enter any text:")
is_valid = True

if text[0].isdigit():
    print("Значення змінної недопустиме")
    is_valid = False

for symbol in text:
    if symbol.isupper():
        print("Значення змінної недопустиме")
        is_valid = False
        break

if " " in text:
    print("Значення змінної недопустиме")
    is_valid = False

for symbol in text[:]:
    if not (symbol.isalpha() or symbol.isdigit() or symbol == '_'):
        print("Значення змінної недопустиме")
        is_valid = False
        break

if is_valid:
    print("Значення змінної допустиме по всім перевіркам")

5.2
while True:
    n1 = int(input("Enter number: "))
    n2 = int(input("Enter number: "))

    action = input("Choice next action: +, -, *, /: ")

    if action == "+":
        result = n1 + n2
    elif action == "-":
        result = n1 - n2
    elif action == "*":
        result = n1 * n2
    elif action == "/":
        if n2 != 0:
            result = n1 / n2
        else:
            print("Cannot divide by zero")
            continue
    else:
        print("Invalid operation")
        continue
    print("Result:", result)

    continue_input = input("Do you want to continue? (y/yes to continue): ")
    if continue_input.lower() not in ["y", "yes"]:
        break

5.3
import string

user = input("Enter text:")
try_text = []

for symbol in user:
    if symbol != " " and symbol not in string.punctuation:
        try_text.append(symbol)

result = ''.join(try_text)
capitalized_words = [word.capitalize() for word in result.split()]
final_result = ''.join(capitalized_words)

if len(final_result) > 140:
    final_result = final_result[:140]
hashtag = '#' + final_result

print(hashtag)






