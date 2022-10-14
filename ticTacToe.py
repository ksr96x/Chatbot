import random

# Ich bin hier mit absolut 0 Plan rangegangen, hab mir erstmal versucht ne Logik aufzubauen, aber mit wenig Programmiererfahrung
# finde ich das wirklich sehr schwer, weil ich nicht genau weiß, wie ich was machen kann. Das merkt man denke ich auch sehr, 
# da manches vielleicht zu einfach gedacht ist und am Ende aber zu kompliziert geschrieben ist. 
# Wusste hier zum Beispiel nie, was in die __init__ soll, weil das glaube ich nicht unbedingt klar ist, wie zB bei nem Charakter 
# (health, mana, damage etc.) 
# Workload bisher bestimmt 4+h
# Will das auch so korrekt machen, wie möglich, sprich falsche Eingaben wollte ich auch berücksichtigen und nicht ignorieren
# Hatte irgendwie Probleme mit while Schleifen, deswegen viele Checker (false, true), Notlösungen mäßig 

class Field():
    def __init__(self):
        self.matchfield = ["", 1, 2, 3, # +"\n"
                               4, 5, 6, # +"\n" funktioniert aber leider nicht    
                               7, 8, 9]

                            # Spielfeld:
                            # [1, 2, 3
                            #  4, 5, 6
                            #  7, 8, 9]
                            #[0] offen, damit leichter verständlich (1 = [1] ... 9 = [9])
                            

#Superklasse Field weil das ja Grundlage für alles ist (war jedenfalls mein Gedanke)
class PlayMechanics(Field):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.usedNumbersPlayer = []
        self.usedNumbersEnemy = []

    #Zug: Wenn der Input in der Liste vorhanden ist, soll die Stelle[number] mit X oder O ersetzt werden
    def setCharPlayer(self,number : int):
        self.checkMark = True
        for i in range(len(self.matchfield)):
            if self.matchfield[i] == number:
                if self.checkMark == True:
                    self.matchfield[i] = "X"
                else:
                    self.matchfield[i] = "O"
        
    #def checkMark(self): #zum tricksen, beim kommentieren aufgefallen, dass ich das einfach in Zeile 35 schreiben kann
        #self.checkMark : True

    def setCharEnemy(self, number : int): #Zeile 33 nur für die KI
        for i in range(len(self.matchfield)):
            if self.matchfield[i] == number:
                if self.checkMark == False:
                    self.matchfield[i] = "X"
                else:
                    self.matchfield[i] = "O"

    def checkCharsPlayer(self, numberUsedPlayer : int): #Parameter Zahl wird in eine neue Liste gepackt und dann wird immer 
        self.newNumberPlayer = None                     #geschaut, ob die schon drin ist, wenn ja, dann muss man eine neue wählen
        if numberUsedPlayer in self.usedNumbersPlayer:
            print("Please choose non used number")
            self.newNumberPlayer = True
        else:
            self.usedNumbersPlayer.append(numberUsedPlayer)
            self.newNumberPlayer = False

    def checkCharsEnemy(self, numberUsedEnemy : int): #gleiches wie Zeile 54 nur für KI
        self.newNumberEnemy = None
        if numberUsedEnemy in self.usedNumbersEnemy:
            self.newNumberEnemy = True
        else:
            self.usedNumbersEnemy.append(numberUsedEnemy)
            self.newNumberEnemy = False
            
            
        

