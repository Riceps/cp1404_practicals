"""Convert string to words + word count"""

user_string = str(input("Text: ").lower())
user_words = user_string.split(" ")
# print(user_words)

words_to_count = {}
for word in user_words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1
# print(words_to_count)

for word in words_to_count:
    print("{:<6} : {}".format(word, words_to_count[word]))
