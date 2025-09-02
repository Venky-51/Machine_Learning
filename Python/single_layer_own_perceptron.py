# creating my own single layer perceptron

def perceptron(inputs, weights, bias):
    total = 0;

    for i in range(len(inputs)):
        total += (inputs[i] * weights[i])
    total += bias

    if total >= 0:
        return 1
    else:
        return 0

inputs = [1,0]
weights =[0.6, 0.9]
bias = -0.5
print("output is ", perceptron(inputs, weights, bias))
