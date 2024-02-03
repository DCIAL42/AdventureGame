from random import randint
import sys, pygame
from time import sleep
import os

pygame.init()

count = 0
weapon1count = 1
scalecount = count // 10
scaling = scalecount * 0.25
playerCoins = 0
curseCount = 0
enemyFireCount = 0
enemyPoisonCount = 0
playerStatusCount = 0
enemyNum = 0
soldierImg = pygame.image.load("Image Files/skeleton.png")
tankImg = pygame.image.load("Image Files/sumo.png")
wizardImg = pygame.image.load("Image Files/wizard.png")
potionImg = pygame.image.load("Image Files/potion.png")
goblinImg = pygame.image.load("Image Files/goblin.png")
dragonImg = pygame.image.load("Image Files/dragon.png")
slimeImg = pygame.image.load("Image Files/slime.png")
skeletonImg = pygame.image.load("Image Files/skeletonEnemy.png")
serpentImg = pygame.image.load("Image Files/serpent.png")
fireballImg = pygame.image.load("Image Files/fireball.png")

enemies = [
    {
        "enemy": "Goblin",
        "enemyHealth": "5",
        "coins": "5",
        "enemyDamage": "2",
        "enemyHitMessage": "swings its club!",
        "statusType": "enemyCoinSteal"
    },
    {
        "enemy": "Skeleton",
        "enemyHealth": "6",
        "coins": "6",
        "enemyDamage": "3",
        "enemyHitMessage": "shoots an arrow!",
        "statusType": "curse"
    },
    {
        "enemy": "Slime",
        "enemyHealth": "5",
        "coins": "5",
        "enemyDamage": "1",
        "enemyHitMessage": "bounces around!",
        "statusType": "none"
    },
    {
        "enemy": "Dragon",
        "enemyHealth": "8",
        "coins": "8",
        "enemyDamage": "5",
        "enemyHitMessage": "uses it's fire breath!",
        "statusType": "enemyFire"
    },
    {
        "enemy": "Serpent",
        "enemyHealth": "7",
        "coins": "7",
        "enemyDamage": "3",
        "enemyHitMessage": "bites!",
        "statusType": "enemyPoison"
    },
    {
        "enemy": "Frost Dragon",
        "enemyHealth": "15",
        "coins": "30",
        "enemyDamage": "6",
        "enemyHitMessage": "uses it's ice breath!",
        "statusType": "enemyFreeze"
    }
]

players = [
    {
        "CName": "Soldier",
        "Weapon1": "Sword Slash",
        "Weapon2": "Shield Block",
        "playerHealth": "10",
        "maxHealth": "10",
        "damage": "3",
        "healPotions": "3"
    },
    {
        "CName": "Tank",
        "Weapon1": "Punch",
        "Weapon2": "Kick",
        "playerHealth": "15",
        "maxHealth": "15",
        "damage": "2",
        "healPotions": "3"
    },
    {
        "CName": "Wizard",
        "Weapon1": "Fireball",
        "Weapon2": "Wind Spell",
        "playerHealth": "7",
        "maxHealth": "7",
        "damage": "4",
        "healPotions": "3"
    }
]

def saving(name, classType, difficulty):
    try:
        os.mkdir(f"Users/{name}")
    except: 
        pass
    f = open(f"Users/{name}/Savefile.csv", "w")
    f.write(f"{classType},{player.health},{player.maxHealth},{player.damage},{player.count},{difficulty},{player.coins},{player.healPotions},{player.Weapon1},{player.Weapon2},{player.weapon1count}")
    f.close()

