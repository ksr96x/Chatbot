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
                                                        #geschaut, ob die schon drin ist, wenn ja, dann muss man eine neue wählen
        if numberUsedPlayer > 0 and numberUsedPlayer < 10 and numberUsedPlayer not in self.usedNumbersPlayer:
            return self.usedNumbersPlayer.append(numberUsedPlayer)
        else:
            return False

    def checkCharsEnemy(self, numberUsedEnemy : int): #gleiches wie Zeile 54 nur für KI
          if numberUsedEnemy > 0 and numberUsedEnemy < 10 and numberUsedEnemy not in self.usedNumbersEnemy:
            self.usedNumbersEnemy.append(numberUsedEnemy)
            return True
          else:
                return False
            
    # Diese 3 Methoden über dir kann ich nicht einfach mal umschreiben. Dafür muss ich sehr weit ausholen.
    # https://press.rebus.community/programmingfundamentals/chapter/scope/ Bitte ließ dir das einmal durch. Und dann schreibe die 2 Methoden einmal um.
    # Danach folgendes: https://realpython.com/python-return-statement/#:~:text=The%20Python%20return%20statement%20is%20a%20special%20statement%20that%20you,can%20be%20any%20Python%20object.
    # Deine Methoden sind wie gemacht um am Ende etwas zu returnen! Du kannst auch deine globale Variable numberUsedEnemy behalten und trotzdem etwas returnen.
    # Ich finde das aber zu kompliziert. Was hast du davon, dass du weißt wer welche Nummern belegt hat? Was du brauchst ist: Welche Nummern sind belegt? Welche Nummern nicht? Der Rest ist doch egal.
    # Danach gibst du zurück ob die Zahl erlaubt ist oder nicht. In meinen Augen kannst du beide Methoden in einer Methode abhandelt. 
    # Wie ich es angehen würde:
    #   1. Schreibe eine Methode, die die neue Zahl als Übergabeparameter hat.
    #   2. Prüfe in der Methode ob die eingegebene Zahl korrekt ist. 
    #       3. Falls Ja setzte das Zeichen in der Liste.
    #       4. Falls Nein returne False
    #   5. Mit dem True oder False wird dann in deiner Whileschleife weiter gearbeitet.

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
       
       # Wie schon gesagt, das kannst du mindestens halbieren! Bzw. mehr als halbieren fällt mir auch nicht ein. @Leonard
        
    def game(self):#einfach nur ne Methode um ne while loop zu nutzen, wird bei win() auf True gesetzt, jedenfalls der Gedanke 
        self.game : False # Ich verstehe nicht warum du das brauchst. Warum kannst du die variable nicht im Konstruktor auf True setzen? @Leonard
        

player_X = PlayMechanics("X")
player_O = PlayMechanics("O")

def runMainLoop():
    while gameWon == False:
        #while True:
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
            turn = int(turn) # Das darfst du so eigentlich auch nicht... Was passiert wenn jemand einen Buchstaben eingibt? Macht den Code komplizierter aber fängt auch Fehler ab. 
                             # Wie man das abfangen kann erkläre ich dir, wenn das Program fertig ist und es dich interessiert. 

             
            while player.checkCharsPlayer == False: #fragt leider nur 1x, d.h. 2x doppelte Zahl fragt nicht ein 2. mal
                player.checkCharsPlayer(turn)
                if player.checkCharsPlayer == False: 
                    turn = input("Choose a new non used number between 1 - 9: ")    
                    turn = int(turn)
                

            # Also diese While-Schleife ist natürlich etwas wild haha. Aber nicht schlimm. Das wird noch.
            # 1. Du musst deine Schleife anders verschachteln.
            # while gameWon == False:
            #   while True:
            #       turn = input("Choose between 1 - 9: ")
            # (bool)allowedNumber = player.checkCharsPlayer(turn) Also: Du willst eine Methode, die dir sagt ob die Zahl erlaubt ist oder nicht. Und falls ja gibt diese True zurück und 
            #                                                      falls Nein False. Jetzt in der Klasse extra eine globale Variable anzulegen macht keinen Sinn.
            # if allowedNumber == True:
            #    macheWasGemachtWerdenSoll()
            #    break 


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
                gameWon = True      # Du setzt diese Variable nur hier. Also hast du eine Endlosschleife außer du kommst hier rein. Jeder der Code Pfade muss also am Ende ein gameWon = True haben
                print("(Enemy win)")# Außer du willst expliziet dass es weiter geht.
                                           
        break

runMainLoop()

# Was nicht funktioniert: 1 Spielfeld Optik (Zeile 14)
#                         2 Mehrfach Nachfrage wenn gleiche Zahl (Zeile 147)
#                         3 KI mehrfach Try wenn selbe Zahl(Zeile 167)
#                         4 Endlos Schleife Spiel (Zeile 142)

# @Leonard 2. 



# @Leonard 3. Ich würde an deiner Stelle eine Methode schreiben, die einen Randomwert aus einer gewissen Menge wählt. Ungefähr so:
# def getRandomPlacment(self, freePlaces):
#   randomNumber = generiere random Number von 0 bis länge freePlaces
#   return freePlaces[randomNumber]

# Dann musst du dir nur davor überlegen wie du an die freien Stellen kommst. Ich hoffe du konntest mir folgen. Das bekommst du auf jeden Fall hin.

# 1. Habe ich im anderen Dokument ja schon erklärt.  
# Du kannst das mit dem Array 1 = [1] so machen. Ich würde es nicht so machen, sondern mich einfach direkt daran gewöhnen, dass es mit 0 anfängt. 
        # Aber das bleibt dir überlassen
        # Also: Wenn du das über ein Array machen möchtest, dann kannst du ein 2 dimensionales Array verwenden.
        # matchfield = [[1,2,3]
        #               [4,5,6]
        #               [7,8,9]]
        # Das würde dann auch so ausgegeben werden. Das kann man so machen, muss man aber nicht.
        #
        # Andernfalls kannst du dir eine Methode schreiben, die dir ein eindimensionales Array schöner ausgibt.
        # for index in range(0,3):
        #   print(f"[{macthfield[0 + index]}][{macthfield[1 + index]}][{macthfield[2 + index]}]")
        # Die sollte funktionieren. Hab sie jetzt nicht getestet.

# Das war wieder sehr viel Input. Aber das wird! Glaub mir. Ich würde an deiner Stelle eine neue Datei nehmen und in dieser nur 1!! Klasse anlegen. Oder auch 2. 
# Danach schaust du deine Methode an und schaust meine Kommentare an. Und aus dieser Kombi schreibst du ein geiles neues Program. Du kannst mir gerne auch einzelne Methoden schicken. Oder 
# kleinere Fragen stellen. 

# Wenn ich das Programm nicht selber schreibe fällt es mir sehr schwer dir Tipps zu geben. Weil wenn ich eine Methode so ändere wie ich sie für richtig halte funktioniert der Rest nicht mehr :D
# Arbeite auf jeden Fall mit return! Arbeite weniger mit self.variable. Also einer Klassenvariable. Und verkünztel dich nicht! Wenig Klassen und immer nach Logik aufteilen. Die Wincondition ist Teil
# des Spiels. Also passt es in die Spielfeld Klasse!