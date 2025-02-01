import pygame 
import os
import random
import math

# SETTING UP DISPLAY

pygame.init()
WIDTH , HEIGHT = 1280, 720
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HANGMAN !")

# COLORS

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (168, 169, 169)
BLACK = (0,0,0)
LIGHT_GRAY = (211,211,211)


# BUTTONS VERIABLES

RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP) * 13) / 2)
starty = 550
A = 65 # ASCII TABLE

number_buttons = round((WIDTH - (RADIUS*2 + GAP) * 13) / 2)

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2+ GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A+i), True])


# HINT BUTTON VARIABLES
HINT_BUTTON_WIDTH = 100
HINT_BUTTON_HEIGHT = 40
HINT_BUTTON_X = WIDTH - HINT_BUTTON_WIDTH - 20
HINT_BUTTON_Y = 20


# FONTS

LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# SOUNDS

WIN_SOUND = pygame.mixer.Sound("sounds/win.mp3")
LOSE_SOUND = pygame.mixer.Sound("sounds/lose.mp3")


# IMAGES 

images = []
for i in range(7):
    image = pygame.image.load(os.path.join("assets","asma"+ str(i)+".png"))
    images.append(image)

ICON_PIC = pygame.image.load(os.path.join("giriş.png"))
BACKGROUND = pygame.image.load(os.path.join("background.jpg"))

# GAME 

mistakes = 0

words =  ["Canada", "Italy", "Brazil", "France", "Japan", "India", "Australia", "Mexico", "Germany", "Java", "Python", "JavaScript", "Developer", "Tomato", "Potato", "Apple", "Strawberry", "Aubergine", "Fork", "Toothbrush", "Clock", "Chair", "Carpet", "Television","Kazakhstan", "Azerbaijan", "Kyrgyzstan", "Bhutan", "Uzbekistan", "Senegal", "Tajikistan", "Luxembourg", "BackEnd", "FrontEnd", "Assembly", "Network", "Sunflower", "Cactus", "Rose", "Daisy", "Lavender", "Refrigerator", "Computer", "Backpack", "Umbrella", "Headphones"]


def choose_word():
    return random.choice(words).upper()

score = 100


word = choose_word()

guessed = []

score_img = LETTER_FONT.render(f"Score : {score}", True, BLACK)


# SETTING UP GAME LOOP


    

def draw():
    win.blit(BACKGROUND,(0,0))
    # DRAWINT TITLE
    icon = pygame.display.set_icon(ICON_PIC)
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width()/2, 20))
    win.blit(score_img, (WIDTH// 2 + score_img.get_width() // 2 + 30, 110))

    # DRAWING WORD
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " " 
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (450, 270))




    # Buttons
    for letter in letters:
        x,y, ltr, visible = letter 
        if visible:
            pygame.draw.circle(win,WHITE, (x,y), RADIUS,3)
            text = LETTER_FONT.render(ltr , 1, WHITE)
            win.blit(text,(x - text.get_width()/2, y - text.get_height()/ 2))

    win.blit(images[mistakes],(150,145))
    pygame.display.update() # UPDATING DISPLAY MANUALLY


def display_message(message):
    
    win.blit(BACKGROUND, (0,0))
    text = WORD_FONT.render(message, 1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width() / 2, HEIGHT/2 - text.get_height()/ 2))
    pygame.display.update()
    pygame.time.delay(3000)
    


FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            mistakes += 1
                            score -= 10
                            score_img = LETTER_FONT.render(f"Score : {score}", True, BLACK)
            # Check if the hint button is clicked
            if HINT_BUTTON_X < m_x < HINT_BUTTON_X + HINT_BUTTON_WIDTH and HINT_BUTTON_Y < m_y < HINT_BUTTON_Y + HINT_BUTTON_HEIGHT:
                if len(guessed) < len(word):
                    unrevealed_letters = [letter for letter in word if letter not in guessed]
                    random_letter = random.choice(unrevealed_letters)
                    guessed.append(random_letter)
                    # You can add additional logic here if needed

    draw()
    
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        WIN_SOUND.play()
        display_message(f"YOU WON!, YOUR SCORE IS : {score}")
        break

    if mistakes == 6:
        LOSE_SOUND.play()
        display_message("YOU LOST!, YOUR SCORE IS : 0")
        display_message(f"CORRECT WORD WAS : {word}")
        break

pygame.quit()
