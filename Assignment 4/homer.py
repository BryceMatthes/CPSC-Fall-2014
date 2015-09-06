# Your name: Bryce Matthes  
# Student ID: 10147880
# Tutorial #: T07
# Version: 0.1
# LC: 405
'''
This program is the simpsons game, started off Tam's source.

Starts by displaying introText() to explain the game
Loads the game board fromt the file specified
Homer can move in 4 directions or stand in place
EPA agents can move in 8 directions or stand in place

Game should meet everything in the spec, Debugging is a little less thorough than other code I have retained

uses: Enhanced version: Homer has to spend a total of 10 successive turns in Alaska before he freezes. 
If he leaves and re-enters Alaska then the count down will start again at the beginning (he has 10 turns before he freezes).

'''

ROWS	  = 20
COLUMNS = 30
AGENTS = 6
aMazeSave = []
import random

# Game states
BUILDING      = "#"
EMPTY         = " "
EPA_AGENT     = "E"
HOMER         = "H"
SPRINGFIELD   = "S"
WATER         = "~"
START_ROW = 1
START_COLUMN = 1

def introText():
  '''
  Displays intro text
  '''
  print('')
  print('     /X \\')
  print('   _------_')
  print('  /        \\')
  print(' |          |')
  print(' |          |')
  print(" |     __  __)\t\t Welcome to my 'The Simpsons Movie' © Fox game!")
  print(' |    /  \/  \\\t\tHelp guide Homer back to SpringField while avoiding the EPA')
  print('/\/\ (o   )o  )\t\t----------------------------------------')
  print('/c    \__/ --.\t\t Move with 8(UP) 2(Down) 4(Left) 6(Right) and 5(Stay in place)')
  print("\_   _-------'\t\t There is a 25"+'%' +" chance Homer won't listen to your move command")
  print(" |  /         \\\t\tHomer can't go in water ('~' he'll drown) or go through walls ('#')")
  print(" | | '\_______)\t\tEPA Agents ('E') catch Homer if he is within one space(any direction)")
  print(' |  \_____)\t\t    Please Load a map file to get started!')
  print(' |_____ |')
  print('|_____/\/\\')
  print('/        \ ')

def rngRolls():
  '''
  Rolls from -1 to 1 to choose the new agent location
  '''
  rngX = random.randrange(-1,2,1)
  rngY = random.randrange(-1,2,1)
  return rngX,rngY

def moveAgents(aMaze,posAgents):
  '''
  moves all of the EPA agents and ensures that they can't break the rules of the game
  '''
  counterMax = (len(posAgents))
  waterError = False # Water Error is used for all errors ie: walls, water, stepping on Homer and the SpringField S
  counter = 0
  while counter < counterMax:
    holderRow = int(posAgents[counter][0])
    stringCol = str(posAgents[counter][1]).strip('[]') # This is used to correct an issue with two or more agents on one line
    if ',' in stringCol:
      stringCol = stringCol.replace(chr(44),'')
      colList = stringCol.split()
      for a in range (0,len(colList),1):
        holderCol = int(colList[a])
        roll1,roll2 = rngRolls()
        if (aMazeSave[holderRow+roll1][holderCol+roll2] != ('#' or '~' or 'S')) and (aMaze[holderRow+roll1][holderCol+roll2] != ('E' or 'S' or '~' or 'S')):
          if(aMazeSave[holderRow+roll1][holderCol+roll2] == "~"):
            waterError = True
          if(aMazeSave[holderRow+roll1][holderCol+roll2] == "S"):
            waterError = True
          if(aMaze[holderRow+roll1][holderCol+roll2] == "H"):
            waterError = True    
          if waterError == True:
            pass
          else:
            if debug == True:
              print("<<< Moving Agent ["+str(counter)+"] to ["+str(holderRow+roll1)+", "+str(holderCol+roll2)+"] >>>")  # Debug          
            aMaze[holderRow+roll1][holderCol+roll2] = 'E'
            aMaze[holderRow][holderCol] = ' '

    else:    
      holderCol = int(str(posAgents[counter][1]).strip('[]'))
      roll1,roll2 = rngRolls()
      if (aMazeSave[holderRow+roll1][holderCol+roll2] != ('#' or '~' or 'S')) and (aMaze[holderRow+roll1][holderCol+roll2] != ('E' or 'S' or '~' or 'S')):        
        if(aMazeSave[holderRow+roll1][holderCol+roll2] == "~"):
          waterError = True
        if(aMazeSave[holderRow+roll1][holderCol+roll2] == "S"):
            waterError = True
        if(aMaze[holderRow+roll1][holderCol+roll2] == "H"):
            waterError = True      
        if waterError == True:
          pass
        else:
          if debug == True:
            print("<<< Moving Agent ["+str(counter)+"] to ["+str(holderRow+roll1)+", "+str(holderCol+roll2)+"] >>>") # Debug
          aMaze[holderRow+roll1][holderCol+roll2] = 'E'
          aMaze[holderRow][holderCol] = ' '
    counter = counter + 1  
  return aMaze

