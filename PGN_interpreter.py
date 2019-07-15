# Writing functions

# After read and translate is finished, take output
# from translate and write it into a file that can be
# stored as text
def interpret(file_string, engineNameList):  # the engineNameList does not have to be populated.
    i = 0 # index
    # engineNameList = engineNameList not sure if this is necessary
    # colorCrossTable = [] which can be used for wins for scoring wins as black or white heavier if the feature is wanted
    trueCrossTable = [] # it's a real crosstable! ok, it's just a placeholder.
    bulletCrossTable = [] #verbatim
    rapidCrossTable = [] #yep
    classicalCrossTable = [] #having fun here
    engineName = ""
    engineIndexWhite = 0 # used for identifying the index of an engine in engineNameList
    engineIndexBlack = 0
    score = 0
    bulletRapidClassical = 0 # will be determined by a game name.
    while i < len(file_string):
        if file_string[i:i+8] == "White \"":
            # go 7 characters forward to skip 'White "'
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = add_engineName(engineName, engineNameList)
            engineIndexWhite = detect_engineIndex(engineNameList, engineName)
        elif file_string[i:i+8] == "Black \"":
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = add_engineName(engineName, engineNameList)
            engineIndexBlack = detect_engineIndex(engineNameList, engineName)
            score, i = detect_score(file_string, i)
            # colorCrossTable[engineIndexWhite][engineIndexBlack] += score for intentionally for as white/black winrates
            trueCrossTable[engineIndexWhite][engineIndexBlack] += score
            trueCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
            score = 0
        elif file_string[i:i+5] == "Event":
            bulletRapidClassical, i = detectTimeControl(file_string, i)
            if bulletRapidClassical == 1:    
                trueCrossTable = bulletCrossTable
            if bulletRapidClassical == 2:
                trueCrossTable = rapidCrossTable
            if bulletRapidClassical == 3:
                trueCrossTable = classicalCrossTable
        ++i
    i = 0
    return bulletRapidClassical, bulletCrossTable, rapidCrossTable, classicalCrossTable
        
def read_engineName(file_string, engineName, index):
    engineNameLength = 0
    while file_string[index] != "\"":
        engineNameLength += 1
    engineName = file_string[index, index+engineNameLength]
    return engineName
    
def add_engineName(engineName, engineNameList): 
    # adds an engineName to the list if it isn't already in the list
    icheck = 0 # engine name index
    engineNameListLength = len(engineNameList)
    while icheck <= engineNameListLength:
        if icheck == engineNameListLength:
            engineNameList += engineName
            # if the engine's name wasn't detected in the list already
        elif engineName == engineNameList[icheck]:
            break
    return engineNameList
    
def detect_engineIndex(engineNameList, engineName):
    index = 0
    engineIndex = 0
    while True:
        if engineName == engineNameList:
            engineIndex = index
            break
        else:
            ++index
    return engineIndex
    
def expandCrossTable(engineNameList, trueCrossTable):
    listSize = len(engineNameList) # the two dimensional array should have this size
    crossTableSize1 = len(trueCrossTable)
    crossTableSize2 = len(trueCrossTable[0])
    while trueCrossTable < listSize:
        i = 0 # index the first dimension of crosstable list
        while trueCrossTable[i] < listSize:  
            trueCrossTable[i] += 0
        ++i
        
def detect_score(file_string, index):
    score = 0 # If white wins, this will be 1. If white draws, it will be 0.5.
    index += 40 # hopefully speeds the reading along a bit, this feature can be disabled.
    while True:
        if file_string[index:index+4] == "0-1":
            break
        elif file_string[index:index+4] == "1-0":
            score = 1
            break
        elif file_string[index:index+8] == "1/2-1/2":
            score = 0.5
            break
        else:
            ++index
    return score, index


