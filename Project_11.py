# 11.1
def prime_generator(end):
    for i in range(2, end):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

# 11.2
def generate_cube_numbers(end):
    for i in range(2, end):
        if i ** 3 < end:
            yield i ** 3
        else:
            return

# 11.3
def is_even(number):
    return (number & 1) == 0

