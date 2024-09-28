import pygame
import sys
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définir la taille de la fenêtre
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()

# Charger les images
test_surface = pygame.image.load('prre pool day08/hangman/Sans titre.png')  # Chemin de l'image de fond
test_surface = pygame.transform.scale(test_surface, (600, 600))

button = pygame.image.load('prre pool day08/hangman/Red-Cross-Logo-768x768.png')  # Chemin de l'image du bouton
button = pygame.transform.scale(button, (40, 40))
button = pygame.transform.rotate(button,45)
button_rect = button.get_rect(topleft=(550, 10))

# Mots possibles pour le jeu
mots = [
    "absolut", "banque", "carotte", "deviser", "effacer", "formule", "galerie", "heureux", "illusion", "jardin"
]

randmoword = random.choice(mots)
word = randmoword.lower()

# Variables pour le jeu
correctletters = ''
guessletters = ''
penalty = 0

# Initialisation des polices
font = pygame.font.SysFont(None, 48)

# Dessiner le pendu
def drawman(screen, x, y, penalty):
    if penalty > 0:
        pygame.draw.circle(screen, BLACK, [x +20, y + 20], 20, 2)  # Tête
    if penalty > 1:
        pygame.draw.line(screen, BLACK, [x + 20, y + 40], [x + 20, y + 100], 2)  # Corps
    if penalty > 2:
        pygame.draw.line(screen, BLACK, [x + 20, y + 60], [x + 60, y + 80], 2)  # Bras droit
    if penalty > 3:
        pygame.draw.line(screen, BLACK, [x + 20, y + 60], [x - 20, y + 80], 2)  # Bras gauche
    if penalty > 4:
        pygame.draw.line(screen, BLACK, [x + 20, y + 100], [x + 40, y + 140], 2)  # Jambe droite
    if penalty > 5:
        pygame.draw.line(screen, BLACK, [x + 20, y + 100], [x, y + 140], 2)  # Jambe gauche

# Afficher les lettres devinées et les manquées
def display_word(screen, word, correctletters, guessletters):
    blanks = '_' * len(word)
    
    # Remplir les lettres devinées dans les espaces du mot
    for i in range(len(word)):
        if word[i] in correctletters:
            blanks = blanks[:i] + word[i] + blanks[i+1:]
    
    # Affichage du mot avec les lettres découvertes
    word_text = font.render(' '.join(blanks), True, BLACK)
    screen.blit(word_text, (150, 100))
    
    # Affichage des lettres manquées
    missed_text = font.render('Lettres ratées: ' + ' '.join(guessletters), True, BLACK)
    screen.blit(missed_text, (150, 550))

# Boucle principale du jeu
while True:
    screen.fill(WHITE)
    screen.blit(test_surface, (0, 0))
    screen.blit(button, (10, 10))

    # Dessiner le pendu selon les pénalités
    drawman(screen, 300, 150, penalty)
    
    # Afficher les lettres devinées et le mot partiellement complété
    display_word(screen, word, correctletters, guessletters)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        # Vérifier les événements de saisie de lettre par le joueur
        elif event.type == pygame.KEYDOWN:
            guess = chr(event.key).lower()
            if guess in word and guess not in correctletters:
                correctletters += guess
            elif guess not in word and guess not in guessletters:
                guessletters += guess
                penalty += 1

    # Vérifier si le joueur a gagné ou perdu
    if all([letter in correctletters for letter in word]):
        print('Félicitations, vous avez gagné!')
        pygame.time.wait(2000)
      
    elif penalty >= 6:  # Nombre maximum d'erreurs
        print('Désolé, vous avez perdu! Le mot était:', word)
        pygame.time.wait(2000)


    pygame.display.update()
    clock.tick(60)