class Player():
    def __init__(self, classType, count, playerCoins, weapon1count, playerStatusCount):
        self.CName = players[classType]["CName"]
        self.Weapon1 = players[classType]["Weapon1"]
        self.Weapon2 = players[classType]["Weapon2"]
        self.health = int(players[classType]["playerHealth"])
        self.maxHealth = int(players[classType]["maxHealth"])
        self.damage = int(players[classType]["damage"])
        self.baseDamage = self.damage
        self.healPotions = int(players[classType]["healPotions"])
        self.count = count
        self.coins = playerCoins
        self.weapon1count = weapon1count
        self.statusCount = playerStatusCount

    def loadChar(self, dataList):
        self.Weapon1 = dataList[8]
        self.Weapon2 = dataList[9]
        self.health = int(dataList[1])
        self.maxHealth = int(dataList[2])
        self.damage = int(dataList[3])
        self.baseDamage = self.damage
        self.healPotions = int(dataList[7])
        self.count = int(dataList[4])
        self.coins = int(dataList[6])
        self.weapon1count = int(dataList[10])

    def poisonEffect(self):
        print("You've been poisoned! You will lose 1 health every turn.")
        self.health -= 1
    
    def curseEffect(self):
        if self.statusCount == 0:
            self.statusCount = 3
            print("You have been cursed!")
            print("You will die from curse in", str(self.statusCount), "turn(s).")
        elif self.statusCount > 0:
            self.statusCount -= 1
            if self.statusCount == 0:
                print("You have died from curse...")
                self.health = 0
            if self.statusCount >= 1:
                print("You will die from curse in", str(self.statusCount), "turn(s).")
    
    def fireEffect(self):
        print("You've been Burned! You lost 2 health and your max health has been reduced by 1!")
        self.health -= 2
        self.maxHealth -= 1
    
    def playerCoinStealEffect(self):
        self.coins -= 2
        print("The Goblin stole 2 of your coins!")
    
    def freezeEffect(self):
        if self.damage > 1:
            self.damage -= 1
            print("You've been Frozen! Your damage has been reduced by 1!")

class Enemy(Player):
    def __init__(self, enemyNum):
        self.enemy = enemies[enemyNum]["enemy"]
        self.health = int(enemies[enemyNum]["enemyHealth"])
        self.coins = int(enemies[enemyNum]["coins"])
        self.damage = int(enemies[enemyNum]["enemyDamage"])
        self.hitMessage = enemies[enemyNum]["enemyHitMessage"]
        self.statusType = enemies[enemyNum]["statusType"]

def button(screen, position, text, color=(100, 100, 100)):
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    r, g, b = color
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (r, g, b), (x, y, w, h))
    return screen.blit(text_render, (x, y))

def showBackground():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

def startMenu():
    showBackground()
    b1 = button(screen, (0, 100),  "Quickload")
    b2 = button(screen, (0, 150), "Admin")
    b3 = button(screen, (0, 50), "Load Game")
    b4 = button(screen, (0, 0), "New Game")
    b5 = button(screen, (550, 0), "Exit")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    menuSelect = 3
                    click_sound.play()
                    running = False
                if b2.collidepoint(pygame.mouse.get_pos()):
                    menuSelect = 5
                    click_sound.play()
                    running = False
                if b3.collidepoint(pygame.mouse.get_pos()):
                    menuSelect = 2
                    click_sound.play()
                    running = False
                if b4.collidepoint(pygame.mouse.get_pos()):
                    menuSelect = 1
                    click_sound.play()
                    running = False
                if b5.collidepoint(pygame.mouse.get_pos()):
                    menuSelect = 4
                    click_sound.play()
                    running = False
        pygame.display.update()
    return menuSelect

