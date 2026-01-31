my_set = {1, 2, 3}
my_set = set([4, 5, 6])

my_set = set()

my_set1 = {1, 2, 2, 2, 3, 3, 3}
print(my_set1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print("Union of set1 and set2 method:", union_result_method)
print("Union of set1 and set2 operator:", union_result_operator)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print("Intersection of set1 and set2 method:", intersection_result_method)
print("Intersection of set1 and set2 operator:", intersection_result_operator)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print("Difference of set1 and set2 method:", difference_result_method)
print("Difference of set1 and set2 operator:", difference_result_operator)

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print("Symmetric Difference of set1 and set2 method:", symmetric_difference_method)
print("Symmetric Difference of set1 and set2 operator:", symmetric_difference_operator) 

#SET METHODS

my_set2 = {1, 2, 3}

my_set2.add(5)

my_set2.remove(2)

my_set2.discard(8)

print(my_set2)

my_set2.clear()

set_length = len(my_set2)
print(set_length)

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = set(my_list)

unique_list = list(unique_list)
print(unique_list)