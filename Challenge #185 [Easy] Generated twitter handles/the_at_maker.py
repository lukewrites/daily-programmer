"""
Online at:
https://www.reddit.com/r/dailyprogrammer/comments/2jt4cx/10202014_challenge_185_easy_generated_twitter/clicmu7
"""

def the_at_maker():
    at_words = []
    with open("WordList.txt", 'r', errors="ignore") as read_words:
        for word in read_words:
            if "'" not in word:
                if word[:3] == 'att':
                    at_words.append(word.replace('att', '@', 1))
                elif word[:2] == 'at':
                    at_words.append(word.replace('at', '@', 1))
    at_words.sort(key=len)
    print("The short ones:")
    for i in range(10):
        print(at_words[i])
    print('The long ones:')
    for i in range(1,10):
        print(at_words[-11+i])


def the_at_maker_bonus_version():
    at_words = []
    with open("WordList.txt", 'r', errors="ignore") as read_words:
        for word in read_words:
            if "'" not in word:
                if 'at' in word:
                    if 'att' in word:
                        at_words.append(word.replace('att', '@').replace('at', '@'))
                    else:
                        at_words.append(word.replace('at', '@'))
    at_words.sort(key=len)
    print("The short ones:")
    for i in range(10):
        print(at_words[i])
    print('The long ones:')
    for i in range(1,10):
        print(at_words[-11+i])