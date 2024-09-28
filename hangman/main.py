import pygame
import sys
import random


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#taille de la fenêtre
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()

# Charger les images
test_surface = pygame.image.load('hangman/Sans titre.png')
test_surface = pygame.transform.scale(test_surface, (600, 600))

win = pygame.image.load('hangman/you-win-video-game-vector.jpg')
win = pygame.transform.scale(win, (600, 600))
lose = pygame.image.load('hangman/you  win titre.png')
lose = pygame.transform.scale(lose, (600, 600))
button = pygame.image.load('hangman/215-2155436_png-file-svg-cross-mark-png-black.png')
button = pygame.transform.scale(button, (40, 40))
button_rect = button.get_rect(topleft=(550, 10))

# Liste des mots
mots = [
    "absolut", "banque", "carotte", "deviser", "effacer", "formule", "galerie", "heureux", "illusion",
    "jardin", "kiwi", "limite", "monstre", "noir", "orange", "pomme", "quitter", "ramasser", "sourire",
    "tenir", "unique", "vague", "wagon", "xylophone", "yaourt", "zenith", "abeille", "balle", "cible",
    "douleur", "enfer", "fete", "gouter", "heros", "insecte", "joie", "karate", "lampe", "maison", "navire",
    "orage", "piano", "quiche", "rivage", "saison", "temple", "utile", "vinyle", "weekend", "xerox", "yoga",
    "zebre", "avion", "bateau", "chat", "dent", "eclair", "fable", "glace", "horizon", "iguane", "jouer",
    "kayak", "lion", "mur", "neige", "outil", "plume", "quai", "route", "soleil", "table", "univers", "voiture",
    "wagon", "xenon", "yeux", "zoo", "acier", "banane", "citron", "drapeau", "etoile", "fleur", "guitare",
    "histoire", "ile", "jouet", "kilo", "lac", "montagne", "nuage", "ombre", "plage", "queue", "rever", "sable",
    "tempete", "usage", "vent", "wagon", "xylophone", "yeti", "zero", "arc", "bal", "coup", "dur", "espace",
    "feu", "guerre", "heure", "idee", "jeu", "kilt", "lune", "mot", "nuit", "oeil", "pain", "quatre", "rideau",
    "serpent", "tigre", "urine", "vol", "wagon", "xenon", "yeti", "zinc", "animal", "bateau", "cloche", "dessin",
    "elephant", "fenetre", "grandeur", "humour", "image", "joie", "koala", "lait", "maree", "nuage"
]

# Variables
correctletters = ''
guessletters = ''
penalty = 0

font = pygame.font.SysFont("simsun", 48)

# dessiner le pendu
def drawman(screen, x, y, penalty):
    if penalty > 0:
        hat =pygame.image.load('hangman/pixel-art-style-18-bit-style-straw-hat-vector.jpg')
        hat.blit(hat,[x,y-10])
        pygame.draw.circle(screen, BLACK, [x, y], 10, 2)  # Tête
    if penalty > 1:
        pygame.draw.line(screen, BLACK, [x, y + 10], [x, y + 50], 2)  # Corps
    if penalty > 2:
        pygame.draw.line(screen, BLACK, [x, y + 20], [x + 20, y + 10], 2)  # Bras droit
    if penalty > 3:
        pygame.draw.line(screen, BLACK, [x, y + 20], [x - 20, y + 10], 2)  # Bras gauche
    if penalty > 4:
        pygame.draw.line(screen, BLACK, [x, y + 50], [x + 20, y + 70], 2)  # Jambe droite
    if penalty > 5:
        pygame.draw.line(screen, BLACK, [x, y + 50], [x - 20, y + 70], 2)  # Jambe gauche
    if penalty == 6:
        pygame.draw.line(screen, WHITE, [x, y + 50], [x - 20, y + 70], 2)
        pygame.draw.line(screen, WHITE, [x, y + 50], [x + 20, y + 70], 2)
        pygame.draw.line(screen, WHITE, [x, y + 20], [x - 20, y + 10], 2)
        pygame.draw.line(screen, WHITE, [x, y + 20], [x + 20, y + 10], 2)
        pygame.draw.line(screen, BLACK, [x, y + 20], [x + 10, y + 40], 2)  #mort
        pygame.draw.line(screen, BLACK, [x, y + 20], [x - 10, y + 40], 2) 
        pygame.draw.line(screen, BLACK, [x, y + 50], [x - 5, y + 80], 2)
        pygame.draw.line(screen, BLACK, [x, y + 50], [x + 5, y + 80], 2)

# afficher le mot deviné et les lettres manquées
def display_word(screen, word, correctletters, guessletters):
    blanks = '_' * len(word)

    for i in range(len(word)):
        if word[i] in correctletters:
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    #  mot deviné
    word_text = font.render(' '.join(blanks), True, BLACK)
    screen.blit(word_text, (150, 100))

    # lettres manquées
    missed_text = font.render('Missed letters: ' + ' '.join(guessletters), True, BLACK)
    screen.blit(missed_text, (150, 150))

# Fonction de jeu
def jeu(correctletters, guessletters, penalty):
    randomword = random.choice(mots)
    word = randomword.lower()

    while True:
        screen.fill(WHITE)
        screen.blit(test_surface, (0, 0))
        screen.blit(button, (550, 10))

        # Dessiner le pendu
        drawman(screen, 300, 240, penalty)

        # Afficher le mot et les lettres manquées
        display_word(screen, word, correctletters, guessletters)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                guess = chr(event.key).lower()
                if guess in word and guess not in correctletters:
                    correctletters += guess
                elif guess not in word and guess not in guessletters:
                    guessletters += guess
                    penalty += 1

        # joueur a gagné
        if all(letter in correctletters for letter in word):
            pygame.time.wait(500)

            screen.blit(win, (0, 0))
            pygame.display.update()
            pygame.time.wait(2000)
            main_menu()

        # joueur a perdu
        elif penalty >= 7:
            pygame.time.wait(500)
            screen.blit(lose, (0, 0))
            pygame.display.update()
            pygame.time.wait(2000)
            main_menu()

   
        pygame.display.update()
        clock.tick(60)

#  menu
def drawmenu(surface):
    start = pygame.image.load('hangman/EKb5.png')
    start = pygame.transform.scale(start, (600, 600))
    start_rect = start.get_rect()
    surface.blit(start, start_rect)
    return start_rect

# menu principal
def main_menu():
    start_rect = drawmenu(screen)
    while True:
        screen.fill(WHITE)
        drawmenu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):  # Commencer une nouvelle partie
                    jeu(correctletters, guessletters, penalty)

        pygame.display.update()

main_menu()
