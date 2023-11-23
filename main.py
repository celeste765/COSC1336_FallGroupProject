import matplotlib.pyplot as plt


def readFile():
    pass


# This is a dict used to test the plotdata function
# It can be deleted once the function works
test_dictionary = {"e": 1, "c": 3, "d": 5}


def plotData(data):
    x_vals = []
    y_vals = []

    for key in data:
        x_vals.append(key)
    for key in data:
        y_vals.append(data[key])

    plt.bar(x_vals, y_vals)
    plt.show()


# This function should encrypt some text given a key as an argument
# The key will be something that makes the encryption unique for that
# file or text
def encrypt():
    pass


# This function will do the opposite of the encrypt function given
# a decryption key
def decrypt():
    pass


def main():
    print("Add functions below this print statement.")
    plotData(test_dictionary)


main()
