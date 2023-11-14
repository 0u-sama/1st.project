phrase = input("enter phrase\n")
listed = phrase.split(" ")


def reversed_words(words):
    reversed_list = []
    reversed_word = ""
    for i in words:
        for j in i[:: -1]:
            reversed_word = reversed_word + j
        reversed_list.append(reversed_word)
        reversed_word = ""
    count = 0

    for i in listed:
        for j in reversed_list:
            if i == j:
                count += 1

    print(
        f"original paragraph :\n {' '.join(listed)}\n paragraph with reversed words :\n {' '.join(reversed_list)}\n"
        f"number of words that stayed the same after reversing :{count}"
    )


reversed_words(listed)
