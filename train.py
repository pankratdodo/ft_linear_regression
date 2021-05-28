import csv
import sys
from predict import data_file_parser
from predict import error
import matplotlib.pyplot as plt

data_file = 'data.csv'
param_file = 'parameters.txt'


def gradient(x, y, epochs, l_rate):
    length = float(len(x))
    a = 0.0
    b = 0.0
    for epoch in range(0, epochs):
        a_gradient = 0.0
        b_gradient = 0.0
        for i in range(0, int(length)):
            a_gradient += a + (b * x[i]) - y[i]
            b_gradient += (a + (b * x[i]) - y[i]) * x[i]
        a -= l_rate * (1 / length) * a_gradient
        b -= l_rate * (1 / length) * b_gradient
    return a, b


def normalize_value(value):
    min_v = min(value)
    max_v = max(value)
    res = []
    for one in value:
        try:
            res.append((one - min_v) / (max_v - min_v))
        except ZeroDivisionError:
            error("File with data {} is incorrect cause max and min values are equals.".format(data_file))
    return res


def write_to_param_file(a, b):
    # if not os.path.isfile(param_file):
    #     error("File with params {} does not exist.".format(param_file))
    try:
        param_file_fd = open(param_file, 'w')
        file = csv.writer(param_file_fd)
        file.writerow([a])
        file.writerow([b])
    except IOError:
        error("Cant open {} file.".format(param_file))


def display_data(x, y, a, b):
    plt.figure(figsize=(5, 5))
    plt.plot(x, y, "b.")
    plt.grid(True)
    plt.xlabel("Millage")
    plt.ylabel("Price")
    plt.title("ft_linear_regression")
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    line_x = [min_x, max_x]
    line_y = []
    for point in line_x:
        normalized_x = (point - min_x) / (max_x - min_x)
        point = b * normalized_x + a
        denormalized_y = point * (max_y - min_y) + min_y
        line_y.append(denormalized_y)
    plt.plot(line_x, line_y, 'y')
    plt.show()


def check_epochs():
    if len(sys.argv) == 3 and sys.argv[1] == "-epoch" and sys.argv[2]:
        try:
            epochs = int(sys.argv[2])
        except ValueError:
            error("Value of epochs have to be int number.")
        if epochs < 10 or epochs > 1000000:
            error("Value of epochs have to be more than 10 and less than 1000000")
    else:
        epochs = 1000
    return epochs


def check_l_rate():
    if len(sys.argv) == 3 and sys.argv[1] == "-lr" and sys.argv[2]:
        try:
            l_rate = float(sys.argv[2])
        except ValueError:
            error("Value of learning rate have to be float number.")
        if l_rate > 1 or l_rate < 0:
            error("Value of learning rate have to be more tah 0 and less than 1")
    else:
        l_rate = 0.1
    return l_rate


def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        error("Invalid parameters. \nUsage: python3 train.py [-lr/epoch] [value ...]")
    epochs = check_epochs()
    l_rate = check_l_rate()
    x, y = data_file_parser()
    x_norm = normalize_value(x)
    y_norm = normalize_value(y)
    a, b = gradient(x_norm, y_norm, epochs, l_rate)
    display_data(x, y, a, b)
    write_to_param_file(a, b)


if __name__ == '__main__':
    main()
