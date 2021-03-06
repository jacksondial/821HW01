# Homework 1
import math as ma


def get_data(string: str) -> list[list[int]]:
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


def analyze_data(data: list[list[int]], statistic: str) -> float:
    """Take list of lists and outputs statistic about data."""
    # Put all numbers into one list for average and sd
    all_data = [number for lst in data for number in lst]
    average = sum(all_data) / len(all_data)

    # Need individual list averages and covariance for cov and corr
    avg0 = sum(data[0]) / len(data[0])
    avg1 = sum(data[1]) / len(data[1])
    covariance = sum(
        (data[0][i] - avg0) * (data[1][i] - avg1) for i in range(len(data[0]))
    ) / len(data[0])

    if statistic == "average":
        return round(average, 1)
    elif statistic == "standard deviation":
        sd = ma.sqrt(sum([(i - average) ** 2 for i in all_data]) / len(all_data))
        return round(sd, 1)
    elif statistic == "covariance":
        return round(covariance, 1)
    elif statistic == "correlation":
        sd0 = ma.sqrt(sum([(i - avg0) ** 2 for i in data[0]]) / len(data[0]))
        sd1 = ma.sqrt(sum([(i - avg1) ** 2 for i in data[1]]) / len(data[1]))
        return round(covariance / (sd0 * sd1), 3)
    else:
        raise ValueError(f"Unrecognized statistic {statistic}")


# if __name__ == "main":
# Lets the user input a file path to run functions on data
filename = input("Enter file path here: ")
with open(filename) as file:
    txt = file.read()

data1 = get_data(txt)
print(analyze_data(data1, "average"))
print(analyze_data(data1, "standard deviation"))
print(analyze_data(data1, "covariance"))
print(analyze_data(data1, "correlation"))
print(analyze_data(data1, "blah"))
