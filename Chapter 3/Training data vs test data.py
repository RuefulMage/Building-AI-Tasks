import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''



def main():
    train_input_file = StringIO(train_string)
    test_input_file = StringIO(test_string)

    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading

    trainData = np.genfromtxt(train_input_file, skip_header=1)
    trainInputs = np.asarray(trainData[:, : len(trainData) - 1])
    trainExpectedOutput = np.asarray(trainData[:, len(trainData) - 1])

    coefficients = np.linalg.lstsq(trainInputs, trainExpectedOutput)[0]

    testData = np.genfromtxt(test_input_file, skip_header=1)
    testInputs = np.asarray(testData[:, : len(testData[0]) - 1])
    testExpectedOutput = np.asarray(testData[:, len(testData) - 1])

    print(coefficients)
    print(testInputs @ coefficients)


main()
