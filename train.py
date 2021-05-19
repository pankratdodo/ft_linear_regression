import csv
import os.path
from predict import data_file_parser
from predict import error

epochs = 1000
l_rate = 0.1
data_file = 'data.csv'
param_file = 'parameters.txt'


def gradient(x, y):
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
    if not os.path.isfile(param_file):
        error("File with params {} does not exist.".format(param_file))
    try:
        param_file_fd = open(param_file, 'w')
        file = csv.writer(param_file_fd)
        file.writerow([a])
        file.writerow([b])
    except IOError:
        error("Cant open {} file.".format(param_file))


def main():
    x, y = data_file_parser()
    x = normalize_value(x)
    y = normalize_value(y)
    a, b = gradient(x, y)
    write_to_param_file(a, b)


if __name__ == '__main__':
    main()
