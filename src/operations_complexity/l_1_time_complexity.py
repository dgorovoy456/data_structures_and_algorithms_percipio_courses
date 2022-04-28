def addition(num1, num2):
    total = num1 + num2

    print(f'The sum of {num1} and {num2} is {total}')


addition(5, 5)


def addition(num1, num2):
    num_iterations = 0

    total = num1 + num2
    num_iterations += 1

    print(f'The sum of {num1} and {num2} is {total}\n number of iterations = {num_iterations}')


addition(5, 6)

addition(10000, 200)

print('\n#####################################################\n')


def check_oddeven(number):
    count = 0
    num_iterations = 0

    if number % 2 == 0:
        num_iterations += 1
        print(f'{number} is an even number')
    else:
        num_iterations += 1
        print(f'{number} is an odd number')

    print(f'Total number of iteration = {num_iterations}')


check_oddeven(76)

print('\n#####################################################\n')


def find_square(number):
    num_iterations = 0
    square = number ** 2

    num_iterations += 1

    print(f'Square of {number} is {square}'
          f'\nTotal number of iterations = {num_iterations}')


find_square(1000)
