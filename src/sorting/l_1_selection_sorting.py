def print_list(num_list):
    print(num_list)


def selection_sorting(original_list):
    length = len(original_list)

    for i in range(length):

        min_value_index = i

        for j in range(i + 1, length):

            if original_list[min_value_index] > original_list[j]:
                min_value_index = j

        original_list[i], original_list[min_value_index] = \
            original_list[min_value_index], original_list[i]
        print(f'Sorted till index {i}')
        print_list(original_list)

        print('Sorted list: ')
        print_list(original_list)


list_val = [22, 43, 55, 67, 23, 2, 77, 445]
list_val1 = ['Denys', 'Anna', 'Matvii', 'Mia']

selection_sorting(list_val)
selection_sorting(list_val1)
