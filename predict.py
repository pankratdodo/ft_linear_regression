import os.path


def error(mess):
    print(mess)
    exit(-1)


def main():
    file_name = "parameters.txt"
    if not os.path.isfile(file_name):
        error("File with params {} does not exist.".format(file_name))
    param_file = open(file_name, 'r')
    lines = param_file.read().split('\n')
    lines = list(filter(None, lines))
    if len(lines) != 2:
        error("File {} is incorrect.".format(file_name))
    try:
        t0 = float(lines[0])
        t1 = float(lines[1])
    except ValueError:
        error("Params have to be float number.")
    if t0 == 0 or t1 == 0:
        error("Params have to be not 0. Train the neural network.")
    try:
        mileage = float(input("Enter a mileage: "))
    except ValueError:
        error("Millage have to be float number.")
    if mileage <= 0 or mileage > 10000000:
        error("Millage have to be more than 0 and less than 10000000")
    price = t0 + t1 * mileage
    print("Car with millage = {} worth {}.".format(mileage, price))


if __name__ == '__main__':
    main()
