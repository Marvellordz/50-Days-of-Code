from spellchecker import SpellChecker
checker = SpellChecker()

word = input("Enter a Word : ")
if word in checker:
    print("The word is correct")
else:

    suggestions = checker.candidates(word)
    print('Did you mean ', suggestions)
