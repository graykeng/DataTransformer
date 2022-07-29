
tempList = []
tempStr = ""
sourcePath = []

divider = "\t"

numberOfTree = 12
numberOfStation = 10
for n in (range(1, numberOfStation+1)):
    sourcePath.append("prunedSource/" + "prunedSource" + str(n) + ".txt")
print(sourcePath)
targetPath = 'output.asc'
for i in range(len(sourcePath)):
    if i == 0:
        with open(sourcePath[0], 'r') as f:

            for line in f.readlines():
                countTab = 0
                for char in line:
                    if char != "\t":
                        if countTab >= numberOfTree:
                            # tempList.append(tempStr)
                            tempStr = ""
                            break
                        else:
                            tempStr = tempStr + char
                    else:
                        tempList.append(tempStr)
                        tempStr = ""
                        countTab = countTab + 1
    else:
        # i = 1 and more
        j = i + 1
        k = 0
        tempStr = ""
        with open(sourcePath[i], 'r') as f:
            for line in f.readlines():
                countTab = 0
                for char in line:
                    if char != "\t":
                        if countTab >= numberOfTree:
                            # tempList.insert(i + j * k, tempStr)
                            tempStr = ""
                            k = k + 1
                            break
                        else:
                            tempStr = tempStr + char
                    else:
                        tempList.insert(i + j * k, tempStr)
                        tempStr = ""
                        k = k + 1
                        countTab = countTab + 1


print(tempList)

for l in range(len(sourcePath)-1, len(tempList), len(sourcePath)):
    tempList[l] = tempList[l] + "\n"
    for m in range(1, len(sourcePath)):
        tempList[l-m] = tempList[l-m] + divider


with open(targetPath, 'w') as t:
    t.writelines(tempList)

# print(tempList)
# print(len(tempList))
