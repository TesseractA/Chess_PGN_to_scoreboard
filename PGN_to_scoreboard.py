# PGN-To-Scoreboard

import sys
#use sys.argv to allow for input of PGN file names

def __main__():
    scoreboard = "" # Will be appended to
    file_name_list = []
    PGN_file_names = str(sys.argv)
    PGN_file_names = ['/Users/gj/scoreboard_from_PGN/ccc-9-the-gauntlet-semifinals-1.pgn']
    bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList = [], [], [], []
    for PGN_name in PGN_file_names:
        print("Hello, world!")
        if PGN_name != 'PGN_to_scoreboard':
            file_name_list.append(PGN_name)
            file_string = I_READ(PGN_name)
            print("Read file!")
            bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList = interpret(file_string, bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList)
    for noob in engineNameList: # noob is the engine in question
        for skrub in engineNameList: # skrub is another engine in question
            print(noob + " vs. " + skrub)
            engineIndex1 = detect_engineIndex(engineNameList, noob)
            engineIndex2 = detect_engineIndex(engineNameList, skrub)
            if engineIndex1 != engineIndex2:
                print(noob + " " + skrub + " works!")
                scoreboard += makeScoreboard(bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList, engineIndex1, engineIndex2)
            else:
                print("An engine can\'t play itself! Not in these tournaments...")
    I_WRITE("CCC_Scoreboard.txt", scoreboard)
        
# TODO create an if statement for 
# [Event "CCC 9: The Gauntlet Semifinals Test (1|1)"]
# [Event "CCC 10: XX Final Bullet  (1|1)"]
# [Event "CCC 10: XX Final Rapid  (1|1)"]
# Maybe recognize "Bullet" and "Rapid" in each of the different files?
# TODO create a recognition statement for which engine is playing black and which is playing white
# [White "Stockfish"]
# [Black "Allie"]
# TODO compare each engine name in each PGN to a new engine and record to a list.
# TODO create a list of scores on each engine
# TODO create an if statement for recognizing what a new game is ending.
# a string of length 3 0-1
# a string of length 3 1-0
# a string of length 7 1/2-1/2
#  


# Writing functions

