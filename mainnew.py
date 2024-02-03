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
'''
curse = False
enemyFire = False
playerFire = False
enemyPoison = False
playerPoison = False
enemyCoinSteal = False
enemyFreeze = False
playerStatusCount = 0
'''
enemyNum = 0
soldierImg = pygame.image.load("skeleton.png")
tankImg = pygame.image.load("sumo.png")
wizardImg = pygame.image.load("wizard.png")
potionImg = pygame.image.load("potion.png")
goblinImg = pygame.image.load("goblin.png")
dragonImg = pygame.image.load("dragon.png")
slimeImg = pygame.image.load("slime.png")
skeletonImg = pygame.image.load("skeletonEnemy.png")
serpentImg = pygame.image.load("serpent.png")
fireballImg = pygame.image.load("fireball.png")

# enemyStatusList = [curse, enemyFire, enemyPoison, enemyCoinSteal, enemyFreeze]

'''
def enemyStatusReset(enemyStatus):
    for status in enemyStatus:
        status = False
        return status
'''

def saving(nameSave, classType, playerHealth, maxHealth, damage, count, difficulty,playerCoins,healPotions,Weapon1,Weapon2,weapon1count):
    try:
        os.mkdir(f"Users/{nameSave}")
    except: 
        pass

    f = open(f"Users/{nameSave}/Savefile.csv", "w")
    f.write(f"{classType},{playerHealth},{maxHealth},{damage},{count},{difficulty},{playerCoins},{healPotions},{Weapon1},{Weapon2},{weapon1count}")
    f.close()

def bossGen():
    # enemyStatusReset(enemyStatusList)
    # enemyFreeze = True
    enemy = "Frost Dragon"
    enemyHealth = 15
    coins = enemyHealth * 2
    enemyDamage = 6
    enemyHitMessage = "uses it's ice breath!"
    return enemy, enemyHealth, coins, enemyDamage, enemyHitMessage

def enemyGen():
    enemyNum = randint(1,5)
    # enemyStatusReset(enemyStatusList)
    if enemyNum == 1:
        # enemyCoinSteal = True
        enemy = "Goblin"
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 2
        enemyHitMessage = "swings its club!"
    if enemyNum == 2:
        # curse = True
        enemy = "Skeleton"
        enemyHealth = 6
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "shoots an arrow!"
    if enemyNum == 3:
        enemy = "Slime"
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 1
        enemyHitMessage = "bounces around!"
    if enemyNum == 4:
        # enemyFire = True
        enemy = "Dragon"
        enemyHealth = 8
        coins = enemyHealth
        enemyDamage = 5
        enemyHitMessage = "uses it's fire breath!"
    if enemyNum == 5:
        # enemyPoison = True
        enemy = "Serpent"
        enemyHealth = 7
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "bites!"
    return enemy, enemyHealth, coins, enemyDamage, enemyHitMessage

'''
# Poison for player
def playerPoisonEffect(playerHealth, playerStatusCount):
    playerStatusCount = 3
    if playerStatusCount > 0:
        print("You've been poisoned! You will lose 1 health every turn.")
        playerHealth -= 1
        playerStatusCount -= 1
    return playerStatusCount, playerHealth
'''

'''
# Poison for enemy
def enemyPoisonEffect():
    playerStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 1
        enemyStatusCount -= 1
'''

'''
# Curse
def curseEffect(playerStatusCount, playerHealth):
    if playerStatusCount == 0:
        playerStatusCount = 3
        print("You have been cursed!")
    elif playerStatusCount > 0:
        playerStatusCount -= 1
    if playerStatusCount == 0:
        print("You have died from curse...")
        playerHealth = 0
    if playerStatusCount >= 1:
        print("You will die from curse in", str(playerStatusCount), "turn(s).")
    return playerStatusCount, playerHealth
'''

'''
# Fire for player
def playerFireEffect(playerHealth, maxHealth):
    print("You've been Burned! You lost 2 health and your max health has been reduced by 1!")
    # maybe don't remove health, just reduce max health to be less op
    playerHealth -= 2
    maxHealth -= 1
    return playerHealth, maxHealth
'''

'''
# Fire for enemy
def enemyFireEffect():
    enemyStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 2
        enemyStatusCount -= 1
'''

'''
# Coin steal for player
def playerCoinStealEffect(playerCoins):
    playerCoins -= 2
    print("The Goblin stole 2 of your coins!")
    return playerCoins
'''

