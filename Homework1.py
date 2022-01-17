# Homework 1


def get_data(string):
    """Take char string of numbers and convert to integer list of lists."""
    new_list = list(string.split("\n"))
    final_list = []
    for i in new_list:
        lst = list(i.split(" "))
        ints = []
        for j in lst:
            ints.append(int(j))
        final_list.append(ints)

    # lst = list(string.split(" "))
    # ints = []
    # for i in lst:
    #     ints.append(int(i))
    return final_list


str1 = """2 1 0 9 3 2
4 7 6 1 2 5"""
print(get_data(str1))
