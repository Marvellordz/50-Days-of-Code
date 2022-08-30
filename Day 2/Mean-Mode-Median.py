def getMean(lists):
    mean = sum(lists)/len(lists)
    return print('The mean of ', lists, 'is: ', round(mean, 3))


def getMode(lists):
    frequency = {}
    for i in lists:
        frequency.setdefault(i, 0)
        frequency[i] += 1

        frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    return print('The mode of ', lists, 'is: ', mode)


def getMedian(lists):
    lists.sort()

    if len(lists) % 2 == 0:
        mid1 = lists[len(lists)//2]
        mid2 = lists[len(lists)//2 - 1]
        median = (mid1 + mid2)/2
    else:
        median = lists[len(lists)//2]
    return print('The median of ', lists, 'is: ', int(median))


testList = [1, 1, 3, 2,  1, 2]
getMean(testList)
getMode(testList)
getMedian(testList)
