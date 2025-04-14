# 7.1
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

# 7.2
def correct_sentence(text):

    text = text[0].upper() + text[1:]


    if not text.endswith('.'):
        text += '.'

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')

# 7.3
def second_index(text, some_str):
    first_occurrence = text.find(some_str)

    if first_occurrence == -1:
        return None

    second_occurrence = text.find(some_str, first_occurrence + len(some_str))

    return second_occurrence if second_occurrence != -1 else None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')


# 7.4
def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    return multiples_of_3 & multiples_of_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')


