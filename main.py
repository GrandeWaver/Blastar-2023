import os
from beep import sos, start_procedure
from introduction import introduction
from modules import configure_terminal_size, nice_print
from mechanics import control_rocket, control_comets, create_stars, generate_comets, render
from constants import *
from pytimedinput import timedInput
import shared

# LOADING ANIMATION
from loading import printProgressBar


CELLS = [(col, row) for row in range(SCREEN_HEIGHT) for col in range(SCREEN_WIDTH)]


def main():
    nice_print("BLASTAR 2023 by Kacper Machaj\n\n", 0.01)
    introduction()
    start_procedure()

    configure_terminal_size()

    # GAME
    while True:
        # DEFAULT PARAMETERS FOR ROCKET
        rocket = {"position": [(SCREEN_WIDTH//2, SCREEN_HEIGHT-4), (SCREEN_WIDTH//2-1, SCREEN_HEIGHT-3), (SCREEN_WIDTH//2, SCREEN_HEIGHT-3), (SCREEN_WIDTH//2+1, SCREEN_HEIGHT-3)],
            "shoots": [], "direction": DIRECTIONS['up']}

        # DEFAULT PARAMETERS FOR COMETS
        comets = []
        comets_counter = COMETS_COUNTER
        stars = []

        while not shared.game_status == 'GAME_OVER':
            rocket = control_rocket(rocket)
            comets, comets_counter = generate_comets(comets, comets_counter)
            comets = control_comets(comets, rocket)
            stars = create_stars(stars)

            os.system('cls')
            render(CELLS, SCREEN_WIDTH, SCREEN_HEIGHT, rocket, comets, stars)

            print(f'SCORE: {shared.score}', end='\n')

            input, _ = timedInput('', timeout = .005)
            
            match input:
                case 'w': rocket["direction"] = DIRECTIONS['up']
                case 's': rocket["direction"] = DIRECTIONS['down']
                case 'a' : rocket["direction"] = DIRECTIONS['left']
                case 'd': rocket["direction"] = DIRECTIONS['right']
                case ' ': rocket["shoots"].append((rocket["position"][0][0], rocket["position"][0][1]-1))

                case 'q': 
                    os.system('cls')    
                    break

        sos()
        nice_print('GAME OVER', 0.01)
        nice_print('\nPRESS ENTER TO PLAY AGAIN', 0.01)
        nice_print('\nPRESS q to QUIT\n', 0.01)
        input, _ = timedInput('', timeout = 20)

        if input == 'q':
            break
        else:
            shared.game_status = 'PLAY'
    return 0

if __name__ == "__main__":
    main()