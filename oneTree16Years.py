tempList = []
tempList2 = []
tempStr = ""
sourcePath = []

divider = "\t"

numberOfTree = 12
numberOfStation = 10
year = 16
print("Loading source path...")
for n in (range(1, numberOfStation+1)):
    sourcePath.append("prunedSource/" + "prunedSource" + str(n) + ".txt")

print(sourcePath)

target = "oneTree16Years.asc"

for i in range(len(sourcePath)):
    with open(sourcePath[i], 'r') as f:
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
# print(tempList)
print("tempList length: " + str(len(tempList)))
for i in range(0, year*numberOfTree):
    for j in range(i, numberOfStation*numberOfTree*year, year*numberOfTree):
        tempList2.append(tempList[j])
# print(tempList2)
print("tempList2 length: " + str(len(tempList2)))

for i in range(len(sourcePath)-1, len(tempList2), len(sourcePath)):
    tempList2[i] = tempList2[i] + "\n"
    for j in range(1, len(sourcePath)):
        tempList2[i-j] = tempList2[i-j] + divider


print(tempList2)
with open(target, "w") as t:
    t.writelines(tempList2)

