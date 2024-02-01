def linear_search(value_to_find, array_to_search_through):
    answer = 0
    for x in array_to_search_through:
        if x == value_to_find:
            return answer
        answer = answer + 1

def linear_search_global(value_to_find, array_to_search_through):
    answer_list = []
    answer = 0
    for x in array_to_search_through:
        if value_to_find == x:
            answer_list.append(answer) 
        answer = answer + 1
    return answer_list
   


print(linear_search(3, [1,2,3]))
print(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))