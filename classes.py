import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y, name, cell_img, screen):
        super().__init__()
        self.name = name
        self.mean_img = pygame.image.load(f"images/{self.name}.png").convert_alpha()
        self.cell_img = pygame.image.load(cell_img).convert_alpha()
        self.rect = self.cell_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.btn_click_check = False

    def update(self, event, mx, my):
        self.screen.blit(self.cell_img, (self.rect.x, self.rect.y))
        self.screen.blit(self.mean_img, (self.rect.x, self.rect.y))

        if self.rect.left < mx < self.rect.right and self.rect.top < my < self.rect.bottom:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.btn_click_check = True
            if self.btn_click_check and event.type == pygame.MOUSEBUTTONUP:
                self.btn_click_check = False
                return self.name

        return ""

