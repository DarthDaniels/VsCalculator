from objects import *
from functions import *

pygame.init()

user_input = ""
output = ""

fps = 60
clock = pygame.time.Clock()

active = True


while active:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    mp = pygame.mouse.get_pos()

    for field in fields_list:
        user_input += field.update(event, mp[0], mp[1])

    for elem in user_input:
        if elem == "C":
            user_input = ""
        if elem == "{":
            user_input = user_input[0: -2]
        if elem == "=":
            user_input = user_input[0:-1]
            user_input = res_output(user_input)

    print_output(user_input, 0, 100, screen, "images/cell_output.png")

    pygame.display.update()
    clock.tick(fps)
