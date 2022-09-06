entryList = [[10, 20, 30, 2], [40, 50, 60, 12], [70, 80, 90, 100]]
resultantLists = []
index = 0

for num in range(len(entryList[0])):
    resultantLists.append([])
    for item in range(len(entryList)):
        resultantLists[index].append(entryList[item][index])
    index = index + 1
for l in resultantLists:
    print(l)
