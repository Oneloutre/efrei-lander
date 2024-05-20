import pygame


def guide_ui(screen, font):
    running = True
    guide_img = pygame.image.load("../Assets/guide.png").convert()
    while running:
        screen.blit(guide_img, (0, 0))
        play_text = font.render("Back", True, (0, 0, 0))
        play_rect = play_text.get_rect()
        play_rect.topleft = (580, 720 / 2)
        screen.blit(play_text, play_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_rect.collidepoint((mouse_x, mouse_y)):
            play_text = font.render("Back", True, (17, 119, 182))
            play_rect = play_text.get_rect()
            play_rect.topleft = (580, 720 / 2)
            screen.blit(play_text, play_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint((mouse_x, mouse_y)):
                    return "menu"
