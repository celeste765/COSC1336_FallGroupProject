import matplotlib.pyplot as plt

fileName = input("Enter the name of the file including the extension.\n")
print(f"Opening {fileName}.\n")


def readFile(file):
    # A dictionary to store the characters and their counts
    fileTestDict = {}
    lines = []
    with open(file, "r") as file:
        for line in file:
            for character in line:
                if character in fileTestDict:
                    fileTestDict[character] += 1
                else:
                    fileTestDict[character] = 1

        print(fileTestDict)

    return lines


# This is a dict used to test the plotdata function
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
    print("Add functions below this print statement.\n")
    readFile(fileName)


main()
