def print_list(num_list):
    print(num_list)


def bubble_sorting(original_list):
    length = len(original_list)

    for i in range(length - 1, 0, -1):
        for index in range(i):
            if original_list[index] > original_list[index + 1]:
                original_list[index + 1], original_list[index] = \
                    original_list[index], original_list[index + 1]

        print(f'Unsorted till index: {i - 1}')
        print_list(original_list)


list_val = [22, 43, 55, -3, 22, 67, 23, 2, 77, 445]
list_val1 = ['Denys', 'Anna', 'Matvii', 'Mia']

bubble_sorting(list_val)
bubble_sorting(list_val1)
