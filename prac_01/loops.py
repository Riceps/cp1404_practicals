"Prints all numbers between 1 and 20 inclusive, with a step of 2 (i.e. all odd numbers)"
for i in range(1, 21, 2):
    "prints number i and a space TODO:(question what (end) does)"
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Enter a whole number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
