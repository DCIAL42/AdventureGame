import random
import sys
import time
import pygame

from colorama import Fore, Back, Style
from pygame import mixer


pygame.init()

# Shortcuts for colors
SoldC = Fore.GREEN
TankC = Fore.YELLOW
WizC = Fore.MAGENTA
s = Fore.RESET
b = Back.RESET
n = Style.NORMAL
wrong = Back.RED
count = 0
weapon1count = 1
scalecount = count // 10
scaling = scalecount * 0.25
playerCoins = 0
curse = False
enemyFire = False
playerFire = False
enemyPoison = False
playerPoison = False
enemyCoinSteal = False
enemyFreeze = False
playerStatusCount = 3
enemyNum = 0
soldierImg = pygame.image.load("skeleton.png")
tankImg = pygame.image.load("sumo.png")
wizardImg = pygame.image.load("wizard.png")
potionImg = pygame.image.load("potion.png")


# Boss generation
def bossGen():
    global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, coins, healPotions, curse, enemyFire, enemyPoison, enemyCoinSteal, enemyFreeze
    curse = False
    enemyFire = False
    enemyPoison = False
    enemyCoinSteal = False
    enemyFreeze = True
    enemy = Fore.CYAN + "Frost Dragon" + s
    enemyHealth = 15
    coins = enemyHealth * 2
    enemyDamage = 6
    enemyHitMessage = "uses it's ice breath!"


def enemyGen():
    # Random Enemy Generation
    global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, coins, healPotions, curse, playerStatusCount, enemyFire, enemyPoison, enemyCoinSteal, enemyFreeze
    if enemyNum == 0:
        enemyNum = random.randint(1, 5)
    if enemyNum == 1:
        curse = False
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = True
        enemyFreeze = False
        enemy = Fore.GREEN + "Goblin" + s
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 2
        enemyHitMessage = "swings its club!"

    if enemyNum == 2:
        playerStatusCount = 4
        curse = True
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.WHITE + Style.BRIGHT + "Skeleton" + s + n
        enemyHealth = 6
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "shoots an arrow!"

    if enemyNum == 3:
        curse = False
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.CYAN + "Slime" + s
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 1
        enemyHitMessage = "bounces around!"

    if enemyNum == 4:
        playerStatusCount = 0
        enemyFire = True
        enemyPoison = False
        curse = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.RED + "Dragon" + s
        enemyHealth = 8
        coins = enemyHealth
        enemyDamage = 5
        enemyHitMessage = "uses it's fire breath!"

    if enemyNum == 5:
        playerStatusCount = 0
        enemyPoison = True
        enemyFire = False
        curse = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.YELLOW + "Serpent" + s
        enemyHealth = 7
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "bites!"


# Poison for player
def playerPoisonEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    playerStatusCount = 3
    if playerStatusCount > 0:
        print(Fore.GREEN +
              "You've been poisoned! You will lose 1 health every turn." + s)
        time.sleep(1)
        playerHealth -= 1
        playerStatusCount -= 1


# Poison for enemy
def enemyPoisonEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    playerStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 1
        enemyStatusCount -= 1


# Curse
def curseEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    if playerStatusCount == 4:
        print(Fore.MAGENTA + Style.DIM + "You have been cursed!" + n + s)
        time.sleep(1)
    if playerStatusCount > 0:
        playerStatusCount -= 1
    if playerStatusCount == 0:
        print(Fore.MAGENTA + Style.DIM + "You have died from curse..." + s + n)
        time.sleep(1)
        playerHealth = 0
    if playerStatusCount >= 1:
        print(Fore.MAGENTA + Style.DIM + "You will die from curse in",
              str(playerStatusCount), "turn(s)." + s + n)
        time.sleep(1)


