# Writing functions

# After read and translate is finished, take output
# from translate and write it into a file that can be
# stored as text
def interpret(file_string): 
    i = 0 # index
    numberOfGamesTable = []
    # colorCrossTable = [] which can be used for wins for scoring wins as black or white heavier if the feature is wanted
    trueCrossTable = [] # it's a real crosstable!
    engineNameList = []
    engineName = ""
    engineIndexWhite = 0 # used for identifying the index of an engine in engineNameList
    engineIndexBlack = 0
    score = 0
    engineScores = []
    while i < len(file_string):
        if file_string[i:i+7] == "White \"":
            # go 7 characters forward to skip 'White "'
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = check_engineName(engineName, engineNameList)
            engineIndexWhite = detect_engineIndex(engineNameList, engineName)
        elif file_string[i:i+7] == "Black \"":
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = check_engineName(engineName, engineNameList)
            engineIndexBlack = detect_engineIndex(engineNameList, engineName)
            score = detect_score(file_string, i)
            # colorCrossTable[engineIndexWhite][engineIndexBlack] += score for intentionally for as white/black winrates
            trueCrossTable[engineIndexWhite][engineIndexBlack] += score
            trueCrossTable[engineIndexBlack][engineIndexWhite] += 1-score
            score = 0
        ++i
    i = 0
    
        
def read_engineName(file_string, engineName, index):
    engineNameLength = 0
    while file_string[index] != "\"":
        engineNameLength += 1
    engineName = file_string[index, index+engineNameLength]
    return engineName
def check_engineName(engineName, engineNameList):
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
    return index, score


def crosstableVisual(trueCrossTable, numberOfGamesCrosstable):
    # this will create a visual representation
    nice = 1
def detectBulletRapidClassical(file_string):
    i = 0
    while i < len(file_string):
        nice = 1


def I_READ(a_filename):
    filename = open(a_filename, "r")
    longest_string_in_python = filename.read()
    return longest_string_in_python

def I_WRITE(a_filename):
    filename = open("a_filename.txt", "w+")
    longest_string_in_python = filename.write()
    