class WinConditions(Field): 
    def __init__(self):
        super().__init__()

    def win(self):
        #Kombinationen: 1,2,3; 4,5,6; 7,8,9; 1,4,7; 2,5,8; 3,6,9; 1,5,9; 3,5,7;  
        #geht wahrscheinlich einfacher 
        #ich weiß, dass ich das ändern müsste, weil beim KI win jetzt auch win kommt, deswegen zeile 180
        if "X"==self.matchfield[1] and "X"==self.matchfield[2] and "X"==self.matchfield[3]:
            print("WIN!") 
        elif "X"==self.matchfield[4] and "X"==self.matchfield[5] and "X"==self.matchfield[6]:
            print("WIN!")  
        elif "X"==self.matchfield[7] and "X"==self.matchfield[8] and "X"==self.matchfield[9]:
            print("WIN!")
        elif "X"==self.matchfield[1] and "X"==self.matchfield[4] and "X"==self.matchfield[7]:
            print("WIN!")
        elif "X"==self.matchfield[2] and "X"==self.matchfield[5] and "X"==self.matchfield[8]:
            print("WIN!")
        elif "X"==self.matchfield[3] and "X"==self.matchfield[6] and "X"==self.matchfield[9]:
            print("WIN!")
        elif "X"==self.matchfield[1] and "X"==self.matchfield[5] and "X"==self.matchfield[9]:
            print("WIN!")
        elif "X"==self.matchfield[3] and "X"==self.matchfield[5] and "X"==self.matchfield[7]:
            print("WIN!")
        elif "O"==self.matchfield[1] and "O"==self.matchfield[2] and "O"==self.matchfield[3]:
            print("WIN!")
        elif "O"==self.matchfield[4] and "O"==self.matchfield[5] and "O"==self.matchfield[6]:
            print("WIN!")
        elif "O"==self.matchfield[7] and "O"==self.matchfield[8] and "O"==self.matchfield[9]:
            print("WIN!")
        elif "O"==self.matchfield[1] and "O"==self.matchfield[4] and "O"==self.matchfield[7]:
            print("WIN!")
        elif "O"==self.matchfield[2] and "O"==self.matchfield[5] and "O"==self.matchfield[8]:
            print("WIN!")
        elif "O"==self.matchfield[3] and "O"==self.matchfield[6] and "O"==self.matchfield[9]:
            print("WIN!")
        elif "O"==self.matchfield[1] and "O"==self.matchfield[5] and "O"==self.matchfield[9]:
            print("WIN!")
        elif "O"==self.matchfield[3] and "O"==self.matchfield[5] and "O"==self.matchfield[7]:
            print("WIN!")
       
        

    def game(self):#einfach nur ne Methode um ne while loop zu nutzen, wird bei win() auf True gesetzt, jedenfalls der Gedanke 
        self.game : False
        

player_X = PlayMechanics("X")
player_O = PlayMechanics("O")

def runMainLoop():
    while True:
        player = input("Choose X or O: ").upper()

        if player == "O":
            player = player_O
            enemy = player_X
            PlayMechanics.checkMark = False

        elif player == "X":
            player = player_X
            enemy = player_O
            PlayMechanics.checkMark = True

        else:
            raise Exception("Please enter valid symbol")
        
        gameWon = False
        while gameWon == False: #ENDLOS SCHLEIFE WEIß GOTT WARUM
            turn = input("Choose between 1 - 9: ") 
            turn = int(turn) 

            checkerPlayer = False 
            while checkerPlayer == False: #fragt leider nur 1x, d.h. 2x doppelte Zahl fragt nicht ein 2. mal
                player.checkCharsPlayer(turn)
                if player.newNumberPlayer == True: 
                    turn = input("Choose a new non used number between 1 - 9: ")    
                    turn = int(turn)
                checkerPlayer = True
             

            if turn > 0 and turn < 10:
                turn = player.setCharPlayer(turn)
                player.usedNumbersPlayer.append(turn)
                print("Your turn: ")  
                print(player.matchfield[1:]) #[0] wird übersprungen, da ja eh nur ""
                if WinConditions.win(player): 
                   gameWon = True
                    
          
            enemyTurn = random.choice(enemy.matchfield)
            
            #checkerEnemy = False
            #while checkerEnemy == False: #ENDLOS SCHLEIFE, soll doppelte Werte vermeiden, klappt nicht
            #    enemy.checkCharsEnemy(enemyTurn)
            #    if enemy.newNumberEnemy == True: 
            #        enemyTurn = random.choice(enemy.matchfield)
            #    checkerPlayer = True


            enemyTurn = enemy.setCharEnemy(enemyTurn)
            #enemy.usedNumbersEnemy.append(enemyTurn)#wird nur gebraucht wenn Z. 167 geht 
            print("Enemy turn: ")
            print(enemy.matchfield[1:])#[0] wird übersprungen, da ja eh nur ""
            if WinConditions.win(enemy):
                gameWon = True
                print("(Enemy win)")
                                           
        break

runMainLoop()

# Was nicht funktioniert: - Spielfeld Optik (Zeile 14)
#                         - Mehrfach Nachfrage wenn gleiche Zahl (Zeile 147)
#                         - KI mehrfach Try wenn selbe Zahl(Zeile 167)
#                         - Endlos Schleife Spiel (Zeile 142)