# Fire for player
def playerFireEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount, maxHealth
    playerStatusCount = 3
    if playerStatusCount > 0:
        print(
            Fore.RED + Style.BRIGHT +
            "You've been Burned! You lost 2 health and your max health has been reduced by 1!"
            + s + n)
        time.sleep(1)
        # maybe don't remove health, just reduce max health to be less op
        playerHealth -= 2
        maxHealth -= 1
        # playerStatusCount -= 1


# Fire for enemy
def enemyFireEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount, maxHealth
    enemyStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 2
        enemyStatusCount -= 1


# Coin steal for player
def playerCoinStealEffect():
    global playerCoins
    playerCoins -= 2
    print(Fore.YELLOW + Style.BRIGHT + "The Goblin stole 2 of your coins!" + s +
          n)
    time.sleep(1)


def playerFreezeEffect():
    global damage
    if damage > 1:
        damage -= 1
        print(Fore.BLUE +
              "You've been Frozen! Your damage has been reduced by 1!" + s)
        time.sleep(1)


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
    global menuSelect
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


def nameMenu():
    global name
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
            time.sleep(0.09)     
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


def gameModeMenu():
    global gameMode
    b1 = button(screen, (0, 0), "Story")
    b2 = button(screen, (0, 50), "Endless")
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
                    gameMode = 1
                    click_sound.play()
                    running = False
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    gameMode = 2
                    click_sound.play()
                    running = False
        pygame.display.update()


def menu():
    global choice
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
    global difficulty
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


def classMenu():
    global difficulty, classType
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
                button(screen, (0, 0), "Soldier", (143, 186, 255))
                button(screen, (0, 50), "Tank")
                button(screen, (0, 100), "Wizard")
                b4 = button(screen, (500, 350), "Confirm")
            if classType == 3:
                screen.blit(wizardImg, (300, 200))
                button(screen, (0, 0), "Soldier" (143, 186, 255),)
                button(screen, (0, 50), "Tank")
                button(screen, (0, 100), "Wizard")
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

def storeMenu():
    global purchase
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

def upgradesMenu():
    global purchase2
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

def potionsMenu():
    global purchase3
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

def newWeaponsMenu():
    global difficulty, classType
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

def saveMenu():
    global save
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
    pygame.quit()

