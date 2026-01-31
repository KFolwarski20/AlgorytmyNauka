import time
from introductionToAlgorithms import binary_search
from sortingBySelection import selection_sort
from quicksort import sum_digits, sum_code, count_list_elements, find_max_digit

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    start_time_1 = time.time()
    print(f"Item: {binary_search(my_list, 3)}|\t{time.time() - start_time_1:.8f} seconds")
    start_time_2 = time.time()
    print(f"Item: {binary_search(my_list, -1)}|\t{time.time() - start_time_2:.8f} seconds")
    print(f"Selection sort: {selection_sort([5, 3, 6, 2, 10])}")
    print(sum_digits([1, 2, 3, 4]))
    print(sum_code([1, 2, 3, 4]))
    print(count_list_elements([1, 2, 3, 4, 5, 10, 11]))
    print(find_max_digit([1, 2, 3, 14, 5, 10, 11]))