def makeScoreboard(bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList, engineIndex1, engineIndex2): # returns a string
    # this will create a visual representation of the h2h statistics for each engine v. engine
    bulletScoreOne = bulletCrossTable[engineIndex1][engineIndex2]
    bulletScoreTwo = bulletCrossTable[engineIndex2][engineIndex1]
    #blitzScoreOne = blitzCrossTable[engineIndex1][engineIndex2] if the format changes
    #blitzScoreTwo = blitzCrossTable[engineIndex1][engineIndex2]
    rapidScoreOne = rapidCrossTable[engineIndex1][engineIndex2]
    rapidScoreTwo = rapidCrossTable[engineIndex2][engineIndex1]
    classicalScoreOne = classicalCrossTable[engineIndex1][engineIndex2]
    classicalScoreTwo = classicalCrossTable[engineIndex2][engineIndex1]
    gameAmountBullet = amountOfGames(bulletCrossTable, engineIndex1, engineIndex2)
    #gameAmountBlitz = amountOfGames(blitzCrossTable, engineIndex1, engineIndex2)
    gameAmountRapid = amountOfGames(rapidCrossTable, engineIndex1, engineIndex2)
    gameAmountClassical = amountOfGames(classicalCrossTable, engineIndex1, engineIndex2)
    weightedBScoreOne = bulletScoreOne * 0.5
    weightedBScoreTwo = bulletScoreTwo * 0.5
    #weightedBZScoreOne = blitzScoreOne
    #weightedBZScoreTwo = blitzScoreTwo
    weightedRScoreOne = rapidScoreOne * 0.75
    weightedRScoreTwo = rapidScoreTwo * 0.75
    weightedCScoreOne = classicalScoreOne * 1.0
    weightedCScoreTwo = classicalScoreTwo * 1.0
    weightedScoreOne = weightedBScoreOne + weightedRScoreOne + weightedCScoreOne
    weightedScoreTwo = weightedBScoreTwo + weightedRScoreTwo + weightedCScoreTwo
    crossTableVisual = " Event      Games     Score     Weight    " 
    + engineNameList[engineIndex1] + " Score " + engineNameList[engineIndex2] + " Score "
    #end of line 1
    + "\n Bullet      " 
    + (gameAmountBullet) # number of games 
    + "     " + bulletScoreOne + " - " + bulletScoreTwo #h2h game score
    + " 0.5 " # value of bullet games
    + "    " + (weightedBScoreOne) + "        " + (weightedBScoreTwo) 
    # end of line 2
    + "\n Rapid      " 
    + (gameAmountRapid) 
    + "     " + rapidScoreOne + " - " + rapidScoreTwo #h2h game score
    + " 0.75 " # value of bullet games
    + "    " + (weightedRScoreOne) + "        " + (weightedRScoreTwo) 
    # end of line 3
    + "\n Classical      " 
    + (gameAmountClassical) # number of games 
    + "     " + classicalScoreOne + " - " + classicalScoreTwo #h2h game score
    + " 1.0 " # value of bullet games
    + "    " + (weightedCScoreOne) + "        " + (weightedCScoreTwo) 
    # end of line 4
    + "Overall                               " + weightedScoreOne + "                " + weightedScoreTwo
    # end of line 5
    print(crossTableVisual)
    return crossTableVisual
    
def amountOfGames(realCrossTable, engineIndex1, engineIndex2): # will return amount of games played between 2 engines
    gameAmount = realCrossTable[engineIndex1][engineIndex2] + realCrossTable[engineIndex1][engineIndex2]
    return gameAmount
    
def detectTimeControl(file_string, i):
    # 1 = bullet 2 = rapid 3 = classical while 0 probably indicates an error.
    bulletRapidClassical = 0
    while i < len(file_string):
        if file_string[i] == "|":
            expectedMovesConstant = 40
            # this will assume a game length of 40 moves -- the same as human games.
            initialTime = 0 # in minutes
            incrementTime = 0 # in seconds, will be multiplied by expectedMovesConstant
            initialTimeDigits = 0 # used to find out whether a symbol should be interpreted or not
            incrementTimeDigits = 0 # ^
            expectedTime = 0
            if (is_number(file_string[i-1]) and is_number(file_string[i+1])): 
                # if both numbers are right next to the "|"
                if is_number(file_string[i+2]): 
                    incrementTimeDigits = 2
                if is_number(file_string[i-2]): 
                    initialTimeDigits = 2
                initialTime = file_string[i+initialTimeDigits]
                incrementTime = file_string[i+incrementTimeDigits]
            elif (is_number(file_string[i-2]) and is_number(file_string[i+2])): 
                # if both numbers are a spacebar away from what was expected
                if is_number(file_string[i+3]): 
                    incrementTimeDigits = 2
                if is_number(file_string[i-3]): 
                    initialTimeDigits = 2
                initialTime = file_string[i+initialTimeDigits]
                incrementTime = file_string[i+incrementTimeDigits]
            else:
                #if there was no time control detected
                continue
            expectedTime = initialTime * 60 + incrementTime * expectedMovesConstant
            if expectedTime < 360:
                bulletRapidClassical = 1
            elif expectedTime < 540:
                bulletRapidClassical = 2
            else:
                bulletRapidClassical = 3
        elif file_string[i:i+7] == "Bullet":
            bulletRapidClassical = 1
            break
        elif file_string[i:i+8] == "Rapid":
            bulletRapidClassical = 2
            break
        elif file_string[i:i+4] == "Classical":
            bulletRapidClassical = 3
            break
        ++i
    return i, bulletRapidClassical


def is_number(string): # returns a boolean whether the string is a number or not
    if string == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        return True
    else:
        return False


def I_READ(a_filename):
    filename = open(a_filename, "r")
    longest_string_in_python = filename.read()
    return longest_string_in_python

def I_WRITE(a_filename):
    filename = open("a_filename.txt", "w+")
    longest_string_in_python = filename.write()
    
