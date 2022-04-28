def check_prime(number):
    num_iterations = 0
    for i in range(2, number):
        num_iterations += 1

        if number % i == 0:
            print(f'{number} is not a prime number '
                  f'\nTotal number of iterations = {num_iterations}')

    print(f'{number} is a prime number '
          f'\nTotal number of iterations = {num_iterations}')


check_prime(88)
