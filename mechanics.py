import random
from constants import *
import shared


def control_rocket(rocket):
    shoots = []
    for _, shoot in enumerate(rocket["shoots"]):
        # MOVE SHOOTS
        shoot = (shoot[0], shoot[1]-1)
        # DELETE IF OUTSIDE OF MAP
        if shoot[1] < 1:
            pass
        else:
            shoots.append(shoot)

    # CONTROL BORDERS
    # bottom
    if rocket["position"][1][1] == SCREEN_HEIGHT - 2 and rocket["direction"] == DIRECTIONS['down']:
        rocket["direction"] = DIRECTIONS['up']
    # top
    elif rocket["position"][0][1] == 1 and rocket["direction"] == DIRECTIONS['up']:
        rocket["direction"] = DIRECTIONS['down']
    # right
    elif rocket["position"][3][0] == SCREEN_WIDTH - 2 and rocket["direction"] == DIRECTIONS['right']:
        rocket["direction"] = DIRECTIONS['left']
    # left
    elif rocket["position"][1][0] == 1 and rocket["direction"] == DIRECTIONS['left']:
        rocket["direction"] = DIRECTIONS['right']


    # MOVE ROCKET
    rocket = {"position": [
        (rocket["position"][0][0] + rocket["direction"][0], rocket["position"][0][1] + rocket["direction"][1]),
        (rocket["position"][1][0] + rocket["direction"][0], rocket["position"][1][1] + rocket["direction"][1]),
        (rocket["position"][2][0] + rocket["direction"][0], rocket["position"][2][1] + rocket["direction"][1]),
        (rocket["position"][3][0] + rocket["direction"][0], rocket["position"][3][1] + rocket["direction"][1])],
        "shoots":  shoots,
        "direction": rocket["direction"]
        }
    return rocket


def generate_comets(comets, comets_counter):
    comets_counter = comets_counter - 1

    if comets_counter == 0:
        comet = []
        comet_core = (random.randrange(2, SCREEN_WIDTH - 2), 0)

        # BUILD COMET BODY
        comet = [comet_core, 
        (comet_core[0], comet_core[1]+1), 
        (comet_core[0], comet_core[1]-1),
        (comet_core[0]+1, comet_core[1]),
        (comet_core[0]-1, comet_core[1])
        ]

        comets.append(comet)
        comets_counter = COMETS_COUNTER

    return comets, comets_counter


def control_comets(comets, rocket):
    updated_comets = []

    for comet in comets:
        new_position = []
        for part_of_body in comet:
            # MOVE COMET
            new_pos_part_of_body = (part_of_body[0], part_of_body[1]+1)

            # DELETE COMET IF OUTSIDE OF MAP
            if part_of_body[1] > SCREEN_HEIGHT:
                pass
            # DESTROY COMET
            elif [shoot for shoot in rocket["shoots"] if shoot in comet]:
                shared.score = shared.score + 20
                pass
            # ROCKET CRASH
            elif [rocket for rocket in rocket["position"] if rocket in comet]:
                shared.game_status = 'GAME_OVER'
            else:
                new_position.append(new_pos_part_of_body)

        updated_comets.append(new_position)

    return updated_comets
    

def create_stars(stars):
    updated_stars = []
    if len(stars) == 0:
        # GENERATE NEW STARS
        for i in range(30):
            new_star = (random.randrange(2, SCREEN_WIDTH - 2), random.randrange(0, SCREEN_HEIGHT -  2))
            stars.append(new_star)
        updated_stars = stars
    else:
        new_star = (random.randrange(2, SCREEN_WIDTH - 2), 2)
        stars.append(new_star)
        for star in stars:
            # MOVE STAR
            star = (star[0], star[1]+1)
            # DELETE IF OUTSIDE OF MAP
            if star[1] > SCREEN_HEIGHT - 3:
                pass
            else:
                updated_stars.append(star)

    return updated_stars


def render(CELLS, SCREEN_WIDTH, SCREEN_HEIGHT, rocket, comets, stars):
    shared.score = shared.score + 1

    for cell in CELLS:
        # BUILD ROCKET
        if cell in rocket["position"]:
            print('$', end='')
        # BUILD SHOOTS
        elif cell in rocket["shoots"]:
            print('*', end='')
        # BUILD
        elif [cell for comet in comets if cell in comet]:
            print('0', end='')
        # BUILD STARS
        elif cell in stars:
            print('`', end='')
        # BUILD FIELD
        elif cell[0] in (0, SCREEN_WIDTH - 1) or cell[1] in (0, SCREEN_HEIGHT - 1):
            print('#', end='')
        else:
            print(' ', end='')
        if cell[0] == SCREEN_WIDTH - 1:
            print('')



