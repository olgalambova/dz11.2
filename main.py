def pow(x):
    return x ** 3
print([pow(2)])
def generate_cube_numbers(begin, end, func):
    for i in range(end):
        yield pow(begin)
        begin += 1
        if begin >= end:
            return func(begin)

from inspect import isgenerator
gen = generate_cube_numbers(2, 10, pow)
print([next(gen), next(gen), next(gen)])


#assert isgenerator(gen) == True, 'Test0'
#assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
#assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
#assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
