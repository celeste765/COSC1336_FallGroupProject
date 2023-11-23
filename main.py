import matplotlib.pyplot as plt


def createMessage():
    message = input("Enter the message you would like to encrypt.")
    message_name = input("What would you like to name this message?")
    with open(f"{message_name}.txt", "w") as file:
        file.write(message)


# This function is the encryption backbone basically
# It takes the value of a char and adds the encryption key to it
# It can be made more complex later
def addToOrd(value, encryption_key):
    output = ord(value) + encryption_key
    return output


def readFile():
    fileName = input("Enter the name of the file including the extension.\n")
    print(f"\nOpening {fileName}.\n")
    encryption_key = input("\nEnter an encryption key.\n")
    print("\nEncryption key entered.\n")
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


def plot_no_library():
    # Here we need to write a function to plot the data without a library
    # similar to the example in the google doc here:
    # https://docs.google.com/document/d/1_Ax3DurS4JfI8jJaGuU6g3Fc26kx0lMokNRkqAaI8BE/edit

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
                encrypted += "x"
                if character == " ":
                    character = "_"
                elif character == "\n":
                    character = "*"
                if character in fileTestDict:
                    fileTestDict[character] += 1
                else:
                    fileTestDict[character] = 1

    with open("encrypted.txt", "w") as enc:
        enc.write(encrypted)
    return (encrypted, fileTestDict)


# This function will do the opposite of the encrypt function given
# a decryption key using the chr instead of the ord function
def decrypt(data):
    file = data[0]
    encryption_key = data[1]
    message = ""
    with open(file, "r") as fl:
        chars = fl.read().split("x")
        for item in chars:
            if item == """""":
                del chars[chars.index(item)]
        print(chars)
    for item in chars:
        if item == "38":
            message += " "
        else:
            item = int(item)
            encryption_key = int(encryption_key)
            message += str(chr(item - encryption_key))

    print(message)


def main():
    print("Add functions below this print statement.\n")
    decrypt(readFile())
    # encrypt(readFile())
    # plotData()
    # createMessage()


main()