# After read and translate is finished, take output
# from translate and write it into a file that can be
# stored as text
def interpret(file_string, bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList):
    # file_string is the text of a file in string form
    # the bulletCrossTable, rapidCrossTable and classicalCrosstable are 2-D arrays, but can be initialized as just an array
    # none of these lists have to be populated, they are initialized elsewhere
    i = 0 # index
    # colorCrossTable = [] which can be used for wins for scoring wins as black or white heavier if the feature is wanted
    trueCrossTable = [] # it's a real crosstable! ok, it's just a placeholder.
    engineName = ""
    engineIndexWhite = 0 # used for identifying the index of an engine in engineNameList
    engineIndexBlack = 0
    score = 0
    bulletRapidClassical = 0 # will be determined by an event name. 1 means bullet, 2 means rapid, 3 means classical
    recorded_EventString = ""
    print("Interpreter executing.")
    while i < len(file_string):
        if file_string[i:i+7] == "White \"":
            print("Found a white engine.")
            # go 7 characters forward to skip 'White "'
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = add_engineName(engineName, engineNameList)
            engineIndexWhite = detect_engineIndex(engineNameList, engineName)
        elif file_string[i:i+7] == "Black \"":
            print("Found a black engine.")
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = add_engineName(engineName, engineNameList)
            engineIndexBlack = detect_engineIndex(engineNameList, engineName)
            score, i = detect_score(file_string, i)
            # colorCrossTable[engineIndexWhite][engineIndexBlack] += score for intentionally for as white/black winrates
            print("Expanding crosstable...")
            print("the value of bulletRapidClassical is: " + str(bulletRapidClassical))
            if bulletRapidClassical == 1:
                print("This is a generalized crossTable1: " + str(trueCrossTable) + " \nThis is a bullet crossTable: " + str(bulletCrossTable))    
                trueCrossTable = bulletCrossTable
                trueCrossTable = expandCrossTable(engineNameList, trueCrossTable)
                bulletCrossTable = expandCrossTable(engineNameList, bulletCrossTable)
                trueCrossTable[engineIndexWhite][engineIndexBlack] += score
                trueCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                bulletCrossTable[engineIndexWhite][engineIndexBlack] += score
                bulletCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                print("This is a generalized crossTable2: " + str(trueCrossTable) + " \nThis is a bullet crossTable: " + str(bulletCrossTable))
                print("This is a generalized crossTable3: " + str(trueCrossTable) + " \nThis is a bullet crossTable: " + str(bulletCrossTable))
            elif bulletRapidClassical == 2:
                print("This is a generalized crossTable1: " + str(trueCrossTable) + " \nThis is a rapid crossTable: " + str(rapidCrossTable))
                trueCrossTable = rapidCrossTable
                trueCrossTable = expandCrossTable(engineNameList, trueCrossTable)
                rapidCrossTable = expandCrossTable(engineNameList, rapidCrossTable)
                trueCrossTable[engineIndexWhite][engineIndexBlack] += score
                trueCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                rapidCrossTable[engineIndexWhite][engineIndexBlack] += score
                rapidCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                print("This is a generalized crossTable2: " + str(trueCrossTable) + " \nThis is a rapid crossTable: " + str(rapidCrossTable))
                print("This is a generalized crossTable3: " + str(trueCrossTable) + " \nThis is a rapid crossTable: " + str(rapidCrossTable))
            elif bulletRapidClassical == 3:
                print("This is a generalized crossTable1: " + str(trueCrossTable) + " \nThis is a classical crossTable: " + str(classicalCrossTable))
                trueCrossTable = classicalCrossTable
                trueCrossTable = expandCrossTable(engineNameList, trueCrossTable)
                classicalCrossTable = expandCrossTable(engineNameList, classicalCrossTable)
                trueCrossTable[engineIndexWhite][engineIndexBlack] += score
                trueCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                classicalCrossTable[engineIndexWhite][engineIndexBlack] += score
                classicalCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
                print("This is a generalized crossTable2: " + str(trueCrossTable) + " \nThis is a classical crossTable: " + str(classicalCrossTable))
                print("This is a generalized crossTable3: " + str(trueCrossTable) + " \nThis is a classical crossTable: " + str(classicalCrossTable))
            print(str(trueCrossTable[engineIndexWhite][engineIndexBlack]) + " This is a score!")
            print(str(rapidCrossTable) + " This is a table!")
            print(str(rapidCrossTable[engineIndexWhite][engineIndexBlack]) + " This is a rapid score!")
            score = 0
        elif file_string[i:i+5] == "Event":
            print("Event: " + recorded_EventString)
            testChunkSize = 20
            if file_string[i:i+testChunkSize] != recorded_EventString:
                print("It's recording an event string: " + recorded_EventString)
                recorded_EventString = file_string[i:i+testChunkSize]
                bulletRapidClassical, i = detectTimeControl(file_string, i)
                if bulletRapidClassical == 1:    
                    trueCrossTable = bulletCrossTable
                    bulletCrossTable = trueCrossTable
                elif bulletRapidClassical == 2:
                    trueCrossTable = rapidCrossTable
                    rapidCrossTable = trueCrossTable
                elif bulletRapidClassical == 3:
                    trueCrossTable = classicalCrossTable
                    classicalCrossTable = trueCrossTable
        i += 1
    return bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList
   
def read_engineName(file_string, engineName, index):
    engineNameLength = 0
    print("Reading engine name...")
    while file_string[index] != "\"":
        engineNameLength += 1
        index += 1
    engineName = file_string[index-engineNameLength:index]
    print("The engine\'s name is " + engineName + "!")
    return engineName
    
def add_engineName(engineName, engineNameList): 
    # adds an engineName to the list if it isn't already in the list
    icheck = 0 # engine name index
    engineNameListLength = len(engineNameList)
    while icheck <= engineNameListLength:
        if icheck == engineNameListLength:
            engineNameList.append(engineName)
            # if the engine's name wasn't detected in the list already
            break
        elif engineName == engineNameList[icheck]:
            break
        icheck += 1
    return engineNameList
    
def detect_engineIndex(engineNameList, engineName):
    index = 0
    print("Detecting engine index...")
    while True:
        if engineName == engineNameList[index]:
            print("Found " + engineName + "\'s Index!")
            break
        else:
            index += 1
    return index
    
