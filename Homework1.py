# Homework 1

def get_data(string):
    """Take char string of numbers and convert to integer list of lists."""
    lst = list(string.split(" "))
    ints = []
    for i in lst:
        ints.append(int(i))
    return ints


str1 = "2 1 0 9 3"
print(get_data(str1))
