# A palindrome is a word that is the same when spelt either forward or backward. E.g Eve, Eye, noon etc.

def palindrome():
    text = input('Enter a word to test for palindrome: ')
    word = text.lower()
    a = word[::-1]
    if (word == a):
        print(text, ' is a palindrome')
    else:
        print(text, ' is not a plaindrome')
    return a


palindrome()
