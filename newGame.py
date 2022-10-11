from random import *

# Ich verstehe was du hier machen wolltest. Aber ich würde das ganze anders machen. Eine Klasse Item, sollte ein Item beschreiben und alles was das Item kann. Ich finde ein Item 
# sollte nicht mit dem Player interagieren. Sondern der Player mit dem Item. Hier kommt jetzt vererbung ins Spiel. Das ist erst mal kompliziert, aber eigentlich recht einfach. 
# Bei dir macht es einfach Sinn, verschiedene Waffenklassen zu haben. Solltest du das Spiel erweitern, könnte es recht schnell nervig werden, wenn du immer Objekte erzeugst, die aber 
# am Ende 10 leere Paramter annehmen. z.B. Zauberstab(50,60,40,0,0,0,0,0). Das ist kompliziert und recht schnell sehr schwer zu verstehen. 

class Item():
    def __init__(self, bonusDamage : int, bonusHealth : int, bonusMana : int):
        self.itemName : str
        self.damage = bonusDamage
        self.mana = bonusMana
        self.health = bonusHealth

    #Beispiel Methode, was in dieser Klasse per Methode passieren könnte. 
    def changeItemNameTag(self, newName : str):
        self.itemName = newName

#Diese Klasse kann alles was die Klasse Item kann.
class Weapon(Item):
    def __init__(self, bonusDamage, bonusHealth, bonusMana):
        super().__init__(bonusDamage, bonusHealth, bonusMana) # Wir erben den Konstruktor aus Item aus Zeile 9.

#Diese Klasse kann alles was die Klasse Item kann und noch viel mehr.
class Clothing(Item):
    def __init__(self, bonusDamage, bonusHealth, bonusMana, bonusArmor, bonusMr):
        super().__init__(bonusDamage, bonusHealth, bonusMana) # Hier das gleiche. Aber hier erweitern wir den Konstruktur um 2 weitere Werte.
        self.bonusArmor = bonusArmor
        self.bonusMr = bonusMr

# Ich weiß, der Abschnitt oben wirkt sehr verstöhrend. Zumindestens ist er für mich noch verstöhrend. Aber ich finde Vererbung äußerst wichtig und vor allem ist es für dein Spiel
# sehr passend. Für deinen leichten Usecase ist es mehr Arbeit als Nutzen. Aber erweitere dein Spiel um 5 Waffen, wie zum Beispiel Nahkampf und Fernkampfwaffen und du schreibst 5 mal
# das gleiche, obwohl du dir durch Vererbung einiges sparen kannst. Das gleiche gilt für die Character class. Eigentlich willst du eine Character class, von der dann Ork und Zauberer erben.
# Zumindestens hast du es jetzt einmal gesehen, nutzen musst du es momentan noch nicht.

# Python hat von Haus aus keine angezeigt Typisierung. Manchmal kann es aber Sinnvoll sein, wenn VS-Code einem automatisch Methoden aufgrund des Types vorschlägt. Außerdem hilft es 
# dir bei größeren Projekten, wenn du über die Methode hoverst und sehen kannst, welchen Typ du übergeben musst. Durch damage : int weiß vs-code welchen Typ du gerne nutzen würdest. 

