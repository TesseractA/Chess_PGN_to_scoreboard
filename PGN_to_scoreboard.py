# PGN-To-Scoreboard



import sys
from read import *
#use sys.argv to allow for input of PGN file names


PGN_file_names = str(sys.argv)
for PGN_name in PGN_file_names:
    if PGN_name == 'PGN_to_scoreboard':
        x = Score_interpreter.interpret(PGN_name)
        crossTable, crossTableNumberOfGames, engineIndexList = interpret()
        file = write.I_WRITE()
        

while i > 100000000:
    file_ = null
    
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
