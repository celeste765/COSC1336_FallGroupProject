import matplotlib.pyplot as plt


# This function is the encryption backbone basically
# It takes the value of a char and adds the encryption key to it
# It can be made more complex later
def addToOrd(value, encryption_key):
    output = ord(value) + encryption_key
    return output


def readFile():
    fileName = input("Enter the name of the file including the extension.\n")
    print(f"Opening {fileName}.\n")
    encryption_key = input("Enter an encryption key.\n")
    print("Encryption key entered.\n")
    return (fileName, encryption_key)


# This is a dict used to test the plotdata function
test_dictionary = {"e": 1, "c": 3, "d": 5}


def plotData(data):
    x_vals = []
    y_vals = []
    data = data[1]
    for key in data:
        x_vals.append(key)
    for key in data:
        y_vals.append(data[key])

    plt.bar(x_vals, y_vals)
    plt.show()


# This function should encrypt some text given a key as an argument
# The key will be something that makes the encryption unique for that
# file or text


# This function takes a tuple that is returned by the readfile function
# The first value in the tuple is the file information
# The second value in the tuple is the encryption key
def encrypt(info):
    # A dictionary to store the characters and their counts
    fileTestDict = {}
    file = info[0]
    count = 0
    encryption_key = int(info[1])
    encrypted = ""
    with open(file, "r") as file:
        for line in file:
            for character in line:
                encrypted += str(addToOrd(character, encryption_key))
                if character == " ":
                    character = "_"
                elif character == "\n":
                    character = "*"
                if character in fileTestDict:
                    fileTestDict[character] += 1
                else:
                    fileTestDict[character] = 1

    print(encrypted)
    return encrypted, fileTestDict


# This function will do the opposite of the encrypt function given
# a decryption key
def decrypt():
    pass


def main():
    print("Add functions below this print statement.\n")
    encrypt(readFile())
    # plotData()


main()
