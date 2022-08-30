def getMean(lists):
    mean = sum(lists)/len(lists)
    return print(round(mean, 3))


def getMode(lists):
    frequency = {}
    for i in lists:
        frequency.setdefault(i, 0)
        frequency[i] += 1

        frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    return print(mode)


list1 = [1, 2, 3, 1, 2, 3, 4, 9, 0, 0, 0, 2,  3, 1, 0, 0, 1, 0]
getMean(list1)
getMode(list1)
