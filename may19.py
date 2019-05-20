"""
The question is the following:
return a new sorted merged list from K sorted lists, each with size N
For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32]
"""
import heapq

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


def merg_sorted_list2(list_sorted_lists):
    merged_list = []
    heap = [(lis[0], count, 0) for count, lis in enumerate(list_sorted_lists) if lis]
    heapq.heapify(heap)

    while heap:
        val, list_index, ele_index = heapq.heappop(heap)
        merged_list.append(val)

        if ele_index + 1 < len(list_sorted_lists[list_index]):
            heapq.heappush(heap, (list_sorted_lists[list_index][ele_index + 1],
                                  list_index,
                                  ele_index + 1
                                  ))
    return merged_list


test_data = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
expected_result = [10, 12, 15, 15, 17, 20, 20, 30, 32]
# result = merge_sorted_list(test_data)
result = merg_sorted_list2(test_data)
print(result)
assert result == expected_result
