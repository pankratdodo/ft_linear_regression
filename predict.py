import os.path
import csv

data_file = 'data.csv'
param_file = 'parameters.txt'


def error(mess):
    print('\033[91m' + mess)
    exit(-1)


def param_file_parser():
    if not os.path.isfile(param_file):
        error("File with params {} does not exist.".format(param_file))
    param_file_fd = open(param_file, 'r')
    lines = param_file_fd.read().split('\n')
    lines = list(filter(None, lines))
    if len(lines) != 2:
        error("File {} is incorrect.".format(param_file))
    try:
        t0 = float(lines[0])
        t1 = float(lines[1])
    except ValueError:
        error("Params have to be float number.")
    if t0 == 0 or t1 == 0:
        print("It seems like you have not trained the model. Price is 0.")
        exit(0)
    return t0, t1


def data_file_parser():
    if not os.path.exists(data_file):
        error("File with data {} does not exist.".format(data_file))
    x = []
    y = []
    try:
        with open(data_file, 'r') as data_file_fd:
            data = csv.reader(data_file_fd, delimiter=',')
            next(data, None)
            for i in data:
                if len(i) != 2:
                    error("Row {} is incorrect.".format(i))
                if i[0].isnumeric() or i[1].isnumeric():
                    x.append(int(i[0]))
                    y.append(int(i[1]))
                else:
                    error("Row {} has incorrect values.".format(i))
    except IOError:
        error("Cant open {} file.".format(data_file))
    return x, y


def millage_parser():
    try:
        millage = float(input("Enter a mileage: "))
    except ValueError:
        error("Millage have to be float number.")
    if millage <= 0 or millage > 10000000:
        error("Millage have to be more than 0 and less than 10000000")
    return millage


def normalize_millage(x, millage):
    min_km = min(x)
    max_km = max(x)
    normalized_mileage = (millage - min_km) / (max_km - min_km)
    return normalized_mileage


def get_estimate_price(normalized_mileage, t0, t1, y):
    normalized_price = t0 + t1 * normalized_mileage
    min_price = min(y)
    max_price = max(y)
    estimate_price = normalized_price * (max_price - min_price) + min_price
    return estimate_price


def main():
    t0, t1 = param_file_parser()
    millage = millage_parser()
    x, y = data_file_parser()
    normalized_mileage = normalize_millage(x, millage)
    estimate_price = get_estimate_price(normalized_mileage, t0, t1, y)
    print('\033[92m' + "Car with millage = {} worth {}.".format(millage, int(estimate_price)))


if __name__ == '__main__':
    main()
