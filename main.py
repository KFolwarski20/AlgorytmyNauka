import time
from introductionToAlgorithms import binary_search
from sortingBySelection import selection_sort

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    start_time_1 = time.time()
    print(f"Item: {binary_search(my_list, 3)}|\t{time.time() - start_time_1:.8f} seconds")
    start_time_2 = time.time()
    print(f"Item: {binary_search(my_list, -1)}|\t{time.time() - start_time_2:.8f} seconds")
    print(f"Selection sort: {selection_sort([5, 3, 6, 2, 10])}")
