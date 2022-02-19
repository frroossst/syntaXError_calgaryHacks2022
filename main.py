# Imported modules and libraries
import pygame



# Constants
WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
FPS = 60

# Window settings
pygame.display.set_caption("Tracker Beta")


# Main program
def main():

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()
    


if __name__ == "__main__":
    main()