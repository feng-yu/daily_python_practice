"""
The question is the following:
return a new sorted merged list from K sorted lists, each with size N
For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32]
"""


def merge_sorted_list(list_sorted_lists):
    merged_list = list_sorted_lists[0]
    for sorted_list in list_sorted_lists[1:]:
        for number in sorted_list:
            if number >= merged_list[-1]:
                merged_list.append(number)
            else:
                for index in range(0,len(merged_list)):
                    if number < merged_list[index]:
                        merged_list.insert(index, number)
                        break

    return merged_list


test_data = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
expected_result = [10, 12, 15, 15, 17, 20, 20, 30, 32]
result = merge_sorted_list(test_data)
print(result)
assert result == expected_result