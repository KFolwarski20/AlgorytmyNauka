import time
from introductionToAlgorithms import binary_search
from sortingBySelection import selection_sort
from quicksort import sum_digits, sum_code, count_list_elements, find_max_digit, quicksort
from dictionary import voted, check_voter
from broadSearch import mango_seller_search
from DijkstryAlgorithm import dijkstry

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
    print(quicksort([10, 5, 2, 3]))

    book = dict()
    book["jabłko"] = 0.67
    book["mleko"] = 1.49
    book["awokado"] = 1.49
    print(book)
    print(book["awokado"])

    print(check_voter("tomasz"))
    print(check_voter("michał"))
    print(check_voter("michał"))

    mango_seller_search("ty")

    dijkstry()
