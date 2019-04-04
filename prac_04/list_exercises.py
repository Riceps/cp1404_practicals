def main():
    numbers = []
    for number in range(0, 5):
        numbers.append(int(input("Pick number {}: ".format(number + 1))))

    print(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    average_of_numbers = sum(numbers) / len(numbers)
    print("The average of the numbers is {}".format(average_of_numbers))
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = str(input("What is your username: "))
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
