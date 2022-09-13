from difflib import SequenceMatcher


def matcher():
    text1 = input('Enter the first text or sentence: ')
    text2 = input('Enter the second text or sentence: ')
    sequenceRate = SequenceMatcher(None, text1, text2).ratio()
    print(f"Both are {round(sequenceRate * 100, 2)} % similar")


matcher()
