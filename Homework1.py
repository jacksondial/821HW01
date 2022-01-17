# Homework 1
import math as ma


def get_data(string):
    """Take char string of numbers and convert to integer list of lists."""
    lst = list(string.split(" "))
    ints = []
    for i in lst:
        ints.append(int(i))
    return ints


str1 = "2 1 3"
data1 = get_data(str1)


def analyze_data(data, statistic):
    """Take list of lists and outputs statistic about data."""
    average = sum(data) // len(data)
    if statistic == "average":
        output = average
    if statistic == "standard deviation":
        sd = sum([(i - average) ** 2 for i in data]) // len(data)
        output = sd
    return output


print(analyze_data(data1, "standard deviation"))