'''
def playerFreezeEffect(damage):
    if damage > 1:
        damage -= 1
        print("You've been Frozen! Your damage has been reduced by 1!")
        return damage
'''

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

def startMenu():
    screen.blit(background, (0, 0))
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
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
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
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            if classType == 1:
                screen.blit(soldierImg, (300, 200))
                button(screen, (0, 0), "Soldier", (143, 186, 255))
                button(screen, (0, 50), "Tank")
                button(screen, (0, 100), "Wizard")
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 2:
                screen.blit(tankImg, (300, 200))
                button(screen, (0, 0), "Soldier")
                button(screen, (0, 50), "Tank", (143, 186, 255))
                button(screen, (0, 100), "Wizard")
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 3:
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
    return classType

def storeMenu():
    screen.fill((0, 0, 0))
    screen.blit(storeBackground, (0, 0))
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
    screen.fill((0, 0, 0))
    screen.blit(storeBackground, (0, 0))
    b1 = button(screen, (0, 0), "+1 Max Health (5 coins)")
    b2 = button(screen, (0, 50), "+1 Damage (5 coins)")
    b3 = button(screen, (0, 100), "Back")
    clicked = False
    running = True
    while running:
        if clicked:
            screen.fill((0, 0, 0))
            screen.blit(storeBackground, (0, 0))
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
    screen.fill((0, 0, 0))
    screen.blit(storeBackground, (0, 0))
    b1 = button(screen, (0, 0), "Health Potion (3 coins, 3 in your inventory)")
    b2 = button(screen, (0, 50), "Back")
    clicked = False
    running = True
    while running:
        if clicked:
            screen.fill((0, 0, 0))
            screen.blit(storeBackground, (0, 0))
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

