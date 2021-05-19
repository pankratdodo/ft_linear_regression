# ft_linear_regression
## Installation and run
1. Download/Clone this repo:
```
git clone https://github.com/pankratdodo/ft_linear_regression.git
```
2. `cd` into directrory and run this to train model:
```
cd ft_linear_regression && python3 train.py
```
3. To predict any value run:
```
python3 predict.py
```

## Mandatory part
You will implement a simple linear regression with a single feature - in this case, the mileage of the car.
To do so, you need to create two programs :

- The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price:
```
estimatePrice(mileage) = θ0 + (θ1 * mileage)
```
Before the run of the training program, theta0 and theta1 will be set to 0.

- The second program will be used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program.

You will be using the following formulas:
```
tmpθ0 = learningRate * 1/m ∑mi=0 (estimatePrice(mileage[i]) − price[i])
tmpθ1 = learningRate * 1/m ∑mi=0 (estimatePrice(mileage[i]) − price[i]) * milleage[i]
```
Note that the estimatePrice is the same as in our first program, but here it uses
your temporary, lastly computed theta0 and theta1.
Also, don’t forget to simultaneously update theta0 and theta1.

## Bonus part
- Plotting the data into a graph to see their repartition.
- Plotting the line resulting from your linear regression into the same graph. 
- Possible to change learning rate and value of epchos by flags `-lr`, `-epchos`.
- Colour of responses.
