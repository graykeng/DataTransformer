
startYear = "1970"
endYear = "1985"
tempStr = ""
tempList = []
numberOfTree = 12
numberOfStation = 10

sourcePath = []
targetPath = []

for i in (range(1, numberOfStation+1)):
    sourcePath.append("source/" + "bt" + "%03d" % i + "-noaa.rwl.txt")
for i in (range(1, numberOfStation+1)):
    targetPath.append("target/" + "TARGET" + str(i) + ".txt")

for i in range(len(sourcePath)):
    with open(sourcePath[i], "r") as f:
        file = f.readlines()
    process = -1
    for line in file:

        if line.startswith(startYear) or process == 1:
            print(line)
            tempList.append(line)
            process = 1
            if line.startswith(endYear):
                process = -1

    print("Target: " + targetPath[i])

    tempList2 = []
    with open(targetPath[i], "w") as b:
        for string in tempList:
            tempList2.append(string[5:])
        b.writelines(tempList2)

    tempList = []

print(tempList)



