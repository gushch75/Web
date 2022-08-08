print(open("f1.txt").read())
allPowers = []
powerMultiplier = {}
for names in ["f1.txt", "f2.txt"]:
    curData = open(names).read().split("+")
    for elem in curData:
        print(elem.strip())
        if elem.strip().find("x") == -1:
            allPowers.append(0)
            if 0 not in powerMultiplier:
                powerMultiplier[0] = 0
            powerMultiplier[0] += int(elem.strip())
        else:
            multiplierString = elem.split("x")[0].split("*")[0].strip()
            multiplier = 1
            if multiplierString != "":
                multiplier = int(multiplierString)
            powerString = elem.split("x")[-1].split("^")[-1].strip()
            power = 1
            if powerString != "":
                power = int(powerString)
            allPowers.append(power)
            if power not in powerMultiplier:
                powerMultiplier[power] = 0
            powerMultiplier[power] += multiplier
allPowers.sort(reverse=True)
f3 = open("f3.txt", "w")
isFirstPower = True
for i in range(len(allPowers)):
    if i != 0 and allPowers[i] == allPowers[i - 1]:
        continue
    curAdd = ""
    if allPowers[i] == 0:
        curAdd += str(powerMultiplier[allPowers[i]])
    elif allPowers[i] == 1:
        if powerMultiplier[allPowers[i]] == 1:
            curAdd += "x"
        else:
            curAdd += str(powerMultiplier[allPowers[i]]) + "*x"
    else:
        if powerMultiplier[allPowers[i]] == 1:
            curAdd += "x^" + str(allPowers[i])
        else:
            curAdd += str(powerMultiplier[allPowers[i]]) + "*x^" + str(allPowers[i])
    if not isFirstPower:
        f3.write("+")
    f3.write(curAdd)
    isFirstPower = False
f3.write("\n")
f3.close