# Homework 1
import math as ma


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


str1 = """1 44 31 4 5 6
21 3 2 13 55 72"""
data1 = get_data(str1)


def analyze_data(data, statistic):
    """Take list of lists and outputs statistic about data."""
    all_data = [number for lst in data for number in lst]
    average = sum(all_data) / len(all_data)
    if statistic == "average":
        output = round(average, 1)
    if statistic == "standard deviation":
        sd = ma.sqrt(sum([(i - average) ** 2 for i in all_data]) / len(all_data))
        output = round(sd, 1)
    return output


print(analyze_data(data1, "average"))
print(analyze_data(data1, "standard deviation"))
# str1 = """2 1 0 9 3 2
# 4 7 6 1 2 5"""
# print(get_data(str1))