def movementHandler(aMaze,a,hLocation):
  '''
  Manages the movement of the player through moveH and error checks him.
  '''
  global amzeSave
  wonGame = False
  aMaze,a,hLocation,gameOver,choice,skipTurn = moveH(a,aMaze,hLocation)
  if gameOver == True:
    pass
  else:
    if ((int(choice) == 8) and (aMazeSave[a][hLocation] == '~')): ##Moved up
      print("Homer Drowned to Death!")
      gameOver = True
    if ((int(choice) == 4) and (aMazeSave[a][hLocation] == '~')): ##Moved left
      print("Homer Drowned to Death!")
      gameOver = True
    if ((int(choice) == 6) and (aMazeSave[a][hLocation] == '~')): ##Moved right
      print("Homer Drowned to Death!")  
      gameOver = True
    if ((int(choice) == 2) and (aMazeSave[a][hLocation] == '~')): ##Moved down
      print("Homer Drowned to Death!")  
      gameOver = True
    if ((int(choice) == 8) and (aMazeSave[a][hLocation] == '#')): ##Moved up
      print("Ran into a wall.")
      aMaze[a+1][hLocation] = 'H'
      aMaze[a][hLocation] = '#'
    if ((int(choice) == 4) and (aMazeSave[a][hLocation] == '#')): ##Moved left
      print("Ran into a wall.")
      aMaze[a][hLocation+1] = 'H'
      aMaze[a][hLocation] = '#'
    if ((int(choice) == 6) and (aMazeSave[a][hLocation] == '#')): ##Moved right
      print("Ran into a wall.")
      aMaze[a][hLocation-1] = 'H'
      aMaze[a][hLocation] = '#'
    if ((int(choice) == 2) and (aMazeSave[a][hLocation] == '#')): ##Moved down
      print("Ran into a wall.")
      aMaze[a-1][hLocation] = 'H'
      aMaze[a][hLocation] = '#'
    if ((aMazeSave[a][hLocation] == 'S')): ##Moved down
      print("You got Homer Back to SpringField! ")
      wonGame = True
  posAgents = findAllAgents(aMaze)
  if skipTurn == False: # So agents don't move when Homer enter a value > 9
    aMaze = moveAgents(aMaze,posAgents)        
  return aMaze,a,hLocation,gameOver,choice,wonGame,posAgents,skipTurn    

def findAllAgents(aMaze):
  '''
  puts all agents locations into a list
  '''
  a = 0
  n = 0
  posAgents = []
  occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
  while a < 20:
    if str(list(occurrences('E', aMaze[a]))) != '[]':
      posAgents.append ([])
    a = a + 1
  a = 0  
  while a < 20:
    if str(list(occurrences('E', aMaze[a]))) != '[]':
      posAgents [n] = [a,list(occurrences('E', aMaze[a]))]
      n = n + 1
    a = a + 1 
  return posAgents     

def getArgs():
  '''
  get input file from user input
  '''
  counter = 1
  fileName = input("Enter File Name: ")
  return fileName

def agentLocation(aMaze):
  for a in range (0,30,1):
    if 'E' in aMaze[a]:
      hLocation = aMaze[a].index['E']
      print(str(a) +" " +str(hLocation))
      break

def displayWorld(aMaze, articTime, currentRow):
     # Author: James Tam
     # function: displayWorld
     # displayWorld(2Dlist,int,int,int)
     # returns(nothing)
     # Shows the current state of the world (location of Homer, the EPA agents)
     '''
     Re-Draws the game board
     '''
     print()
     print("Turns in Alaska (Top 6 Rows): " +str(articTime))        
     for r in range (0, ROWS, 1):
          for c in range (0, COLUMNS, 1):
               print(aMaze[r][c], end="")
          print()

