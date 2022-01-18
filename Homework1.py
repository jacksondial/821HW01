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

    return final_list


str1 = """1 44 31 4 5 6
21 3 2 13 55 72"""
data1 = get_data(str1)


def analyze_data(data, statistic):
    """Take list of lists and outputs statistic about data."""
    all_data = [number for lst in data for number in lst]
    average = sum(all_data) / len(all_data)
    if statistic == "average":
        return round(average, 1)
    if statistic == "standard deviation":
        sd = ma.sqrt(sum([(i - average) ** 2 for i in all_data]) / len(all_data))
        return round(sd, 1)
    avg0 = sum(data[0]) / len(data[0])
    avg1 = sum(data[1]) / len(data[1])
    covariance = sum(
        (data[0][i] - avg0) * (data[1][i] - avg1) for i in range(len(data[0]))
    ) / len(data[0])
    if statistic == "covariance":
        return round(covariance, 1)
    if statistic == "correlation":
        sd0 = ma.sqrt(sum([(i - avg0) ** 2 for i in data[0]]) / len(data[0]))
        sd1 = ma.sqrt(sum([(i - avg1) ** 2 for i in data[1]]) / len(data[1]))
        return round(covariance / (sd0 * sd1), 3)


print(analyze_data(data1, "average"))
print(analyze_data(data1, "standard deviation"))
print(analyze_data(data1, "covariance"))
print(analyze_data(data1, "correlation"))
