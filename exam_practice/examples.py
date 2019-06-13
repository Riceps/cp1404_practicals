import random


def main():
    # Example 2
    age = int(input("What is your age? "))
    for i in range(age, 0, -1):
        print(i * i)

    # Example 3
    x = 9
    y = 11
    print(total_numbers(x, y))

    # Example 4
    s, t = "James Brown", ""
    for i in range(len(s)):
        t += s[i - len(s)]
    print(t)

    # Example 5
    a = [1, 2, 3]
    a.append(a[1])
    a.reverse()
    print(a)

    # Example 6
    s = "This is a sentence with words in it"
    words = s.split()
    print(words)
    print(len(words))

    # Example 7
    n = 4
    print(get_random_number_list(n))

    # Example 8
    input_string = str(input("Gimme a string: "))
    print(get_double_string(input_string))


def get_random_number_list(n):
    random_number_list = []
    for i in range(n):
        random_number_list.append(random.randint(1, 10 * n))
    return random_number_list


def total_numbers(x, y):
    total_number = 0
    if x >= y:
        return total_number
    else:
        for i in range(x, y + 1):
            total_number += i
    return total_number


def get_double_string(input_string):
    double_string = ""
    for i in range(len(input_string)):
        double_string += input_string[i] * 2
    return double_string


main()