def checkAgents(aMaze,row,hLocation,gameOver,wonGame):
  '''
  Uses to check is Homer has been caught by an agent and ends the game.
  '''
  global debug
  if wonGame == True:
    pass
  else:  
    if (aMaze[row-1][hLocation] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row+1][hLocation] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row][hLocation-1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row][hLocation+1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row+1][hLocation+1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row-1][hLocation+1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row+1][hLocation-1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True
    elif (aMaze[row-1][hLocation-1] == 'E'):
      print("Homer was caught by and EPA agent, game over.")
      gameOver = True                
  return gameOver               

def moveH(a,aMaze,hLocation):
  '''
  Draws the compass for movement and takes input, error checks for input values
  '''
  global debug
  skipTurn = False
  rng = random.randrange(1,5,1)
  global debug
  gameOver = False ##Works Left and Right
  print("Movement Options, the numbers correspond to the 4 compass \n\
    directions (5 to not move). Or enter 0 to quit the game.")
  print("  8  ")
  print("4 5 6 ")
  print("  2  ")
  choice = input("Choice: ")
  moves = "4 5 6 8 2 0"
  if debug == True:
    print("<<< Random Number (1-4): " +str(rng) +" >>>")
    print("<<< if the number is one: Homer is distracted, else: follows instructions >>>")
  if int(choice) < 0:
    if debug == True:
      debug = False
    else:  
      debug = True
  if int(choice) == 4:
    if rng == 1:
      print("Homer becomes distracted and refuses to move")
    else: 
      hLocation = hLocation - 1
      aMaze[a][hLocation] = "H"
      aMaze[a][hLocation+1] = " "
  if int(choice) == 6:
    if rng == 1:
      print("Homer becomes distracted and refuses to move")
    else: 
      hLocation = hLocation + 1
      aMaze[a][hLocation] = "H"
      aMaze[a][hLocation-1] = " "
  if int(choice) == 8:
    if rng == 1:
      print("Homer becomes distracted and refuses to move")
    else:
      a = a - 1
      aMaze[a][hLocation] = "H"
      aMaze[a+1][hLocation] = " "
  if int(choice) == 2:
    if rng == 1:
      print("Homer becomes distracted and refuses to move")
    else:
      a = a + 1
      aMaze[a][hLocation] = "H"
      aMaze[a-1][hLocation] = " "
  if int(choice) == 5:
    pass
  if int(choice) == 0:
    print('You quit the game! Thanks for playing!')
    gameOver = True
  if not(choice in moves) and int(choice) <= 9:
    print("Homer doesn't know how to move that way.")
  if not(choice in moves) and int(choice) > 9:
    print("Movement Command Error: Turn Skipped for EPA and Homer")
    skipTurn = True                
  return aMaze,a,hLocation,gameOver,choice,skipTurn

def initializeHC():
   # Author: James Tam
   # function: initializeHC (hard-coded initialization)
   # initializeHC(none)
   # returns(2DList)

   # The legacy method of initializing the game world. It's retained so students can see
   # an alternative (non-file IO) method of initialization.
   '''
   Generates the game board with the file in getArgs()
   '''
   global aMazeSave
   aMaze = []
   agentLocation = []

   # Create the grid. Initialize elements to a space.
   for r in range (0, ROWS, 1):
        aMaze.append ([])
        aMazeSave.append ([])
        for c in range (0, COLUMNS, 1):
             aMaze[r].append (" ")
             aMazeSave[r].append (" ")

   inputFileN = getArgs()          
   a = 0
   inputFile=open(inputFileN,"r")
   for line in inputFile:
    aMazeSave [a] = list(line)
    aMaze [a] = list(line)
    a = a + 1
   return(aMaze,agentLocation)

def start():
     '''
     The main funciton, keeps track of the time in Alaska and running the other functions.

     Note: Some of the variables here can probably be removed, but I don't want to mess anything up.
     '''
     global debug
     global aMazeSave
     aMaze = []
     a = 0
     gameOver = False
     introText() ## Intro Text
     agentLocation = []
     articTime = 0
     aChecker = 0
     currentRow = START_ROW
     currentColumn = START_COLUMN
     newRow = START_ROW
     newColumn = START_COLUMN
     direction = 0
     i = 0
     aMaze,agentLocation = initializeHC()
     displayWorld(aMaze,articTime,currentRow)
     while articTime < 11 and gameOver == False:
      for a in range (0,30,1):
        if 'H' in aMaze[a]:
          if gameOver == True:
            pass
          else:  
            hLocation = aMaze[a].index('H')
            aMaze,a,hLocation,gameOver,choice,wonGame,posAgents,skipTurn = movementHandler(aMaze,a,hLocation)
            if gameOver == True:
              displayWorld(aMaze,articTime,currentRow)
            else:  
              displayWorld(aMaze,articTime,currentRow)
              gameOver = checkAgents(aMaze,a,hLocation,gameOver,wonGame)
              if gameOver == True:  
                stringGA = "True"
              else:
                stringGA = "False"
              if debug == True:
                print("<<< Homer Position: " +"Row " +str(a) +":[" +str(hLocation) +"]" +" >>>")
                print("<<< Old Agent Positions: ", end=" ")
                print(posAgents, end=" ") 
                print(">>>")
                print("<<< Game Over: " +stringGA +" >>>")
              if wonGame == True:
                gameOver = True
              if (int(a) < 7) and skipTurn == False:
                print("Turn Spent in Alaska")  
                articTime = articTime + 1
                if articTime == 11:
                  print("Game Over: Homer Froze from being in Alaska too long")
              elif(skipTurn != True):
                if articTime != 0:
                  print('You left Alaska, Timer Reset!') 
                articTime = 0      
          break

debug = False
start()