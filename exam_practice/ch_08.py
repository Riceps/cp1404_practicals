text = "This is a sentence"
list_of_words = text.split()
print(list_of_words)
short_words = [word for word in list_of_words if len(word) <= 2]
print(short_words)

for i in range(1900, 2018, 4):
    print(i)

numbers = [29, 54, 67, 1, 2, 30, 69, 420]
numbers.sort()
print(numbers)
print(len(numbers))
median_position = int(len(numbers)/2)
median = numbers[median_position - 1]
print(median)