class Character():
    def __init__(self, damage : int, armor : int, mr : int):
        self.health = 100
        self.mana = 200
        self.damage = damage
        self.armor = armor
        self.mr = mr

    # Das ist jetzt ein bisschen schwer zu erklären. 
    # Ich finde, wenn die Klasse Character heißt, dann kann sie nur Charakter Methoden enthalten. Eine Methode die sowohl den Player, als auch das Target abarbeitet,
    # wiederspricht dem Ziel der Klasse. z.B. ork = Charakter(x,y,z,k). Dann kann diese Klasse mit ork.attack(target) das target angreifen. Das ist in sich logischer. Oder du musst eine 
    # neue Klasse schreiben, die das Spiel handelt und die Methode attack dort hinein legen. Versuche immer beim Programmieren, dass eine Klasse nur eine
    # Aufgabe hat und so stark wie möglich von anderem gekappselt ist. 
    # https://www.inztitut.de/blog/glossar/generalisierung/ Ich denke, dieser Artikel ist etwas zu früh für dich und passt auch nicht exakt auf unser Beispiel,
    # aber dann hast du wenigstens schon einmal gehört und weißt, dass es so etwas gibt.

    #weak attack oder default attack
    def attack(self, target, attackType):
        critChance = randint(1, 10)
        if attackType == "default":
            manaUsage = randint(25, 30)
            method = self.__calculateAttackDamageDefault
            # ^ In Python sind Methoden auch Objekte. So kann ich eine Methode als Argument übergeben und diese später aufrufen. Das muss man so aber nicht machen!
            # | https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
            self.__attack(target, critChance, manaUsage, method, critValue = 200, noCritValue = 100)

        elif attackType == "weak":
            manaUsage = randint(20, 30)
            method = self.__calculateAttackDamageWeak
            self.__attack(target, critChance, manaUsage, method , critValue = 2, noCritValue = 5)

        else:
            raise Exception("Unknown attack type") #Bei if und elif abfolgen sollte am Ende immer eine Exception oder ein else stehen. Je nach dem ob es einen Default
                                                    #gibt oder nicht.

    # __attack() == private attack()
    def __attack(self, target, critChance : int, manaUsage : int, method, critValue, noCritValue):
        # Ich bin wirklich immer zu faul mir variablen Namen auszudenken. Aber glaub mir, es spart dir später viel Zeit und der Code wird auch für andere leichter lesbar.
        # Ich musste mich in deinem Code erst einmal umschauen, wo x überhaupt genutzt wird. Aber durch eine sprechende variablen Bennenung wird alles leichter.
        if critChance < 10:
                if target.armor > target.mr:
                    #attackDamage = self.calculateAttackDamage(target.armor, 100)
                    attackDamage = method(target.armor, noCritValue)
                else:
                    #Beide else if fallen weg, da du genau das gleiche machst.
                    #attackDamage = self.calculateAttackDamage(target.mr, 100)
                    attackDamage = method(target.mr, noCritValue)
                self.mana -= manaUsage
        else:
            print("CRITICAL HIT")
            #attackDamage = self.calculateAttackDamage(target.armor, 200)
            attackDamage = method(target.armor, critValue)
            self.mana -= 50

        target.health -= attackDamage
        print("Current Damage: "+str(attackDamage))
        print("Mana Left: ", self.mana) #Ob man hier print("Mana Left:", self.mana) oder print("Mana left:"+str(self.mana)) nutzt, kann ich dir nicht sagen. Mach was du lieber hast.

    # def calculateAttackDamage() -> int. Auch das ist Typisierung. Ich sage VSCode, ich returne am Ende einen integer. Hilft bei großen Projekten. Mach am besten -> int weg und 
    # hover über die Methode. Dann schreibe es wieder hin und schaue dir den Unterschied an.
    def __calculateAttackDamageDefault(self, enemyValue : int, multiplicator : int) -> int:
        # 1. attackDmgAd = (attacker.damage / enemy.armor)*100
        # 2. attackDmgAp = (attacker.damage / enemy.mr)*100
        # 3. attackDmgBoth = (attacker.damage / enemy.mr)*100

        # 2 und 3 sind die gleiche Rechnung. Bei 1 ist nur ein Wert anders. Versuche solche Ähnlichkeiten zu finden und dann in einer Methode zu vereinen. Weniger Code == einfacher und 
        # leichter zu warten.
        return (self.damage / enemyValue) * multiplicator

    def __calculateAttackDamageWeak(self, enemyValue : int, divisor : int) -> int:
        return (self.damage / enemyValue) * self.mana / divisor
    
    def setWeapon(self, weapon : Weapon):
        self.damage += weapon.damage

        self.mana += weapon.mana

        self.health += weapon.health
    
    def setClothing(self, clothing: Clothing):

        self.armor += clothing.bonusArmor

        self.mr += clothing.bonusMr

        self.damage += clothing.damage

        self.mana += clothing.mana

        self.health += clothing.health

        # Das sollst du hier nicht verwenden! Es soll dir nur zeigen, dass Methoden aus der Elternklasse auch genutzt werden können.
        clothing.changeItemNameTag("Hausschuhe")

Zauberstab = Weapon(30, 20, 80)
Keule = Weapon(50, 10, 10)

Zaubermantel = Clothing(0, 70, 70, 25, 25)
Orkhelm = Clothing(5, 70, 70, 25, 25)

Ork = Character(15, 50, 50)
Zauberer = Character(50, 15, 15)  

