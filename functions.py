import pygame
import math


def res_output(user_input):
    elem = ""
    list_elm = []

    for i in user_input:
        if i != "+" and i != "-" and i != "#" and i != "@" and i != "R":
            elem += i
        else:
            list_elm.append(elem)
            list_elm.append(i)
            elem = ""

    list_elm.append(elem)

    for i2 in range(len(list_elm)-1):
        if list_elm[i2] == "":
            list_elm.remove(list_elm[i2])
        if not "" in list_elm:
            break

    while True:
        if "R" in list_elm:
            for elem in range(len(list_elm) - 1):
                if list_elm[elem] == "R":
                    list_elm[elem+1] = math.sqrt(float(list_elm[elem+1]))
                    list_elm.remove(list_elm[elem])
                    break

        elif "@" in list_elm or "#" in list_elm:
            for elem in range(len(list_elm)-1):
                if list_elm[elem] == "@":
                    list_elm[elem-1] = float(list_elm[elem-1])*float(list_elm[elem+1])

                    list_elm.remove(list_elm[elem])
                    list_elm.remove(list_elm[elem])
                    break
                elif list_elm[elem] == "#":
                    if list_elm[elem + 1] == "0" or list_elm[elem + 1] == "0.0":
                        return ""
                    list_elm[elem - 1] = float(list_elm[elem - 1]) / float(list_elm[elem + 1])
                    list_elm.remove(list_elm[elem])
                    list_elm.remove(list_elm[elem])
                    break

        elif "+" in list_elm or "-" in list_elm:

            for elem in range(len(list_elm)-1):
                if list_elm[elem] == "+":
                    list_elm[elem - 1] = float(list_elm[elem - 1]) + float(list_elm[elem + 1])

                    list_elm.remove(list_elm[elem])
                    list_elm.remove(list_elm[elem])
                    break
                elif list_elm[elem] == "-":
                    list_elm[elem - 1] = float(list_elm[elem - 1]) - float(list_elm[elem + 1])
                    list_elm.remove(list_elm[elem])
                    list_elm.remove(list_elm[elem])
                    break
        else:
            break

    return str(list_elm[0])


def print_output(user_input, x, y, screen, cell_img):
    img = pygame.image.load(cell_img).convert_alpha()

    screen.blit(img, (x, y))

    ui = user_input[::-1]

    if len(ui) > 0:
        for count in range(len(ui)):
            show = pygame.image.load(f"images/{ui[count]}.png")

            screen.blit(show, (x+320-20*count, y))