def expandCrossTable(engineNameList, trueCrossTable):
    listSize = len(engineNameList) # both dimensions of the crosstable should be this large
    i1 = 0 # cycles through each of the elements in the first dimension
    crossTableSize1 = len(trueCrossTable)
    crossTableSize2 = 0 # initialization
    while i1 < listSize:
        # index the second dimension of crosstable list
        crossTableSize1 = len(trueCrossTable)
        try:
            crossTableSize2 = len(trueCrossTable[i1])
        except:
            crossTableSize2 = 0
        if crossTableSize1 < listSize:
            trueCrossTable.append([])
        while crossTableSize2 < listSize:  
            trueCrossTable[i1].append(0)
            crossTableSize2 = len(trueCrossTable[i1])
        i1 += 1
    crossTableSize1 = len(trueCrossTable)
    print("This is the crosstable's size: " + str(crossTableSize1) + "\n and this is the engineNameList's size: " + str(crossTableSize2))
    return trueCrossTable
        
def detect_score(file_string, index):
    score = 0 # If white wins, this will be 1. If white draws, it will be 0.5.
    # index += 10 # hopefully speeds the reading along a bit, this feature can be disabled.
    while True:
        if file_string[index:index+3] == "0-1":
            print("Found a black-won game.")
            break
        elif file_string[index:index+3] == "1-0":
            score = 1
            print("Found a white-won game.")
            index += 200 # speeding along...
            break
        elif file_string[index:index+7] == "1/2-1/2":
            score = 0.5
            print("Found a drawn game.")
            index += 200 # speedy!
            break
        elif file_string[index:index+10] == "disconnect":
            index += 200 # welp this is pointless
            print("Warning! Disconnects in the PGN could alter scores.")
            break
        else:
            index += 1
    return score, index


def makeScoreboard(bulletCrossTable, rapidCrossTable, classicalCrossTable, engineNameList, engineIndex1, engineIndex2): # returns a string
    # this will create a visual representation of the h2h statistics for each engine v. engine 
    bulletWeightConstant = 0.5
    rapidWeightConstant = 0.75
    classicalWeightConstant = 1.00
    # initialized variables
    bulletScoreOne = 0
    bulletScoreTwo = 0
    rapidScoreOne = 0
    rapidScoreTwo = 0
    classicalScoreOne = 0
    classicalScoreTwo = 0
    weightedBScoreOne = 0
    weightedBScoreTwo = 0
    weightedRScoreOne = 0
    weightedRScoreTwo = 0
    weightedCScoreOne = 0
    weightedCScoreTwo = 0
    weightedScoreOne = 0
    weightedScoreTwo = 0 
    gameAmountBullet = 0
    gameAmountRapid = 0
    gameAmountClassical = 0
    try:
        bulletScoreOne = bulletCrossTable[engineIndex1][engineIndex2]
        bulletScoreTwo = bulletCrossTable[engineIndex2][engineIndex1]
        gameAmountBullet = amountOfGames(bulletCrossTable, engineIndex1, engineIndex2)
        weightedBScoreOne = bulletScoreOne * bulletWeightConstant
        weightedBScoreTwo = bulletScoreTwo * bulletWeightConstant
    except:
        pass
        #blitzScoreOne = blitzCrossTable[engineIndex1][engineIndex2] if the format changes
        #blitzScoreTwo = blitzCrossTable[engineIndex1][engineIndex2]
    try:
        rapidScoreOne = rapidCrossTable[engineIndex1][engineIndex2]
        rapidScoreTwo = rapidCrossTable[engineIndex2][engineIndex1]
        gameAmountRapid = amountOfGames(rapidCrossTable, engineIndex1, engineIndex2)
        weightedRScoreOne = rapidScoreOne * rapidWeightConstant
        weightedRScoreTwo = rapidScoreTwo * rapidWeightConstant
    except:
        pass
    try:
        classicalScoreOne = classicalCrossTable[engineIndex1][engineIndex2]
        classicalScoreTwo = classicalCrossTable[engineIndex2][engineIndex1]
        gameAmountClassical = amountOfGames(classicalCrossTable, engineIndex1, engineIndex2)
        weightedCScoreOne = classicalScoreOne * classicalWeightConstant
        weightedCScoreTwo = classicalScoreTwo * classicalWeightConstant
    except:
        pass
    #gameAmountBlitz = amountOfGames(blitzCrossTable, engineIndex1, engineIndex2)
    #weightedBZScoreOne = blitzScoreOne
    #weightedBZScoreTwo = blitzScoreTwo
    weightedScoreOne = weightedBScoreOne + weightedRScoreOne + weightedCScoreOne
    weightedScoreTwo = weightedBScoreTwo + weightedRScoreTwo + weightedCScoreTwo
    crossTableVisual = "\n Event      Games     Score     Weight    " + engineNameList[engineIndex1] + " Score " + engineNameList[engineIndex2] + " Score "
    #end of line 1
    if gameAmountBullet != 0:
        crossTableVisual += "\n Bullet      " + str(gameAmountBullet) + "     " + str(bulletScoreOne) + " - " + str(bulletScoreTwo) + " " + str(bulletWeightConstant) + "     " + str(weightedBScoreOne) + "        " + str(weightedBScoreTwo) # number of games, h2h game score, value of bullet games 
        # end of line 2
    if gameAmountRapid != 0:
        crossTableVisual += "\n Rapid      " + str(gameAmountRapid) + "     " + str(rapidScoreOne) + " - " + str(rapidScoreTwo) + " " + str(rapidWeightConstant) + "     " + str(weightedRScoreOne) + "        " + str(weightedRScoreTwo) # number of games, h2h game score, value of bullet games
        # end of line 3
    if gameAmountClassical != 0:
        crossTableVisual += "\n Classical      " + str(gameAmountClassical) + "     " + str(classicalScoreOne) + " - " + str(classicalScoreTwo) + " " + str(classicalWeightConstant) + "     " + str(weightedCScoreOne) + "        " + str(weightedCScoreTwo) # number of games, h2h game score, value of bullet games
        # end of line 4
    crossTableVisual += "\nOverall                                   " + str(weightedScoreOne) + "       " + str(weightedScoreTwo)
    # end of line 5
    print(crossTableVisual)
    return crossTableVisual
    