def nameMenu():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(0, 350, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    active = True
    text = ''
    text_change = False
    b1 = button(screen, (0, 0), "Back")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if active:
                    if event.key == pygame.K_RETURN:
                        name = text.title().strip()
                        text = ''
                        running = False
                    if event.key == pygame.K_BACKSPACE:
                        text_change = True
                    else:
                        text += event.unicode
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    text_change = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    name = "Back"
                    click_sound.play()
                    running = False
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
        if text_change:   
            sleep(0.09)     
            text = text[:-1]
        showBackground()
        button(screen, (0, 0), "Back")
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
        pygame.display.update()
    return name

def menu():
    b1 = button(screen, (350, 350), "   Rest   ")
    b2 = button(screen, (470, 350), "Profile")
    b3 = button(screen, (470, 300), " Store ")
    b4 = button(screen, (350, 300), "  Battle  ")
    b5 = button(screen, (550, 0), "Exit")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    choice = 3
                    click_sound.play()
                    running = False
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    choice = 4
                    click_sound.play()
                    running = False
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    choice = 2
                    click_sound.play()
                    running = False
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    choice = 1
                    click_sound.play()
                    running = False
                elif b5.collidepoint(pygame.mouse.get_pos()):
                    choice = 5
                    click_sound.play()
                    running = False
        pygame.display.update()
    return choice

def profileMenu():
    b1 = button(screen, (350, 350), "Continue")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    running = False
        pygame.display.update()

def difficultyMenu():
    b1 = button(screen, (0, 0), "Easy")
    b2 = button(screen, (0, 50), "Hard")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    difficulty = 1
                    click_sound.play()
                    running = False
                if b2.collidepoint(pygame.mouse.get_pos()):
                    difficulty = 2
                    click_sound.play()
                    running = False
        pygame.display.update()
    return difficulty

def classMenu():
    b1 = button(screen, (0, 0), "Soldier")
    b2 = button(screen, (0, 50), "Tank")
    b3 = button(screen, (0, 100), "Wizard")
    clicked = False
    running = True
    while running:
        if clicked:
            showBackground()
            if classType == 0:
                screen.blit(soldierImg, (300, 200))
                button(screen, (0, 0), "Soldier", (143, 186, 255))
                button(screen, (0, 50), "Tank")
                button(screen, (0, 100), "Wizard")
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 1:
                screen.blit(tankImg, (300, 200))
                button(screen, (0, 0), "Soldier")
                button(screen, (0, 50), "Tank", (143, 186, 255))
                button(screen, (0, 100), "Wizard")
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 2:
                screen.blit(wizardImg, (300, 200))
                button(screen, (0, 0), "Soldier")
                button(screen, (0, 50), "Tank")
                button(screen, (0, 100), "Wizard", (143, 186, 255))
                b4 = button(screen, (500, 350), "Confirm")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    classType = 0
                    click_sound.play()
                    clicked = True
                if b2.collidepoint(pygame.mouse.get_pos()):
                    classType = 1
                    click_sound.play()
                    clicked = True
                if b3.collidepoint(pygame.mouse.get_pos()):
                    classType = 2
                    click_sound.play()
                    clicked = True
                try:
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        click_sound.play()
                        running = False
                except:
                    continue
        pygame.display.update()
    return classType

def storeMenu():
    showBackground()
    b1 = button(screen, (0, 0), "Stat Upgrades")
    b2 = button(screen, (0, 50), "Potions")
    b3 = button(screen, (0, 100), "New Weapons")
    b4 = button(screen, (0, 150), "Back")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    purchase = 1
                    click_sound.play()
                    running = False
                if b2.collidepoint(pygame.mouse.get_pos()):
                    purchase = 2
                    click_sound.play()
                    running = False
                if b3.collidepoint(pygame.mouse.get_pos()):
                    purchase = 3
                    click_sound.play()
                    running = False
                if b4.collidepoint(pygame.mouse.get_pos()):
                    purchase = 4
                    click_sound.play()
                    running = False
        pygame.display.update()
    return purchase

def upgradesMenu():
    showBackground()
    b1 = button(screen, (0, 0), "+1 Max Health (5 coins)")
    b2 = button(screen, (0, 50), "+1 Damage (5 coins)")
    b3 = button(screen, (0, 100), "Back")
    clicked = False
    running = True
    while running:
        if clicked:
            showBackground()
            if purchase2 == 1:
                button(screen, (0, 0), "+1 Max Health (5 coins)", (143, 186, 255))
                button(screen, (0, 50), "+1 Damage (5 coins)")
                button(screen, (0, 100), "Back")
                b4 = button(screen, (500, 350), "Purchase")
            if purchase2 == 2:
                button(screen, (0, 0), "+1 Max Health (5 coins)")
                button(screen, (0, 50), "+1 Damage (5 coins)", (143, 186, 255))
                button(screen, (0, 100), "Back")
                b4 = button(screen, (500, 350), "Purchase")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    purchase2 = 1
                    click_sound.play()
                    clicked = True
                if b2.collidepoint(pygame.mouse.get_pos()):
                    purchase2 = 2
                    click_sound.play()
                    clicked = True
                if b3.collidepoint(pygame.mouse.get_pos()):
                    purchase2 = 3
                    click_sound.play()
                    running = False
                try:
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        click_sound.play()
                        running = False
                except:
                    continue
        pygame.display.update()
    return purchase2

def potionsMenu():
    showBackground()
    b1 = button(screen, (0, 0), "Health Potion (3 coins, 3 in your inventory)")
    b2 = button(screen, (0, 50), "Back")
    clicked = False
    running = True
    while running:
        if clicked:
            showBackground()
            if purchase3 == 1:
                screen.blit(potionImg, (300, 200))
                button(screen, (0, 0), "Health Potion (3 coins, 3 in your inventory)", (143, 186, 255))
                button(screen, (0, 50), "Back")
                b3 = button(screen, (500, 350), "Purchase")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    purchase3 = 1
                    click_sound.play()
                    clicked = True
                if b2.collidepoint(pygame.mouse.get_pos()):
                    purchase3 = 2
                    click_sound.play()
                    running = False
                try:
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        click_sound.play()
                        running = False
                except:
                    continue
        pygame.display.update()
    return purchase3

'''
def newWeaponsMenu():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    b1 = button(screen, (0, 0), "Soldier")
    b2 = button(screen, (0, 50), "Tank")
    b3 = button(screen, (0, 100), "Wizard")
    clicked = False
    running = True
    while running:
        if clicked:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            button(screen, (0, 0), "Soldier")
            button(screen, (0, 50), "Tank")
            button(screen, (0, 100), "Wizard")
            if classType == 1:
                screen.blit(soldierImg, (300, 200))
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 2:
                screen.blit(tankImg, (300, 200))
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 3:
                screen.blit(wizardImg, (300, 200))
                b4 = button(screen, (500, 350), "Confirm")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    classType = 1
                    click_sound.play()
                    clicked = True
                if b2.collidepoint(pygame.mouse.get_pos()):
                    classType = 2
                    click_sound.play()
                    clicked = True
                if b3.collidepoint(pygame.mouse.get_pos()):
                    classType = 3
                    click_sound.play()
                    clicked = True
                try:
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        click_sound.play()
                        running = False
                except:
                    continue
        pygame.display.update()
'''

def saveMenu():
    b1 = button(screen, (0, 0), "Save")
    b2 = button(screen, (0, 50), "Don't Save")
    b3 = button(screen, (0, 100), "Back")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    save = 1
                    click_sound.play()
                    running = False
                if b2.collidepoint(pygame.mouse.get_pos()):
                    save = 2
                    click_sound.play()
                    running = False
                if b3.collidepoint(pygame.mouse.get_pos()):
                    save = 3
                    click_sound.play()
                    running = False
        pygame.display.update()
    return save

def restMenu():
    showBackground()
    b1 = button(screen, (350, 350), "Continue")
    pygame.mixer.music.load("Sound Files/fireplace-fire-crackling-loop-123930.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    rest()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    running = False
        pygame.display.update()
    pygame.mixer.music.load("Sound Files/medieval-fantasy-142837.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def battleMenu(enemyType):
    b1 = button(screen, (350, 350), "  Heal  ")
    b2 = button(screen, (470, 350), "  Run  ")
    b3 = button(screen, (470, 300), "  Stun  ")
    b4 = button(screen, (350, 300), " Attack ")
    b5 = button(screen, (550, 0), "Exit")
    screen.blit(wizardImg, (100, 275))
    if enemyType == "Goblin":
        screen.blit(goblinImg, (350, 150))
    if enemyType == "Slime":
        screen.blit(slimeImg, (350, 150))
    if enemyType == "Dragon":
        screen.blit(dragonImg, (350, 150))
    if enemyType == "Skeleton":
        screen.blit(skeletonImg, (350, 150))
    if enemyType == "Serpent":
        screen.blit(serpentImg, (350, 150))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    choice = 3
                    click_sound.play()
                    running = False
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    choice = 4
                    click_sound.play()
                    running = False
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    choice = 2
                    click_sound.play()
                    running = False
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    choice = 1
                    click_sound.play()
                    running = False
                elif b5.collidepoint(pygame.mouse.get_pos()):
                    choice = 5
                    click_sound.play()
                    running = False
        pygame.display.update()
    return choice

def fireballAnimation(screen, enemyType):
    x = 100
    y = 275
    for i in range(250):
        showBackground()
        x += 1.1
        y -= 0.4
        button(screen, (350, 350), "  Heal  ")
        button(screen, (470, 350), "  Run  ")
        button(screen, (470, 300), "  Stun  ")
        button(screen, (350, 300), " Attack ")
        button(screen, (550, 0), "Exit")
        screen.blit(wizardImg, (100, 275))
        if enemyType == "Goblin":
            screen.blit(goblinImg, (350, 150))
        if enemyType == "Slime":
            screen.blit(slimeImg, (350, 150))
        if enemyType == "Dragon":
            screen.blit(dragonImg, (350, 150))
        if enemyType == "Skeleton":
            screen.blit(skeletonImg, (350, 150))
        if enemyType == "Serpent":
            screen.blit(serpentImg, (350, 150))
        fireball = pygame.Rect((x, y, 16, 16))
        pygame.draw.rect(screen, (255, 0, 0), fireball)
        pygame.display.update()
        sleep(0.01)
    showBackground()
    button(screen, (350, 350), "  Heal  ")
    button(screen, (470, 350), "  Run  ")
    button(screen, (470, 300), "  Stun  ")
    button(screen, (350, 300), " Attack ")
    button(screen, (550, 0), "Exit")
    screen.blit(wizardImg, (100, 275))
    if enemyType == "Goblin":
        screen.blit(goblinImg, (350, 150))
    if enemyType == "Slime":
        screen.blit(slimeImg, (350, 150))
    if enemyType == "Dragon":
        screen.blit(dragonImg, (350, 150))
    if enemyType == "Skeleton":
        screen.blit(skeletonImg, (350, 150))
    if enemyType == "Serpent":
        screen.blit(serpentImg, (350, 150))
    pygame.display.update()
    sleep(0.01)

# Defining battle()
def battle(difficulty):
    # pre-battle constants
    enemyStun = 0
    curseCount = 0
    enemyFireCount = 0
    enemyPoisonCount = 0
    player.statusCount = 0

    # Scaling
    player.count += 1
    scaling = (player.count // 10) * 0.25
    if difficulty == 2:
        enemy1.health += enemy1.health * scaling
    # Battle System
    while enemy1.health > 0 or player.health > 0:
        # Player Selection
        print(f"\n\n{name} Health: {player.health}\t{enemy1.enemy}'s Health: {enemy1.health}\n{'-'*39}\n1. {player.Weapon1} (75% damage chance)\n2. {player.Weapon2} (50% stun chance)\n3. Heal {player.healPotions} left\n4. Run\n5. Save and Quit")
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        selection = battleMenu(enemy1.enemy)

        # Damage Attack
        if selection == 1:
            damageChance = randint(1, 4)
            if damageChance == 1:
                print(f"{name} missed!\n")
            else:
                print(f"\n{name} used {player.Weapon1} to damage the {enemy1.enemy} for {player.damage} health!")
                enemy1.health -= player.damage
                if enemy1.health < 0:
                    enemy1.health = 0
                print(f"{enemy1.enemy}'s health is at {enemy1.health}\n")
                fireballAnimation(screen, enemy1.enemy)
            if enemy1.health <= 0:
                break
        # Stun Attack
        if selection == 2:
            print(f"\n{name} used {player.Weapon2} to knock back the {enemy1.enemy}!")
            stunChance = randint(1, 2)
            if stunChance == 1:
                print(f"{enemy1.enemy} is stunned!\n")
                print(f"{enemy1.enemy}'s health is at {enemy1.health}")
                enemyStun = 2
            elif stunChance == 2:
                print("Stun failed!\n")
                enemyStun = 0
        # Heal System
        if selection == 3:
            if player.health == player.maxHealth:
                print("Can't heal any more!")
            if player.health < player.maxHealth:
                if player.healPotions > 0:
                    healNum = randint(1, 3)
                    if healNum > (player.maxHealth - player.health):
                        healNum = player.maxHealth - player.health
                    print(f"\nHealed {healNum} health points!")
                    player.health += healNum
                    if player.health > player.maxHealth:
                        player.health = player.maxHealth
                    player.healPotions -= 1
                    print(f"{name}'s health is at {player.health}\n")
                if player.healPotions == 0:
                    print("No Potions Remaining!\n")

        # Run Chance
        if selection == 4:
            runChance = randint(1, 2)
            if runChance == 1:
                break
            if runChance == 2:
                print("Run failed!")

        # Save and exit system
        if selection == 5:
            showBackground()
            save = saveMenu()
            if save == 1:
                saving(name,classType,difficulty)
                pygame.quit()
                print("Progress saved")
                sys.exit()
            if save == 2:
                pygame.quit()
                print("Exited without Saving")
                sys.exit()
            if save == 3:
                continue

        # Enemy hit system
        if enemyStun == 0:
            print(enemy1.enemy, enemy1.hitMessage)
            hitChance = randint(1, 2)
            if hitChance == 1:
                print(f"{enemy1.enemy} damages {name} for {enemy1.damage} health!\n")
                if enemy1.statusType == "curse":
                    curseCount = 1
                if enemy1.statusType == "enemyFire":
                    enemyFireCount = 1
                if enemy1.statusType == "enemyPoison":
                    enemyPoisonCount = 1
                if enemy1.statusType == "enemyCoinSteal":
                    player.playerCoinStealEffect()
                if enemy1.statusType == "enemyFreeze":
                    player.freezeEffect()
                player.health -= enemy1.damage
                if player.health < 0:
                    player.health = 0
                print(f"{name}'s health is at {player.health}")
            if hitChance == 2:
                print(f"{enemy1.enemy} misses the attack!")
            if player.health <= 0:
                break
        if enemyStun > 0:
            print(f"{enemy1.enemy} is stunned and can't move!")
            enemyStun -= 1
        if enemy1.statusType == "curse" and curseCount == 1:
            player.curseEffect()
        if enemy1.statusType == "enemyPoison" and enemyPoisonCount == 1:
            player.poisonEffect()
        if enemy1.statusType == "enemyFire" and enemyFireCount == 1:
            player.fireEffect()
        if player.health <= 0:
            break
    player.damage = player.baseDamage
    if enemy1.health <= 0 and player.health <= 0:
        print("You both died!")
    elif enemy1.health <= 0:
        showBackground()
        button(screen, (350, 350), "  Heal  ")
        button(screen, (470, 350), "  Run  ")
        button(screen, (470, 300), "  Stun  ")
        button(screen, (350, 300), " Attack ")
        button(screen, (550, 0), "Exit")
        screen.blit(wizardImg, (100, 275))
        fireball = pygame.Rect((375, 175, 16, 16))
        pygame.draw.rect(screen, (255, 0, 0), fireball)
        pygame.display.update()
        sleep(0.01)
        print(f"\n\n{name} defeated the {enemy1.enemy}!")
        player.coins += enemy1.coins
        print(f"{name} gained {enemy1.coins} coins!\n")
    elif player.health <= 0:
        print(f"{name} lost...")
    else:
        print("\nRun Successful!")

# Defining store()
def store():
    while True:
        purchase = storeMenu()
        # Stat Upgrade section
        # while True:
        if purchase == 1:
            purchase2 = upgradesMenu()
            # max health
            if purchase2 == 1:
                if player.coins < 5:
                    print("You do not have enough coins")
                if player.coins >= 5:
                    player.maxHealth += 1
                    player.coins -= 5
                    print(f"{name}'s max health is now {player.maxHealth}")
            if purchase2 == 2:
                # damage
                if player.coins < 5:
                    print("You do not have enough coins")
                if player.coins >= 5:
                    player.damage += 1
                    player.baseDamage = player.damage
                    player.coins -= 5
                    print(f"{name}'s new damage is {player.damage}")

        # while True:
        if purchase == 2:
            purchase3 = potionsMenu()
            if purchase3 == 1:
                if player.playerCoins < 5:
                    print("You do not have enough coins")
                if player.playerCoins >= 3:
                    if player.healPotions >= 3:
                        print("You already have max potions!")
                    else:
                        player.healPotions += 1
                        player.playerCoins -= 3
                        print(f"{name} now has {player.healPotions} health potions")

        # New Weapon
        if purchase == 3:
            # Different Store Weapons
            if player.weapon1count == 1:
                storeWeapon = "Frost Spear"
            elif player.weapon1count == 2:
                storeWeapon = "Flame Bow"
            elif player.weapon1count == 3:
                storeWeapon = "Mace"
            elif player.weapon1count > 3:
                storeWeapon = "Frost Spear"
                player.weapon1count = 1

            print(f"\nNew Weapons\n{'-'*39}\n1. New Primary Weapon: {storeWeapon} (20 coins, +2 damage)\n2. New Secondary Weapon: WIP\n3. Exit")
            purchase4 = int(input("Enter desired purchase: "))
            # New Weapon
            if purchase4 == 1:
                if player.playerCoins < 20:
                    print("You do not have enough coins")
                if player.playerCoins >= 20:
                    player.weapon1count += 1
                    player.playerCoins -= 20
                    player.damage += 2
                    player.baseDamage = player.damage
                    player.Weapon1 = storeWeapon
                    print(f"{name} equipped the {player.Weapon1}")
            # Wall of Flames
            if purchase4 == 2:
                if player.playerCoins < 15:
                    print("You do not have enough coins")
                if player.playerCoins >= 15:
                    player.playerCoins -= 15
                    player.Weapon2 = "Wall of Flames"
                    print(f"{name} equipped the {player.Weapon2}")

        # Exit
        elif purchase == 4:
            break

# Defining rest()
def rest():
    # Heal while resting
    print(f"{name} finds a camp to rest and heal their wounds at.")
    player.health += 3
    if player.health >= player.health:
        player.health = player.health
    print(f"{name}'s health is now {player.health}")

while True:
    font = pygame.font.SysFont("Arial", 32)
    # Background Music
    pygame.mixer.music.load("Sound Files/medieval-fantasy-142837.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    click_sound = pygame.mixer.Sound("Sound Files/click-game-menu-147356.wav")
    background = pygame.image.load("Image Files/fantasy-game-background.jpg")
    restBackground = pygame.image.load("Image Files/936357.jpg")
    restBackground = pygame.transform.scale(restBackground, (600, 400))
    storeBackground = pygame.image.load("Image Files/Store.jpg")
    storeBackground = pygame.transform.scale(storeBackground, (600, 400))
    screen = pygame.display.set_mode((600, 400))
    menuSelect = startMenu()
    # asks for menu selection
    if menuSelect == 1:
        while True:
            print("Creating new game")
            showBackground()
            name = nameMenu()
            if name == "Back":
                break
            showBackground()
            difficulty = difficultyMenu()
            try:
                os.mkdir(f"Users/{name}")
            except:
                pass
            # checks that there is not already a file with that name
            try:
                f = open(f"Users/{name}/Savefile.csv", "r")
                f.close()
                print("\nA file with this name already exists")
                # asks user if they want to overwrite existing file
                check = int(input("Do you want to overwrite this file?\n1. Yes\n2. No\n"))
                if name == "Back" or name == "back":
                    break
                if check == 1:
                    f = open(f"Users/{name}/Savefile.csv", "w")
                    f.close()
                    break
                else:
                    continue
            except:
                # if file doesn't exist, creates new one
                f = open(f"Users/{name}/Savefile.csv", "w")
                f.close()
                break

    elif menuSelect == 2:
        while True:
            try:
                showBackground()
                name = nameMenu()
                if name == "Back" or name == "back":
                    break
                f = open(f"Users/{name}/Savefile.csv", "r")
                f.close()
                break
            except:
                print("No file found with that name.")
                continue
    # quickload system
    elif menuSelect == 3:
        fQuick = open("quickload.csv", "r")
        name = fQuick.read()
    elif menuSelect == 4:
        exit()

    elif menuSelect == 5:
        f = open("Users/Admin/Admin.csv", "r")
        dataIn = f.read()
        dataList = dataIn.split(",")
        name = "Admin"
        classType = int(dataList[0])
        difficulty = int(dataList[5])
        player = Player(classType, count, playerCoins, weapon1count, playerStatusCount)
        player.loadChar(dataList)
        f.close()
        break

    else:
        print("Not a valid menu selection")
        continue
    if name == "Back" or name == "back":
        continue
    break

f = open("quickload.csv", "w")
f.write(name)
f.close()
# Class Selection
if menuSelect == 1:
    showBackground()
    classType = classMenu()
    player = Player(classType, count, playerCoins, weapon1count, playerStatusCount)

elif menuSelect == 2 or menuSelect == 3:
    f = open(f"Users/{name}/Savefile.csv", "r")
    dataList = f.read().split(",")
    classType = int(dataList[0])
    player = Player(classType, count, playerCoins, weapon1count, playerStatusCount)
    player.loadChar(dataList)
    difficulty = int(dataList[5])
    scaling = (count // 10) * 0.25
    f.close()

# game begins
print(f"\n\nName: {name}\nMax Health: {player.maxHealth}\nDamage: {player.damage}\nCoins: {player.coins}\nCurrent Health: {player.health}\nPotions: {player.healPotions}\nBattles Completed: {count}\nCurrent Weapons: {player.Weapon1}, {player.Weapon2}")

showBackground()
while True:
    showBackground()
    choice = menu()
    if choice == 1:
        if count % 5 == 0 and count:
            boss = Enemy(5)
            battle(difficulty)
        else:
            enemy1 = Enemy(randint(0,4))
            battle(difficulty)
    elif choice == 2:
        store()
    elif choice == 3:
        restMenu()
    elif choice == 4:
        showBackground()
        screen.blit(font.render((f"Name: {name}"),True, (255, 255, 255)), (0, 0))
        screen.blit(font.render((f"Damage: {player.damage}"),True, (255, 255, 255)), (0, 50))
        screen.blit(font.render((f"Coins: {player.coins}"),True, (255, 255, 255)), (0, 100))
        screen.blit(font.render((f"Current Health: {player.health}/{player.maxHealth}"),True, (255, 255, 255)), (0, 150))
        screen.blit(font.render((f"Potions: {player.healPotions}"),True, (255, 255, 255)), (0, 200))
        screen.blit(font.render((f"Battles Completed: {player.count}"),True, (255, 255, 255)), (0, 250))
        screen.blit(font.render((f"Current Weapons: {player.Weapon1}, {player.Weapon2}"),True, (255, 255, 255)), (0, 300))
        profileMenu()
    elif choice == 5:
        showBackground()
        save = saveMenu()
        if save == 1:
            saving(name, classType, difficulty)
            print("Progress saved")
            sys.exit()
        if save == 2:
            print("Exited without Saving")
            sys.exit()
        if save == 3:
            continue
    # Makes sure user is not dead
    if player.health <= 0:
        break
    # Autosave
    saving(name, classType, difficulty)
showBackground()
save = saveMenu()
if save == 1:
    saving(name,classType,difficulty)
    print("Progress saved")
    sys.exit()
if save == 2:
    print("Exited without Saving")
    sys.exit()