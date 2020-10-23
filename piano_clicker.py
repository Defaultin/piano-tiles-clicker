from mss import mss
from pyautogui import click
from keyboard import is_pressed
from time import sleep
import numpy as np


def game(wait_time=5):
    x, y = 520, 560
    box = (x, y, x + 320, y + 1)
    coords = np.array([0, 100, 200, 300])

    sleep(wait_time)
    with mss() as shot:
        while not is_pressed('esc'):
            img = shot.grab(box)
            for c in coords:
                if img.pixel(c, 0)[0] < 100:
                    click(x + c, y)
                    break


if __name__ == '__main__':
    game()