def amountOfGames(realCrossTable, engineIndex1, engineIndex2): # will return amount of games played between 2 engines
    gameAmount = realCrossTable[engineIndex1][engineIndex2] + realCrossTable[engineIndex1][engineIndex2]
    return gameAmount
    
def detectTimeControl(file_string, i):
    # 1 = bullet 2 = rapid 3 = classical while 0 probably indicates an error.
    bulletRapidClassical = 0
    initial_i = int(i)
    while i < len(file_string):
        if file_string[i] == "|":
            initialTime = 0 # in minutes
            incrementTime = 0 # in seconds, will be multiplied by expectedMovesConstant
            initialTimeDigits = 1 # used to find out whether a symbol should be interpreted or not
            incrementTimeDigits = 1 # ^
            expectedTime = 0
            if (is_digit(file_string[i-1]) and is_digit(file_string[i+1])): 
                # if both numbers are right next to the "|"
                if is_digit(file_string[i+2]): 
                    incrementTimeDigits = 2
                if is_digit(file_string[i-2]): 
                    initialTimeDigits = 2
                initialTime = int(file_string[i-initialTimeDigits:i]) * 60 # initial time in seconds
                incrementTime = int(file_string[i+1:i+incrementTimeDigits+1]) # increment time in seconds
                expectedTime = computeTimeTC(initialTime, incrementTime)
            elif (is_digit(file_string[i-2]) and is_digit(file_string[i+2])): 
                # if both numbers are a spacebar away from what was expected
                if is_digit(file_string[i+3]): 
                    incrementTimeDigits = 2
                if is_digit(file_string[i-3]): 
                    initialTimeDigits = 2
                initialTime = int(file_string[i-initialTimeDigits:i])
                incrementTime = int(file_string[i+1:i+incrementTimeDigits+1])
                expectedTime = computeTimeTC(initialTime, incrementTime)
            else:
                #if there was no time control detected
                continue
            print("Expected time: " + str(expectedTime))
            if expectedTime < 360:
                bulletRapidClassical = 1
                break
            elif expectedTime < 540:
                bulletRapidClassical = 2
                break
            else:
                bulletRapidClassical = 3
                break
        elif file_string[i:i+7] == "Bullet":
            bulletRapidClassical = 1
            break
        elif file_string[i:i+8] == "Rapid":
            bulletRapidClassical = 2
            break
        elif file_string[i:i+4] == "Classical":
            bulletRapidClassical = 3
            break
        elif file_string[i:i+11] == "TimeControl \"" or file_string[i:i+12] == "Time Control \"" or file_string[i:i+12] == "Time-Control \"":
            initialTimeDigits = 0
            incrementTimeDigits = 0
            expectedTime = 0
            while True:
                if file_string[i] == "\"":
                    i = initial_i
                    break
                elif file_string[i] == "+" and (is_digit(file_string[i-1]) and is_digit(file_string[i+1])): 
                    # if both numbers are right next to the "+"
                    if is_digit(file_string[i+2]): 
                        if is_digit(file_string[i+3]): 
                            if is_digit(file_string[i+4]):
                                incrementTimeDigits = 4
                            else:
                                incrementTimeDigits = 3
                        else:
                            incrementTimeDigits = 2
                    else:
                        incrementTimeDigits = 1
                    if is_digit(file_string[i-2]):
                        if is_digit(file_string[i-3]): 
                            if is_digit(file_string[i-4]):    
                                initialTimeDigits = 4
                            else:
                                initialTimeDigits = 3
                        else:
                            initialTimeDigits = 2
                    else:
                        initialTimeDigits = 1
                    initialTime = int(file_string[i-initialTimeDigits:i]) # initial time in seconds
                    incrementTime = int(file_string[i+1:i+incrementTimeDigits+1]) # increment time in seconds
                    expectedTime = computeTimeTC(initialTime, incrementTime)
                    print("Expected time: " + str(expectedTime))
                    if expectedTime < 360:
                        bulletRapidClassical = 1
                        break
                    elif expectedTime < 540:
                        bulletRapidClassical = 2
                        break
                    else:
                        bulletRapidClassical = 3
                        break
                elif file_string[i] == "+" and (is_digit(file_string[i-2]) and is_digit(file_string[i+2])): 
                    # if both numbers are a spacebar away from the + that was expected
                    if is_digit(file_string[i+3]): 
                        if is_digit(file_string[i+4]): 
                            if is_digit(file_string[i+5]):
                                incrementTimeDigits = 4
                            else:
                                incrementTimeDigits = 3
                        else:
                            incrementTimeDigits = 2
                    else:
                        incrementTimeDigits = 1
                    if is_digit(file_string[i-3]):
                        if is_digit(file_string[i-4]): 
                            if is_digit(file_string[i-5]):    
                                initialTimeDigits = 4
                            else:
                                initialTimeDigits = 3
                        else:
                            initialTimeDigits = 2
                    else:
                        initialTimeDigits = 1
                    initialTime = int(file_string[i-initialTimeDigits:i])
                    incrementTime = int(file_string[i+1:i+incrementTimeDigits+1])
                    expectedTime = computeTimeTC(initialTime, incrementTime)
                    print("Expected time: " + str(expectedTime))
                    if expectedTime < 360:
                        bulletRapidClassical = 1
                        break
                    elif expectedTime < 540:
                        bulletRapidClassical = 2
                        break
                    else:
                        bulletRapidClassical = 3
                        break
                else:
                    i += 1  
        else:
            i += 1
    return bulletRapidClassical, i

def computeTimeTC(initialTime, incrementTime): # computes the expected time in the timecontrol.
    expectedMovesConstant = 40
    # this will assume a game length of 40 moves -- the same as human games.
    expectedTime = initialTime + incrementTime * expectedMovesConstant
    return expectedTime
    
def is_digit(string): # returns a boolean whether the string is a digit or not
    if string == '1' or string == '2' or string == '3' or string == '4' or string == '5' or string == '6' or string == '7' or string == '8' or string == '9' or string == '0':
        return True
    else:
        return False

# Reads Game Files
def I_READ(a_filename):
    filename = open(a_filename, "r")
    longest_string_in_python = filename.read()
    return longest_string_in_python

# takes in a name a_filename, and writes the writetext string in that file
def I_WRITE(a_filename, writetext): 
    filename = open(a_filename, "w+")
    print("I'm about to write this to a file: " + writetext)
    filename.write(writetext)