def restMenu():
    screen.fill((0, 0, 0))
    screen.blit(restBackground, (0, 0))
    b1 = button(screen, (350, 350), "Continue")
    mixer.music.load("fireplace-fire-crackling-loop-123930.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
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
    mixer.music.load("medieval-fantasy-142837.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)


# Defining battle()
def battle():
    global count, scaling, scalecount
    global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, playerCoins, healPotions, curse, enemyStatusCount, playerStatusCount, curseCount, enemyPoisonCount, enemyFireCount, enemyCoinSteal, damage, Weapon1
    # pre-battle constants
    global playerHealth
    enemyStun = 0

    # Opening Battle text
    print("\n")
    print("A", enemy, "appears!")
    time.sleep(1)

    # Scaling
    count += 1
    scalecount = count // 10
    scaling = scalecount * 0.25
    if difficulty == 2:
        enemyHealth += enemyHealth * scaling
    # Battle System
    while enemyHealth > 0 or playerHealth > 0:
        # Player Selection
        print("\n\n", name, "Health:", Fore.GREEN + str(playerHealth) + s,
              "      ", enemy, "'s Health:", Fore.RED + str(enemyHealth) + s, "\n",
              39 * "-", "\n 1.", Weapon1, "(75% damage chance) \n", "2.", Weapon2,
              "(50% stun chance)", "\n 3.", Fore.GREEN + "Heal" + s, healPotions,
              "left", "\n 4. Run", "\n 5. Save and Quit")
        selection = int(input("What will " + name + " do? "))

        # Damage Attack
        if selection == 1:
            damageChance = random.randint(1, 4)
            if damageChance == 1:
                print(name, "missed!\n")
                time.sleep(1)
            else:
                print("\n" + name, "used", Weapon1, "to damage the", enemy, "for",
                      damage, "health!")
                enemyHealth -= damage
                if enemyHealth < 0:
                    enemyHealth = 0
                print(enemy, "'s health is at", enemyHealth, "\n")
                time.sleep(1)
            if enemyHealth <= 0:
                break
        # Stun Attack
        if selection == 2:
            print("\n", name, "used", Weapon2, "to knock back the", enemy, "!")
            time.sleep(1)
            stunChance = random.randint(1, 2)
            if stunChance == 1:
                print(enemy, "is stunned! \n")
                time.sleep(1)
                print(enemy, "'s health is at", enemyHealth)
                enemyStun = 2

            if stunChance == 2:
                print(Fore.RED + "Stun failed!", "\n" + s)
                enemyStun = 0
            time.sleep(1)
        # Heal System
        global maxHealth
        if selection == 3:
            if playerHealth == maxHealth:
                print(Fore.RED + "Can't heal any more!" + s)
                time.sleep(1)
            if playerHealth < maxHealth:
                if healPotions > 0:
                    healNum = random.randint(1, 3)
                    if healNum > (maxHealth - playerHealth):
                        healNum = maxHealth - playerHealth
                    print(Fore.GREEN + "\nHealed", healNum, "health points!" + s)
                    time.sleep(1)
                    playerHealth += healNum
                    if playerHealth > maxHealth:
                        playerHealth = maxHealth
                    healPotions -= 1
                    print(name, "'s health is at", playerHealth, "\n")
                    time.sleep(1)
                if healPotions == 0:
                    print(Fore.RED + "No Potions Remaining! \n" + s)
                    time.sleep(1)

        # Run Chance
        if selection == 4:
            runChance = random.randint(1, 2)
            if runChance == 1:
                print("\n")
                break
            if runChance == 2:
                print("Run failed!")
                time.sleep(1)

        # Save and exit system
        if selection == 5:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            saveMenu()
            if save == 1:
                f = open(f"{nameSave}.csv", "w")
                f.write(
                    str(classType) + "," + str(playerHealth) + "," + str(maxHealth) +
                    "," + str(damage) + "," + str(count) + "," + str(difficulty) + "," +
                    str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," +
                    Weapon2 + "," + str(weapon1count))
                f.close()
                print("Progress saved")
                time.sleep(1)
                sys.exit()
            if save == 2:
                print("Exited without Saving")
                time.sleep(1)
                sys.exit()
            if save == 3:
                continue

        # Enemy hit system
        if enemyStun == 0:
            print(enemy, enemyHitMessage)
            hitChance = random.randint(1, 2)
            if hitChance == 1:
                print(enemy, "damages", name, "for", enemyDamage, "health!\n")
                if curse:
                    curseCount = 1
                if enemyFire:
                    enemyPoisonCount = 1
                if enemyPoison:
                    enemyPoisonCount = 1
                if enemyCoinSteal:
                    playerCoinStealEffect()
                if enemyFreeze:
                    playerFreezeEffect()
                time.sleep(1)
                playerHealth -= enemyDamage
                if playerHealth < 0:
                    playerHealth = 0
                print(name, "'s health is at", playerHealth)
                time.sleep(1)
            if hitChance == 2:
                print(enemy, "misses the attack!")
                time.sleep(1)
            if playerHealth <= 0:
                break
        if enemyStun > 0:
            print(enemy, "is stunned and can't move!")
            enemyStun -= 1
            time.sleep(1)
        time.sleep(1)
        if curse == True and curseCount == 1:
            curseEffect()
        if enemyPoison == True and enemyPoisonCount == 1:
            playerPoisonEffect()
        if enemyFire == True and enemyFireCount == 1:
            playerFireEffect()
        if playerHealth <= 0:
            break
    # ↓ not sure what this is for, but it was breaking stuff
    damage = baseDamage
    if enemyHealth <= 0 and playerHealth <= 0:
        print("You both died!")
    elif enemyHealth <= 0:
        print("\n\n" + name, "defeated the", enemy, "!")
        playerCoins += coins
        print(name, "gained", coins, "coins! \n")
        time.sleep(1)
    elif playerHealth <= 0:
        print(name, "lost...")
    else:
        print("\n Run Successful!")


# Defining store()
def store():
    global damage
    global maxHealth, playerCoins, healPotions, damage, baseDamage
    while True:
        print("\nBalance:", Fore.YELLOW + str(playerCoins) + s, "\n" + 39 * "-",
              "\n1.", Fore.BLUE + "Stat Upgrades" + s, "\n2.",
              Fore.GREEN + "Potions" + s, "\n3.", Fore.RED + "New Weapons" + s,
              "\n4. Exit")
        storeMenu()
        # Stat Upgrade section
        # while True:
        if purchase == 1:
            print(Fore.BLUE + "\nStat Upgrades" + s, "\n" + 39 * "-", "\n1. +1",
                  Fore.BLUE + "Max Health" + s, "(5 coins)\n2. +1",
                  Fore.RED + "Damage" + s, "(5 coins) \n3. Exit")
            upgradesMenu()
            # max health
            if purchase2 == 1:
                if playerCoins < 5:
                    print("You do not have enough coins")
                    time.sleep(1)
                if playerCoins >= 5:
                    maxHealth += 1
                    playerCoins -= 5
                    print(name, "'s max health is now", maxHealth)
                    time.sleep(1)
            if purchase2 == 2:
                # damage
                if playerCoins < 5:
                    print("You do not have enough coins")
                    time.sleep(1)
                if playerCoins >= 5:
                    damage += 1
                    baseDamage = damage
                    playerCoins -= 5
                    print(name, "'s new damage is", damage)
                    time.sleep(1)
            if purchase2 == 3:
                print("\n")

                # potion section

        # while True:
        if purchase == 2:
            print(Fore.GREEN + "\nPotions" + s, "\n" + 39 * "-",
                  "\n1.", Fore.GREEN + "Health Potions" + s, "(3 coins,",
                  str(healPotions), "in your inventory)", "\n2. Exit")
            potionsMenu()
            if purchase3 == 1:
                if playerCoins < 5:
                    print("You do not have enough coins")
                    time.sleep(1)
                if playerCoins >= 3:
                    if healPotions >= 3:
                        print(Fore.RED + "You already have max potions!" + s)
                        time.sleep(1)
                    else:
                        healPotions += 1
                        playerCoins -= 3
                        print(name, "now has", healPotions, "health potions")
                        time.sleep(1)
            if purchase3 == 2:
                print("\n")

        # New Weapon
        if purchase == 3:
            # Different Store Weapons
            global weapon1count
            if weapon1count == 1:
                storeWeapon = Fore.BLUE + Style.BRIGHT + "Frost Spear" + s + n
            elif weapon1count == 2:
                storeWeapon = Fore.RED + "Flame Bow" + s
            elif weapon1count == 3:
                storeWeapon = Fore.BLACK + "Mace" + s
            elif weapon1count > 3:
                storeWeapon = Fore.BLUE + Style.BRIGHT + "Frost Spear" + s + n
                weapon1count = 1

            print(Fore.RED + "\nNew Weapons" + s, "\n" + 39 * "-",
                  "\n1. New Primary Weapon: ", storeWeapon, " (20 Coins, +2 damage)",
                  "\n2. New Secondary Weapon: WIP", "\n3. Exit")
            purchase4 = int(input("Enter desired purchase: "))
            # New Weapon
            if purchase4 == 1:
                if playerCoins < 20:
                    print("You do not have enough coins")
                    time.sleep(1)
                if playerCoins >= 20:
                    global Weapon1  # storeWeapon
                    weapon1count += 1
                    playerCoins -= 20
                    damage += 2
                    baseDamage = damage
                    Weapon1 = storeWeapon
                    print(name, "equipped the", Weapon1)
                    time.sleep(1)
            # Wall of Flames
            if purchase4 == 2:
                if playerCoins < 15:
                    print("You do not have enough coins")
                    time.sleep(1)
                if playerCoins >= 15:
                    global Weapon2
                    playerCoins -= 15
                    Weapon2 = Fore.RED + "Wall of Flames" + s
                    print(name, "equipped the", Weapon2)
                    time.sleep(1)
                # exit weapon
            if purchase4 == 3:
                print("\n")

        # Exit
        elif purchase == 4:
            print("\n")
            break


# Defining rest()
def rest():
    global playerHealth
    # Heal while resting
    print(name, "finds a camp to rest and heal their wounds at.")
    playerHealth += 3
    if playerHealth >= maxHealth:
        playerHealth = maxHealth
    print(name, "'s health is now", playerHealth)


while True:
    font = pygame.font.SysFont("Arial", 32)
    # Background Music
    mixer.music.load("medieval-fantasy-142837.wav")
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    click_sound = mixer.Sound("click-game-menu-147356.wav")
    background = pygame.image.load("fantasy-game-background.jpg")
    restBackground = pygame.image.load("936357.jpg")
    restBackground = pygame.transform.scale(restBackground, (600, 400))
    storeBackground = pygame.image.load("Store.jpg")
    storeBackground = pygame.transform.scale(storeBackground, (600, 400))
    screen = pygame.display.set_mode((600, 400))
    startMenu()
    # asks for menu selection
    if menuSelect == 1:
        while True:
            print("Creating new game")
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            nameMenu()
            if name == "Back" or name == "back":
                break
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            difficultyMenu()
            # checks that there is not already a file with that name
            try:
                f = open(fr"{name}.csv", "r")
                f.close()
                print("\nA file with this name already exists")
                # asks user if they want to overwrite existing file
                check = int(
                    input("Do you want to overwrite this file?\n1. Yes\n2. No\n"))
                if name == "Back" or name == "back":
                    break
                if check == 1:
                    f = open(fr"{name}.csv", "w")
                    f.close()
                    break
                else:
                    continue
            except:
                # if file doesn't exist, creates new one
                f = open(fr"{name}.csv", "w")
                f.close()
                break

    elif menuSelect == 2:
        while True:
            try:
                screen.fill((0, 0, 0))
                screen.blit(background, (0, 0))
                nameMenu()
                if name == "Back" or name == "back":
                    break
                f = open(fr"{name}.csv", "r")
                f.close()
                break
            except:
                print("No file found with that name.")
                continue
    # quickload system
    elif menuSelect == 3:
        fQuick = open("quickload.csv", "r")
        name = fQuick.read()
        while True:
            try:
                # name = input("Enter your name: ").strip().title()
                if name == "Back" or name == "back":
                    break
                f = open(fr"{name}.csv", "r")
                f.close()
                break
            except:
                print("No file found with that name.")
                continue
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
        CName = WizC + "Wizard"
        Weapon1 = Fore.RED + Style.BRIGHT + "Fireball" + s + n
        Weapon2 = Fore.WHITE + Style.BRIGHT + "Wind Spell" + n + s
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
        classMenu()
        # Soldier
        if classType == 1:
            print(SoldC + "The Soldier is equipped with a Sword and Shield \n" + s)
            CName = SoldC + "Soldier"
            Weapon1 = Fore.RED + "Sword Slash" + s
            Weapon2 = Fore.CYAN + "Shield Block" + s
            name = SoldC + name + s
            playerHealth = 10
            maxHealth = 10
            damage = 3
            baseDamage = damage
            healPotions = 3
            break
        # Tank
        if classType == 2:
            print(TankC + "The Tank is equipped only with his Fists and Feet \n" + s)
            CName = TankC + "Tank"
            Weapon1 = Fore.YELLOW + "Punch" + s
            Weapon2 = Fore.BLUE + "Kick" + s
            name = TankC + name + s
            playerHealth = 15
            maxHealth = 15
            damage = 2
            baseDamage = damage
            healPotions = 3
            break
        # Wizard
        if classType == 3:
            print(WizC + "The Wizard is equipped with Spellbook \n" + s)
            CName = WizC + "Wizard"
            Weapon1 = Fore.RED + Style.BRIGHT + "Fireball" + s + n
            Weapon2 = Fore.WHITE + Style.BRIGHT + "Wind Spell" + n + s
            name = WizC + name + s
            playerHealth = 7
            maxHealth = 7
            damage = 4
            baseDamage = damage
            healPotions = 3
            break
        elif classType > 3 or classType < 1:
            print(wrong, "Invalid Selection", b)

elif menuSelect == 2 or menuSelect == 3:
    f = open(fr"{nameSave}.csv", "r")
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
        CName = SoldC + "Soldier"
        name = SoldC + name + s
    if classType == 2:
        CName = TankC + "Tank"
        name = TankC + name + s
    if classType == 3:
        CName = WizC + "Wizard"
        name = WizC + name + s
    # Loads Weapons after ^ that
    Weapon1 = dataList[8]
    Weapon2 = dataList[9]
    print("File load successful")
    time.sleep(1)

# game begins
# print("\n" * 20)
print("\n\nName:", name, "\nMax Health:", Fore.GREEN + str(maxHealth) + s,
      "\nDamage:", Fore.RED + str(damage) + s, "\nCoins:",
      Fore.YELLOW + str(playerCoins) + s, "\nCurrent Health:",
      Fore.GREEN + str(playerHealth) + s, "\nPotions:",
      Fore.GREEN + str(healPotions) + s, "\nBattles Completed:",
      Fore.CYAN + str(count) + s, "\nCurrent Weapons:", Weapon1, ",", Weapon2)
'''
# Picks random choices for different paths and allows choice between two random paths
while True:
    choice1 = random.randint(0, 4)
    choice2 = random.randint(0, 4)
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
gameModeMenu()
if gameMode == 2:
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        menu()
        if choice == 1:
            bossCheck = count % 5
            if bossCheck == 0 and count > 0:
                bossGen()
                battle()
            else:
                curseCount = 0
                enemyPoisonCount = 0
                enemyFireCount = 0
                enemyGen()
                battle()
        elif choice == 2:
            store()
        elif choice == 3:
            restMenu()
        elif choice == 4:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            profileDetails1 = font.render(("Name:"+ name),True, (255, 255, 255))
            profileDetails2 = font.render(("Max Health:" + str(maxHealth)),True, (255, 255, 255))
            profileDetails3 = font.render(("Damage:" + str(damage)),True, (255, 255, 255))
            profileDetails4 = font.render(("Coins:" + str(playerCoins)),True, (255, 255, 255))
            profileDetails5 = font.render(("Current Health:" + str(playerHealth)),True, (255, 255, 255))
            profileDetails6 = font.render(("Potions:" + str(healPotions)),True, (255, 255, 255))
            profileDetails7 = font.render(("Battles Completed:" + str(count)),True, (255, 255, 255))
            profileDetails8 = font.render(("Current Weapons:" + Weapon1 + "," + Weapon2),True, (255, 255, 255))
            screen.blit(profileDetails1, (0, 0))
            screen.blit(profileDetails2, (0, 50))
            screen.blit(profileDetails3, (0, 100))
            screen.blit(profileDetails4, (0, 150))
            screen.blit(profileDetails5, (0, 200))
            screen.blit(profileDetails6, (0, 250))
            screen.blit(profileDetails7, (0, 300))
            screen.blit(profileDetails8, (0, 350))
            profileMenu()
        elif choice == 5:
            print("\n")
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            saveMenu()
            if save == 1:
                f = open(f"{nameSave}.csv", "w")
                f.write(
                    str(classType) + "," + str(playerHealth) + "," + str(maxHealth) +
                    "," + str(damage) + "," + str(count) + "," + str(difficulty) + "," +
                    str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," +
                    Weapon2 + "," + str(weapon1count))
                f.close()
                print("Progress saved")
                time.sleep(1)
                sys.exit()
            if save == 2:
                print("Exited without Saving")
                time.sleep(1)
                sys.exit()
            if save == 3:
                continue
            # Makes sure user is not dead
        if playerHealth <= 0:
            break
        # Autosave
        f = open(f"{nameSave}.csv", "w")
        f.write(
            str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," +
            str(damage) + "," + str(count) + "," + str(difficulty) + "," +
            str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," +
            Weapon2)
        f.close()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    saveMenu()
    if save == 1:
        f = open(f"{nameSave}.csv", "w")
        f.write(
            str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," +
            str(damage) + "," + str(count) + "," + str(difficulty) + "," +
            str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," +
            Weapon2 + "," + str(weapon1count))
        f.close()
        print("Progress saved")
        time.sleep(1)
        sys.exit()
    if save == 2:
        print("Exited without Saving")
        time.sleep(1)
        sys.exit()

elif gameMode == 1:
    # define the different rooms in the game
    # while True:
    room_Forest = {
        "name": "Forest",
        "description":
            "You are in a large, enchanted forest. The trees are so tall that the clouds are below the top of them.",
        "paths": ["Path"],
        "items": ["Health Potion"],
        "battles": ["Slime"]
    }

    room_Path = {
        "name": "Path",
        "description": "You are on a long, gravel path.",
        "paths": ["Town", "Forest", "Swamp", "Castle"],
        "items": ["Health Potion"],
        "battles": ["Slime"]
    }

    room_Town = {
        "name": "Town",
        "description":
            "You are in a big, bustling town. You are standing in a busy street, there are shops on either side of the street.",
        "paths": ["Path"],
        "items": ["Health Potion"],
        "battles": ["Slime"]
    }

    room_Swamp = {
        "name": "Swamp",
        "description": "",
        "paths": ["Path"],
        "items": ["Health Potion"],
        "battles": ["Slime"]
    }

    room_Castle = {
        "name": "Castle",
        "description": "",
        "paths": ["Path"],
        "items": ["Health Potion"],
        "battles": ["Slime"]
    }

    # define the player's inventory and current room
    inventory = []
    current_room = room_Castle

    # define the main game loop
    while True:
        # print the current room description
        for c in current_room["name"]:
            print(c, end="")
            time.sleep(0.05)
        print("")
        time.sleep(1)

        for c in current_room["description"]:
            print(c, end="")
            time.sleep(0.02)
        print("")
        time.sleep(1)

        # print the available paths
        print("Paths:")
        for exit in current_room["paths"]:
            print("- " + exit)

        # print the available items
        print("Items:")
        for item in current_room["items"]:
            print("- " + item)

        print("Battles:")
        for b in current_room["battles"]:
            print("- " + b)

        # get the player's input
        command = input("What do you want to do? ").title()

        # if the player wants to go to a different room, move them there
        if command in current_room["paths"]:
            if current_room["battles"] == []:
                current_room = globals()["room_" + command]
            else:
                print("\nThere is still an enemy in this area.\n")
                time.sleep(1)
        # if the player wants to take an item, add it to their inventory
        elif command in current_room["items"]:
            inventory.append(command)
            print("You picked up the " + command + ".")
            current_room["items"].remove(command)

        elif command in current_room["battles"]:
            if command == "Goblin":
                enemyNum = 1
            elif command == "Skeleton":
                enemyNum = 2
            elif command == "Slime":
                enemyNum = 3
            elif command == "Dragon":
                enemyNum = 4
            elif command == "Serpent":
                enemyNum = 5
            enemyGen()
            battle()
            if enemyHealth == 0:
                print("You defeated the " + command + ".")
                current_room["battles"].remove(command)
            else:
                print("You failed to defeat the", command)

        # inventory check
        elif command == "inventory":
            print(inventory)
        # if the player enters an invalid command, print an error message
        else:
            print("Invalid input")