def simple_search(search_list, item):
    low = 0
    high = len(search_list) - 1
    simple_sum = 0

    index_element = 0
    while index_element <= item:
    # while low <= high:
        index_element = search_list[low]
        if index_element == item:
            print("当前索引: [" + str(low) + "]")
            print("当前元素:", index_element)
            simple_sum += 1
            return simple_sum
        elif index_element < item:
            low += 1
            simple_sum += 1
        else:
            return None

def binary_search(search_list, item):
    low = 0
    high = len(num_list) - 1
    binary_sum = 0

    while low <= high:
        index = (low + high) // 2
        index_element = num_list[index]
        if index_element == item:
            print("当前索引: [" + str(index) + "]")
            print("当前元素:", index_element)
            binary_sum += 1
            return binary_sum
        elif index_element < item:
            low = index + 1
            binary_sum += 1
        elif index_element > item:
            high = index - 1
            binary_sum += 1
        else:
            return None

edge = 2**5

set_num = edge
num_list = []
i = 0
while i < set_num:
    i += 1
    num_list.append(i)
print("------简单查找------")
print("查找次数:", simple_search(num_list, i))
print("------二分查找------")
print("查找次数:", binary_search(num_list, i))
