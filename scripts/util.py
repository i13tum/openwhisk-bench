def writeListToFile(fileName, content):
    f = open(fileName, "w")
    f.write("".join(str(e) + " " for e in content))
    f.close()


def readFileToArray(fileName):
    return [line.rstrip('\n') for line in open(fileName)]