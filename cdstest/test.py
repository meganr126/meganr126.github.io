def importFile(file):
    f = open(file, 'r')
    return f.read()

def parse(fFile):
    fFile = fFile.lower()
    fFile = fFile.replace(';',' ').replace(':',' ').replace(',',' ').replace('“',' ').replace('”',' ')
    fList = fFile.replace('.',' ').replace(';',' ').replace('’s',' ').split()
    #print(fList)
    d = {}
    for word in fList:
        #print(word)
        if word in d:
            #print(word,d[word])
            d[word]+=1
            #print(word, d[word])
        else:
            d[word] = 1
            #print("--",word,d[word])
    #print(fFile)
    return d

def printResult(dic):
    excluded = ["for", "and", "nor", "but", "or",
                "yet", "so", "if", "then", "a",
                "the", "it", "of", "in", "on", "are",
                "is", "to", "be", "this",
                "that", "with", "have", "as", "been",
                "these", "those", "can", "about", "who", "am"]
    for key, value in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        if (value>1 and (key not in excluded)):
            print(str(key)+": "+str(value))

def main():
    file = importFile("testtxt.txt")
    dictResult = parse(file)
    printResult(dictResult)

main()
