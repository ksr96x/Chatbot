import random

# Ich bin hier mit absolut 0 Plan rangegangen, hab mir erstmal versucht ne Logik aufzubauen, aber mit wenig Programmiererfahrung
# finde ich das wirklich sehr schwer, weil ich nicht genau weiß, wie ich was machen kann. Das merkt man denke ich auch sehr, 
# da manches vielleicht zu einfach gedacht ist. Wusste hier zum Beispiel nie, was in die __init__ soll, weil das glaube ich
# nicht unbedingt klar ist, wie zB bei nem Charakter (health, mana, damage etc.) Workload bisher bestimmt 4+ h

class Field():
    def __init__(self):
        self.matchfield = ["", 1, 2, 3, 
                               4, 5, 6,     
                               7, 8, 9]

                            # Spielfeld:
                            # [1, 2, 3
                            #  4, 5, 6
                            #  7, 8, 9]
                            #[0] offen, damit leichter verständlich (1 = [1] ... 9 = [9])
                            #wird nur nicht so ausgegeben wie gewünscht :/

    def get_matchfield(self):
        return self.matchfield

#Superklasse Field weil das ja Grundlage für alles ist (war jedenfalls mein Gedanke)
class PlayMechanics(Field):
    def __init__(self, player):
        super().__init__()
        self.player = player
         
    def printSymbol(self):
        if self.player == "X":
            return ["X"]
        else:
            return ["O"]

        
        
    #Zug: Wenn der Input in der Liste vorhanden ist, soll die Stelle[number] mit X oder O ersetzt werden
    def setChar(self, number : int):
        
        for i in range(len(self.matchfield)):
            if self.matchfield[i] == number:
                if player_X:
                    self.matchfield[i] = "X"
                else:
                    self.matchfield[i] = "O"
        

class WinConditions(Field): #keine Ahnung was da zusätzlich initialisiert werden soll 
    def __init__(self):
        super().__init__()

    def win(self):
        #Kombinationen: 1,2,3; 4,5,6; 7,8,9; 1,4,7; 2,5,8; 3,6,9; 1,5,9; 3,5,7;  
        #geht wahrscheinlich einfacher 
        #ich weiß, dass ich das ändern müsste, weil beim KI win jetzt auch win kommt, deswegen zeile 127
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
        

    def gameWonFalse(self):#einfach nur ne Methode um ne while loop zu nutzen, wird bei win() auf True gesetzt 
        self.gameWonFalse : bool = False

player_X = PlayMechanics("X")
player_O = PlayMechanics("O")

def runMainLoop():
    while True:
        player = input("Choose X or O: ").upper()

        if player == "O":
            player = player_O
            enemy = player_X
        elif player == "X":
            player = player_X
            enemy = player_O
        else:
            raise Exception("Please enter valid symbol")
        
        while WinConditions.gameWonFalse:
            turn = input("Choose between 1 - 9: ") #würde hier gerne turn.isdigit() implementieren, aber spuckt folgendes aus:
            turn = int(turn)                       #ModuleNotFoundError: No module named '_curses', nachdem etwas automatisch importiert wird
            if turn > 0 and turn < 10:
                turn = player.setChar(turn)
                print("Your turn: ")  
                print(player.matchfield) 
                if WinConditions.win(player): #wenn win() eintritt, gameWonFalse == True, somit soll die while loop enden, klappt aber glaube ich noch nicht
                    WinConditions.gameWonFalse = True

                enemyTurn = random.choice(enemy.matchfield) #eine Art KI die dann random einfach irgendwo das Gegenteilige Symbol setzt
                enemyTurn = enemy.setChar(enemyTurn)
                print("Enemy turn: ")
                print(enemy.matchfield)
                if WinConditions.win(enemy):
                    WinConditions.gameWonFalse = True
                    print("(Enemy win)")

            else:
                raise Exception("Enter valid number")       
        break

runMainLoop()

