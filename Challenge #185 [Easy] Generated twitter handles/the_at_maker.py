def the_at_maker():
    at_words = []
    with open("WordList.txt", 'r', errors="ignore") as read_words:
        for word in read_words:
            if "'" not in word:
                if word[:3] == 'att':
                    at_words.append(word.replace('att', '@', 1).replace('at', '@'))

                elif word[:2] == 'at':
                    at_words.append(word.replace('at', '@', 1))
    at_words.sort(key=len)
    print("The short ones:")
    for i in range(10):
        print(at_words[i])
    print('The long ones:')
    for i in range(1,10):
        print(at_words[-i])