def restMenu(playerHealth, maxHealth):
    screen.fill((0, 0, 0))
    screen.blit(restBackground, (0, 0))
    b1 = button(screen, (350, 350), "Continue")
    pygame.mixer.music.load("fireplace-fire-crackling-loop-123930.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    playerHealth, maxHealth = rest(playerHealth, maxHealth)
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
    pygame.mixer.music.load("medieval-fantasy-142837.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    return playerHealth, maxHealth

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
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
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
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
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
def battle(count, difficulty, enemyHealth, enemyDamage, enemyHitMessage, coins, playerCoins, playerHealth, maxHealth, damage, enemy, healPotions):
    # pre-battle constants
    enemyStun = 0

    # Opening Battle text
    print(f"\nA {enemy} appears!")

    # Scaling
    count += 1
    scaling = (count // 10) * 0.25
    if difficulty == 2:
        enemyHealth += enemyHealth * scaling
    # Battle System
    while enemyHealth > 0 or playerHealth > 0:
        # Player Selection
        print(f"\n\n{name} Health: {playerHealth}\t{enemy}'s Health: {enemyHealth}\n{'-'*39}\n1. {Weapon1} (75% damage chance)\n2. {Weapon2} (50% stun chance)\n3. Heal {healPotions} left\n4. Run\n5. Save and Quit")
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        selection = battleMenu(enemy)

        # Damage Attack
        if selection == 1:
            damageChance = randint(1, 4)
            if damageChance == 1:
                print(f"{name} missed!\n")
            else:
                print(f"\n{name} used {Weapon1} to damage the {enemy} for {damage} health!")
                enemyHealth -= damage
                if enemyHealth < 0:
                    enemyHealth = 0
                print(f"{enemy}'s health is at {enemyHealth}\n")
                fireballAnimation(screen, enemy)
            if enemyHealth <= 0:
                break
        # Stun Attack
        if selection == 2:
            print(f"\n{name} used {Weapon2} to knock back the {enemy}!")
            stunChance = randint(1, 2)
            if stunChance == 1:
                print(f"{enemy} is stunned!\n")
                print(f"{enemy}'s health is at {enemyHealth}")
                enemyStun = 2

            if stunChance == 2:
                print("Stun failed!\n")
                enemyStun = 0
        # Heal System
        if selection == 3:
            if playerHealth == maxHealth:
                print("Can't heal any more!")
            if playerHealth < maxHealth:
                if healPotions > 0:
                    healNum = randint(1, 3)
                    if healNum > (maxHealth - playerHealth):
                        healNum = maxHealth - playerHealth
                    print(f"\nHealed {healNum} health points!")
                    playerHealth += healNum
                    if playerHealth > maxHealth:
                        playerHealth = maxHealth
                    healPotions -= 1
                    print(f"{name}'s health is at {playerHealth}\n")
                if healPotions == 0:
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
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            save = saveMenu()
            if save == 1:
                saving(nameSave,classType,playerHealth,maxHealth,damage,count,difficulty,playerCoins,healPotions,Weapon1,Weapon2,weapon1count)
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
            print(enemy, enemyHitMessage)
            hitChance = randint(1, 2)
            if hitChance == 1:
                print(f"{enemy} damages {name} for {enemyDamage} health!\n")
                '''
                if curse:
                    curseCount = 1
                if enemyFire:
                    enemyFireCount = 1
                if enemyPoison:
                    enemyPoisonCount = 1
                if enemyCoinSteal:
                    playerCoinStealEffect(playerCoins)
                if enemyFreeze:
                    playerFreezeEffect(damage)
                '''
                playerHealth -= enemyDamage
                if playerHealth < 0:
                    playerHealth = 0
                print(f"{name}'s health is at {playerHealth}")
            if hitChance == 2:
                print(f"{enemy} misses the attack!")
            if playerHealth <= 0:
                break
        if enemyStun > 0:
            print(f"{enemy} is stunned and can't move!")
            enemyStun -= 1
        '''
        if curse == True and curseCount == 1:
            playerStatusCount, playerHealth = curseEffect(playerStatusCount, playerHealth)
        if enemyPoison == True and enemyPoisonCount == 1:
            playerStatusCount, playerHealth = playerPoisonEffect(playerHealth, playerStatusCount)
        if enemyFire == True and enemyFireCount == 1:
            playerHealth, maxHealth = playerFireEffect(playerHealth, maxHealth)
        '''
        if playerHealth <= 0:
            break
    damage = baseDamage
    if enemyHealth <= 0 and playerHealth <= 0:
        print("You both died!")
    elif enemyHealth <= 0:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
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
        print(f"\n\n{name} defeated the {enemy}!")
        playerCoins += coins
        print(f"{name} gained {coins} coins!\n")
    elif playerHealth <= 0:
        print(f"{name} lost...")
    else:
        print("\nRun Successful!")


# Defining store()
def store(playerCoins, damage, healPotions, maxHealth, weapon1count):
    while True:
        purchase = storeMenu()
        # Stat Upgrade section
        # while True:
        if purchase == 1:
            purchase2 = upgradesMenu()
            # max health
            if purchase2 == 1:
                if playerCoins < 5:
                    print("You do not have enough coins")
                if playerCoins >= 5:
                    maxHealth += 1
                    playerCoins -= 5
                    print(f"{name}'s max health is now {maxHealth}")
                    return playerCoins, damage, healPotions, maxHealth, weapon1count
            if purchase2 == 2:
                # damage
                if playerCoins < 5:
                    print("You do not have enough coins")
                if playerCoins >= 5:
                    damage += 1
                    baseDamage = damage
                    playerCoins -= 5
                    print(f"{name}'s new damage is {damage}")
                    return playerCoins, damage, healPotions, maxHealth, weapon1count

        # while True:
        if purchase == 2:
            purchase3 = potionsMenu()
            if purchase3 == 1:
                if playerCoins < 5:
                    print("You do not have enough coins")
                if playerCoins >= 3:
                    if healPotions >= 3:
                        print("You already have max potions!")
                    else:
                        healPotions += 1
                        playerCoins -= 3
                        print(f"{name} now has {healPotions} health potions")
                        return playerCoins, damage, healPotions, maxHealth, weapon1count

        # New Weapon
        if purchase == 3:
            # Different Store Weapons
            if weapon1count == 1:
                storeWeapon = "Frost Spear"
            elif weapon1count == 2:
                storeWeapon = "Flame Bow"
            elif weapon1count == 3:
                storeWeapon = "Mace"
            elif weapon1count > 3:
                storeWeapon = "Frost Spear"
                weapon1count = 1

            print(f"\nNew Weapons\n{'-'*39}\n1. New Primary Weapon: {storeWeapon} (20 coins, +2 damage)\n2. New Secondary Weapon: WIP\n3. Exit")
            purchase4 = int(input("Enter desired purchase: "))
            # New Weapon
            if purchase4 == 1:
                if playerCoins < 20:
                    print("You do not have enough coins")
                if playerCoins >= 20:
                    weapon1count += 1
                    playerCoins -= 20
                    damage += 2
                    baseDamage = damage
                    Weapon1 = storeWeapon
                    print(f"{name} equipped the {Weapon1}")
                    return playerCoins, damage, healPotions, maxHealth, weapon1count
            # Wall of Flames
            if purchase4 == 2:
                if playerCoins < 15:
                    print("You do not have enough coins")
                if playerCoins >= 15:
                    playerCoins -= 15
                    Weapon2 = "Wall of Flames"
                    print(f"{name} equipped the {Weapon2}")
                    return playerCoins, damage, healPotions, maxHealth, weapon1count

        # Exit
        elif purchase == 4:
            return playerCoins, damage, healPotions, maxHealth, weapon1count
            break


# Defining rest()
def rest(playerHealth, maxHealth):
    # Heal while resting
    print(f"{name} finds a camp to rest and heal their wounds at.")
    playerHealth += 3
    if playerHealth >= maxHealth:
        playerHealth = maxHealth
    print(f"{name}'s health is now {playerHealth}")
    return playerHealth, maxHealth


while True:
    font = pygame.font.SysFont("Arial", 32)
    # Background Music
    pygame.mixer.music.load("medieval-fantasy-142837.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    click_sound = pygame.mixer.Sound("click-game-menu-147356.wav")
    background = pygame.image.load("fantasy-game-background.jpg")
    restBackground = pygame.image.load("936357.jpg")
    restBackground = pygame.transform.scale(restBackground, (600, 400))
    storeBackground = pygame.image.load("Store.jpg")
    storeBackground = pygame.transform.scale(storeBackground, (600, 400))
    screen = pygame.display.set_mode((600, 400))
    menuSelect = startMenu()
    # asks for menu selection
    if menuSelect == 1:
        while True:
            print("Creating new game")
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            name = nameMenu()
            if name == "Back" or name == "back":
                break
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
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
                check = int(
                    input("Do you want to overwrite this file?\n1. Yes\n2. No\n"))
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
                screen.fill((0, 0, 0))
                screen.blit(background, (0, 0))
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
        f = open("Admin.csv", "r")
        f.close()
        name = "Admin"
        classType = 3
        maxHealth = 100
        damage = 100
        baseDamage = damage
        playerCoins = 10000
        healPotions = 3
        playerHealth = 90
        difficulty = 2
        CName = "Wizard"
        Weapon1 = "Fireball"
        Weapon2 = "Wind Spell"
        break

    else:
        print("Not a valid menu selection")
        continue
    if name == "Back" or name == "back":
        continue
    break

# Defining name for saving
nameSave = name
f = open("quickload.csv", "w")
f.write(name)
f.close()
# Class Selection
if menuSelect == 1:
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        classType = classMenu()
        # Soldier
        if classType == 1:
            print("The Soldier is equipped with a Sword and Shield\n")
            CName = "Soldier"
            Weapon1 = "Sword Slash"
            Weapon2 = "Shield Block"
            name = name
            playerHealth = 10
            maxHealth = 10
            damage = 3
            baseDamage = damage
            healPotions = 3
            break
        # Tank
        if classType == 2:
            print("The Tank is equipped only with his Fists and Feet\n")
            CName = "Tank"
            Weapon1 = "Punch"
            Weapon2 = "Kick"
            name = name
            playerHealth = 15
            maxHealth = 15
            damage = 2
            baseDamage = damage
            healPotions = 3
            break
        # Wizard
        if classType == 3:
            print("The Wizard is equipped with Spellbook\n")
            CName = "Wizard"
            Weapon1 = "Fireball"
            Weapon2 = "Wind Spell"
            name = name
            playerHealth = 7
            maxHealth = 7
            damage = 4
            baseDamage = damage
            healPotions = 3
            break
        elif classType > 3 or classType < 1:
            print("Invalid Selection")

elif menuSelect == 2 or menuSelect == 3:
    f = open(f"Users/{nameSave}/Savefile.csv", "r")
    dataIn = f.read()
    dataList = dataIn.split(",")
    classType = int(dataList[0])
    playerHealth = int(dataList[1])
    maxHealth = int(dataList[2])
    damage = int(dataList[3])
    baseDamage = damage
    count = int(dataList[4])
    difficulty = int(dataList[5])
    playerCoins = int(dataList[6])
    healPotions = int(dataList[7])
    # weapon1 and weapon2 are underneath
    weapon1count = int(dataList[10])
    scalecount = count // 10
    scaling = scalecount * 0.25
    f.close()
    if classType == 1:
        CName = "Soldier"
        name = name
    if classType == 2:
        CName = "Tank"
        name = name
    if classType == 3:
        CName = "Wizard"
        name = name
    # Loads Weapons after ^ that
    Weapon1 = dataList[8]
    Weapon2 = dataList[9]

# game begins
print(f"\n\nName: {name}\nMax Health: {maxHealth}\nDamage: {damage}\nCoins: {playerCoins}\nCurrent Health: {playerHealth}\nPotions: {healPotions}\nBattles Completed: {count}\nCurrent Weapons: {Weapon1}, {Weapon2}")
'''
# Picks random choices for different paths and allows choice between two random paths
while True:
    choice1 = randint(0, 4)
    choice2 = randint(0, 4)
    if choice1 == 0 or choice1 == 1 or choice1 == 2:
        print("1. Battle")
    if choice1 == 3:
        print("1. Store")
    if choice1 == 4:
        print("1. Rest")
    if choice2 == 0 or choice2 == 1 or choice2 == 2:
        print("2. Battle")
    if choice2 == 3:
        print("2. Store")
    if choice2 == 4:
        print("2. Rest")
    choice = int(input("What option do you want: "))
    '''
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
while True:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    choice = menu()
    if choice == 1:
        bossCheck = count % 5
        if bossCheck == 0 and count > 0:
            enemyFreeze, enemy, enemyHealth, coins, enemyDamage, enemyHitMessage = bossGen()
            battle(count, difficulty, enemyHealth, enemyDamage, enemyHitMessage, coins, playerCoins, playerHealth, maxHealth, damage, enemy, healPotions)
        else:
            curseCount = 0
            enemyPoisonCount = 0
            enemyFireCount = 0
            enemy, enemyHealth, coins, enemyDamage, enemyHitMessage = enemyGen()
            battle(count, difficulty, enemyHealth, enemyDamage, enemyHitMessage, coins, playerCoins, playerHealth, maxHealth, damage, enemy, healPotions)
    elif choice == 2:
        playerCoins, damage, healPotions, maxHealth, weapon1count = store(playerCoins, damage, healPotions, maxHealth, weapon1count)
    elif choice == 3:
        playerHealth, maxHealth = restMenu(playerHealth, maxHealth)
    elif choice == 4:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        profileDetails1 = font.render((f"Name: {name}"),True, (255, 255, 255))
        profileDetails2 = font.render((f"Damage: {damage}"),True, (255, 255, 255))
        profileDetails3 = font.render((f"Coins: {playerCoins}"),True, (255, 255, 255))
        profileDetails4 = font.render((f"Current Health: {playerHealth}/{maxHealth}"),True, (255, 255, 255))
        profileDetails5 = font.render((f"Potions: {healPotions}"),True, (255, 255, 255))
        profileDetails6 = font.render((f"Battles Completed: {count}"),True, (255, 255, 255))
        profileDetails7 = font.render((f"Current Weapons: {Weapon1}, {Weapon2}"),True, (255, 255, 255))
        screen.blit(profileDetails1, (0, 0))
        screen.blit(profileDetails2, (0, 50))
        screen.blit(profileDetails3, (0, 100))
        screen.blit(profileDetails4, (0, 150))
        screen.blit(profileDetails5, (0, 200))
        screen.blit(profileDetails6, (0, 250))
        screen.blit(profileDetails7, (0, 300))
        profileMenu()
    elif choice == 5:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        save = saveMenu()
        if save == 1:
            saving(nameSave, classType, playerHealth, maxHealth, damage, count, difficulty, playerCoins, healPotions, Weapon1, Weapon2, weapon1count)
            print("Progress saved")
            sys.exit()
        if save == 2:
            print("Exited without Saving")
            sys.exit()
        if save == 3:
            continue
    # Makes sure user is not dead
    if playerHealth <= 0:
        break
    # Autosave
    saving(nameSave, classType, playerHealth, maxHealth, damage, count, difficulty, playerCoins, healPotions, Weapon1, Weapon2, weapon1count)
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
save = saveMenu()
if save == 1:
    saving(nameSave,classType,playerHealth,maxHealth,damage,count,difficulty,playerCoins,healPotions,Weapon1,Weapon2,weapon1count)
    print("Progress saved")
    sys.exit()
if save == 2:
    print("Exited without Saving")
    sys.exit()