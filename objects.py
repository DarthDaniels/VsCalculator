from classes import *

sc_w = 400
sc_h = 700

screen = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("VsCalculator - v.1.2.8")
icon = pygame.image.load("images/icon.png")

pygame.display.set_icon(icon)

field_1 = Field(sc_w - 400, sc_h - 200, "1", "images/cell.png", screen)
field_2 = Field(sc_w - 300, sc_h - 200, "2", "images/cell.png", screen)
field_3 = Field(sc_w - 200, sc_h - 200, "3", "images/cell.png", screen)
field_4 = Field(sc_w - 400, sc_h - 300, "4", "images/cell.png", screen)
field_5 = Field(sc_w - 300, sc_h - 300, "5", "images/cell.png", screen)
field_6 = Field(sc_w - 200, sc_h - 300, "6", "images/cell.png", screen)
field_7 = Field(sc_w - 400, sc_h - 400, "7", "images/cell.png", screen)
field_8 = Field(sc_w - 300, sc_h - 400, "8", "images/cell.png", screen)
field_9 = Field(sc_w - 200, sc_h - 400, "9", "images/cell.png", screen)
field_0 = Field(sc_w - 300, sc_h - 100, "0", "images/cell.png", screen)

field_plus = Field(sc_w - 100, sc_h - 300, "+", "images/cell.png", screen)
field_minus = Field(sc_w - 100, sc_h - 400, "-", "images/cell.png", screen)
field_multiplication = Field(sc_w - 200, sc_h - 500, "@", "images/cell.png", screen)
field_division = Field(sc_w - 300, sc_h - 500, "#", "images/cell.png", screen)

field_root_2 = Field(sc_w - 400, sc_h - 100, "R", "images/cell.png", screen)

field_C = Field(sc_w - 400, sc_h - 500, "C", "images/cell.png", screen)
field_del = Field(sc_w - 100, sc_h - 500, "{", "images/cell.png", screen)
field_equality = Field(sc_w - 100, sc_h - 200, "=", "images/cell_=.png", screen)

field_comma = Field(sc_w - 200, sc_h - 100, ".", "images/cell.png", screen)

fields_list = [field_1, field_2, field_3,
               field_4, field_5, field_6,
               field_7, field_8, field_9,
               field_0,
               field_plus,
               field_minus,
               field_division,
               field_multiplication,
               field_C, field_del, field_equality, field_comma, field_root_2]
