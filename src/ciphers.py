"""
CSAPX Lab 1: Ciphers

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.
    trade - Ta,b swap the places of the a-th and b-th characters.

All indices numbers (the subscript parameters) are 0-based.

author: Max Klot
"""


def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None
    """
    q = False
    while not q:
        printStr = 'Enter one of the following options:\n  E- Encrypt\n  D- Decrypt\n  Q- Terminate\n'
        userInput = input(printStr)
        validInput = False
        while not validInput:
            if userInput != 'E' and userInput != 'Q' and userInput != 'D' and userInput != 'Q':
                userInput = input("Invalid Selection.\n" + printStr)
            else:
                validInput = True
        if userInput == 'E':
            messageStr = input("Please enter a message to encode:\n")
            operationStr = input("Please enter the transformation operation string:\n")
            transform(messageStr, operationStr, True)
        elif userInput == 'D':
            messageStr = input("Please enter a message to decode:\n")
            operationStr = input("Please enter the transformation operation string:\n")
            transform(messageStr, operationStr, False)
        else:
            q = True


def transform(messageStr: str, transformStr: str, encryptOrDecrypt):
    """
    transform, in this version of the lab, simply tells you what operations are going to be performed.
    :param messageStr: message string
    :param transformStr: transformation operation string
    :param encryptOrDecrypt: encrypts = True, decrypt = False
    :return: None
    """
    transformList = transformStr.split(";")
    print('Generating output...\nTransforming message: ' + messageStr)
    print('Applying...\n')

    if(not encryptOrDecrypt):
        transformList.reverse()

    for i in transformList:
        notalreadyDed = True
        type = i[0]
        parameters = i[1:]
        if not encryptOrDecrypt:
            parameterList = parameters.split(',')
            if type == 'S':
                if len(parameterList) == 1:
                    parameters = parameterList[0] + ',-1'
                else:
                    parameters = parameterList[0] + ',' + str((int(parameterList[1]) * -1))
            if type == 'R':
                if parameterList[0] == '':
                    parameters = '-1'
                else:
                    parameters = str((int(parameterList[0]) * -1))
            if type == 'D':
                notalreadyDed = False
                print('Operation Duplicate (D) - ' + 'Parameters: ' + parameters)
                if len(parameterList) == 1:
                    messageStr = messageStr[0:int(parameterList[0])] + messageStr[int(parameterList[0]) + 1:]
                else:
                    messageStr = messageStr[0:int(parameterList[0])] + messageStr[int(parameterList[0]) + int(parameterList[1]):]
                print(messageStr)


        if type == 'S':
            print('Operation Shift (S) - ' + 'Parameters: ' + parameters)
            print(shift(messageStr, parameters))
            messageStr = shift(messageStr, parameters)
        elif type == 'T':
            print('Operation Trade (T) - ' + 'Parameters: ' + parameters)
            print(trade(messageStr, parameters))
            messageStr = trade(messageStr, parameters)
        elif type == "R":
            print('Operation Rotate (R) - ' + 'Parameters: ' + parameters)
            print(rotate(messageStr, parameters))
            messageStr = rotate(messageStr, parameters)
        elif type == "D" and notalreadyDed:
            print('Operation Duplicate (D) - ' + 'Parameters: ' + parameters)
            print(duplicate(messageStr, parameters))
            messageStr = duplicate(messageStr, parameters)


def shift(messageStr: str, parameters: str) -> str:
    """
    shift will take in string messageStr and string parameters Str, and performs the shift operation.
    :param messageStr: message to transform
    :param parameters: parsameters of the operation
    :return: transformed String
    """
    parametersList = parameters.split(",")
    if len(parametersList) > 1:
        return (messageStr[:int(parametersList[0])] +
                chr(((ord(messageStr[int(parametersList[0])]) - 65 +
                      int(parametersList[1])) % 26 + 65)) + messageStr[int(parametersList[0]) + 1:])
    else:
        return (messageStr[:int(parametersList[0])] +
                chr((ord(messageStr[int(parametersList[0])]) - 65) % 26 + 66)
                + messageStr[int(parametersList[0]) + 1:])


def rotate(messageStr: str, parameters: str) -> str:
    """
    function rotate will rotate the string by specified amount.
    :param messageStr: the string to alter
    :param parameters: parameters for the transformation
    :return: finalized transformation string
    """
    parametersList = parameters.split(',')
    if parametersList[0] == '':
        return messageStr[-1] + messageStr[0:-1]
    else:
        return messageStr[-int(parametersList[0]):] + messageStr[0:-int(parametersList[0])]


def duplicate(messageStr: str, parameters: str) -> str:
    """
    duplicate will duplicate letter at specified index, a specified number of times. Default is 1.
    :param messageStr: provided message string
    :param parameters: index, and then number of duplicates
    :return: altered string
    """
    parametersList = parameters.split(',')
    newStr = ''
    if len(parametersList) == 2:
        newStr = messageStr[0:int(parametersList[0]) + 1]
        for i in range(int(parametersList[1])):
            newStr += messageStr[int(parametersList[0])]
        newStr += messageStr[int(parametersList[0]) + 1:]
    else:
        newStr = messageStr[0:int(parametersList[0]) + 1]
        newStr += messageStr[int(parametersList[0])]
        newStr += messageStr[int(parametersList[0]) + 1:]
    return newStr


def trade(messageStr: str, parameters: str) -> str:
    """
    trade will swap characters at the defined indices.
    :param messageStr: the provided message string
    :param parameters: the indices at which the letters should swap.
    :return: the altered message string.
    """
    parametersList = parameters.split(",")
    # I do realize typecasting before having to do all the algorithms would have been more efficient,
    # but I had already written them by this point
    for i in parametersList:
        i = int(i)
    parametersList.sort()
    newStr = (messageStr[0:int(parametersList[0])] + messageStr[int(parametersList[1])]
              + messageStr[int(parametersList[0]) + 1:int(parametersList[1])]
              + messageStr[int(parametersList[0])] + messageStr[int(parametersList[1]) +1:])
    return newStr

if __name__ == '__main__':
    main()
