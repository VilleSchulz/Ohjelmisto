def combine_lists(list1, list2):
    combined_list = []

    for i in list1:
        combined_list.append(i)

    for i in list2:
        combined_list.append(i)

    combined_list.sort()

    return combined_list