def runMainLoop():
    while True:
            userInput = input("Mit welchem Charakter möchtest Du kämpfen? Wähle zwischen Ork oder Zauberer!").upper()
            
            # Wenn du den Input-String in Caps konvertierst, wird ein Fehler wie OrK oder ork vermieden.
            if userInput == "ORK":

                player = Ork
                targetInput = input("Wen möchtest du angreifen?(muss Zauberer)").upper()

                if targetInput == "ZAUBERER":
                    target = Zauberer
            else:
                player = Zauberer
                targetInput = input("Wen möchtest du angreifen?(muss Ork)").upper()

                if targetInput == "ORK":
                    target = Ork

            #Alles was nach der Character Auswahl kommt war bei dir redundant. Versuche solche Dinge in Methoden auszulagern!
            selectedWeapon = input("Wähle deine Waffe: Keule oder Zauberstab!").upper()
            selectedClothing = input("Wähle deine Ruestung: Orkhelm oder Zaubermantel?").upper()

            if selectedWeapon == "KEULE":
                player.setWeapon(Keule)
                target.setWeapon(Zauberstab)
            elif selectedWeapon == "ZAUBERSTAB":
                player.setWeapon(Zauberstab)
                target.setWeapon(Keule)

            if selectedClothing == "ORKHELM":
                player.setClothing(Orkhelm)
                target.setClothing(Zaubermantel)
            elif selectedClothing == "ZAUBERMANTEL":
                player.setClothing(Zaubermantel)
                target.setClothing(Orkhelm)

            # Diesen Teil deines Codes verstehe ich nicht ganz. Ich habe versucht mich an deine Gamelogik zu halten, aber ich kann für nichts garantieren.
            while target.health > 0 and player.health > 0:
                if player.mana < 50:
                    if player.mana < 30:
                        print("Not enough Mana for new attack left!")
                        break
                    player.attack(target, "weak")
                else:
                    player.attack(target, "default")
                print("Enemy HP: "+str(target.health))
                print ("Own HP: " + str(player.health)+"\n")

                if target.mana < 50:
                    if target.mana -30 < 0:
                        print("Not enough Mana for new attack left!")
                        break
                    target.attack(player,"weak")
                else:
                    target.attack(player, "default")
                print("Enemy HP: "+str(target.health))
                print ("Own HP: " + str(player.health)+"\n")
            
            if target.health <= 0:
                print("WIN! ENEMY DEAD")
            else:
                print("LOSE! YOU ARE DEAD")
            break

runMainLoop()

# Du hast hier auf jeden Fall ein cooles Projekt, mit dem du wirklich fast alles lernen kannst, was man können muss. Ich wollte dir auch nicht mit meinen 
# überkomplizierten Ansätzen, den Spaß am Programmieren nehmen, aber bei mir war es so, dass ich nur Dinge gelernt habe, wenn jemand anderes sie mir gezeigt hat.
# Bsw. die Python Typisierung (zahl : int). Kannte ich nicht und ich wusste nicht, dass ich es brauche, ergo ich hätte niemals davon erfahren, hätte Timo es mir nicht gezeigt.
# Deswegen habe ich möglichst viel in dieses Projekt herein gebracht, damit du es wenigstens mal gehört hast und dich dann zurück erinnernt kannst, solltest du es brauchen.

# Worauf du auf jeden Fall achten solltest ist die Redundanz in deinem Code! Sobald du etwas ein zweites mal schreibst, kannst du es wahrscheinlich auslagern oder kürzen.
# Dinge die im if und else gleich sind, können teilweise darunter geschrieben werden, was den Code verkürzt.

# Und denk immer schön dynamisch! Auch wenn du heute nur 2 Waffen hast, implementiere immer gleich dynmiasch für n-Waffen. Am Ende muss man es sowieso machen :D

# Ansonsten wünsch ich dir noch viel Spaß beim Programmieren lernen und du kannst mir immer gerne ein bisschen Python Code schicken.Ich schaue da gerne drüber, wenn
# ich dich jetzt nicht zu sehr abgeschreckt habe. Ich hoffe du findest deinen Code noch in meinem Code. Prinzipell habe ich wenig abgeändert und eigentlich fast nur 
# deinen Code gekürzt. Bleib dran, dann bist du in 2 Wochen besser als Micha ^^

#Leonard