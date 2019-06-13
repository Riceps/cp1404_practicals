user_name = input("What is your name? ")
vowels = "bcdfghjklmnpqrstvwxyz"
number_of_vowels = 0
for i in range(len(user_name)):
    if user_name[i].lower() in vowels:
        number_of_vowels += 1
print(number_of_vowels)
