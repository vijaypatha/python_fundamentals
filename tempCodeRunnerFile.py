def odd_repeats(lst):
    for i in lst:
        lst.count(i % 2 !=0) # any_list.count -> counts returns the number of occurrences 
        print(i)
lst = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
odd_repeats(lst)