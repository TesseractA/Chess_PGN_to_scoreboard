# Writing functions

# After read and translate is finished, take output
# from translate and write it into a file that can be
# stored as text
def interpret(file_string): 
    i = 0 # index
    numberOfEngineGames = 0
    engineNameList = []
    engineName = ""
    engineIndexWhite = 0 # used for identifying the index of an engine in engineNameList
    engineIndexBlack = 0
    while i < len(file_string):
        if file_string[i, i+7] == "White \"" or file_string[i, i+7] == "Black \"":
            # go 7 characters forward to skip 'White "'
            i += 7
            engineName = read_engineName(file_string, engineNameList, i)
            engineNameList = check_engineName(engineName, engineNameList)
             = i,  = detect_score(file_string, i)
        ++i
    i = 0
    while i < len(file_string):
        if n == file_string[i:i+engineNameLength]:  
            for n in engineNameList:
                engineNameLength = len(n)
    
    
        
def read_engineName(file_string, engineName, index):
    engineNameLength = 0
    while file_string[index] != "\"":
        engineNameLength += 1
    engineName = file_string[index, index+engineNameLength]
    return engineName
def check_engineName(engineName, engineNameList):
    icheck = 0 # engine name index
    engineNameList_length = len(engineNameList)
    isRecordedAlready = False
    while icheck <= engineNameList_length:
        if icheck == engineNameList_length:
            engineNameList += engineName
            # if the engine's name wasn't detected in the list already
        elif engineName == engineNameList[icheck]:
            isRecordedAlready = True
            break
    return engineNameList, isRecordedAlready
def detect_engineIndex(engineNameList, engineName):
    index = 0
    while True:
        if engineName == engineNameList:
            
        else:
            index++
            
            
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