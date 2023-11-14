word = input("Enter the word u want to compare:\n")
old_word = input("Enter the word u want to compare with:\n")
listed_word = []
for i in old_word: listed_word.append(i)
last_character = listed_word[-1]
listed_word[-1] = listed_word[-2]
listed_word[-2] = last_character
new_word = "".join(listed_word)

if new_word == word: print("هذا جناس")
else: print("هذا ليس جناسا")

