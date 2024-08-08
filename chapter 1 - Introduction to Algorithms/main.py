from simple_search import simple_search
from binary_search import binary_search

# You need to know how the running time(t or growth) increases as the list size increases(n).
# Big O notation lets you compare the number of operations(n). It tells you how fast the algorithm grows.
# Big O notation is about the worst-case scenario.
# O(log n) is faster than O(n), but it gets a lot faster as the list of items you’re searching grows.


def simple_search_example():
    countries = ["Argentina", "Germany", "Canada", "Spain", "Brazil", "South Korea", "Japan", "China", "Nigeria", "Mexico", "Iran", "Ecuador", "India"]
    item_1 = "China"
    item_2 = "Australia"
    
    item_1_index = simple_search(countries, item_1)    
    item_2_index = simple_search(countries, item_2)
    
    print(item_1_index, item_2_index)


def binary_search_example():
    sorted_countries = ["Argentina", "Brazil", "Canada", "China", "Ecuador", "Germany", "India", "Iran", "Japan", "Nigeria", "Mexico", "Spain", "South Korea"]
    item_1 = "China"
    item_2 = "Australia"
    
    item_1_index = binary_search(sorted_countries, item_1)
    item_2_index = binary_search(sorted_countries, item_2)
    
    print(item_1_index, item_2_index)    


def main():
    
    # simple_search_example()
    # binary_search_example()
    
    return 0


main()
