import random

random_char = chr(random.randint(97, 122))

random_upper_char = chr(random.randint(65, 90))

st = input("enter your message: ")
words = st.split(" ")
coding = input("1 for coding or 0 for decoding: ")
coding = True if (coding == "1") else False

if coding:
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_str = random_char + word[1:] + word[0] + random_upper_char
            new_words.append(new_str)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))

else:
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_str = word[3:-3]
            new_str = new_str[-1] + new_str[:-1]
            new_words.append(new_str)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
