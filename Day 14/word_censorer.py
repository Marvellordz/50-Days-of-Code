from better_profanity import profanity


def censorer():
    text = input('Enter the text you wish to censor: ')
    censoredText = profanity.censor(text)
    print(censoredText)


censorer()
