import pyautogui
import keyboard


class PianoTiles:
    '''Python bot for Piano Tiles autoclicking'''
    def __init__(self):
        print('Welcome to the Piano Tiles Autoclicker! Press ESC to exit.')
        self.game_screen = self._game_screen()
        self.tiles = self._tiles_pos()


    def _game_screen(self):
        y = pyautogui.size()[1] // 2
        x1, y1 = self._mouse_pos('LEFT')
        while keyboard.is_pressed('enter'): pass
        x2, y2 = self._mouse_pos('RIGHT')
        x1, x2 = min(x1, x2), max(x1, x2)
        return [x1, y, x2, y + 1]


    def _mouse_pos(self, border):
        print(f'Place the cursor on the {border} border of the playing field and press ENTER:')
        x, y = 0, 0
        while not keyboard.is_pressed('enter') and not keyboard.is_pressed('esc'):
            x, y = pyautogui.position()
            position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(position, end='')
            print('\b' * len(position), end='', flush=True)

        print(f'{border} border: {x, y}')
        return x, y


    def _tiles_pos(self):
        start = self.game_screen[0]
        stop = self.game_screen[2] - start
        step = stop // 4
        return [(start + i, self.game_screen[1]) for i in range(step // 2, stop, step)]


    def _is_tile(self, pixel, threshold):
        color = pyautogui.pixel(*pixel)
        # return True if all([c < threshold for c in color]) else False
        return True if color[0] <= threshold else False


    def run(self, *, tile_rgb=10):
        while not keyboard.is_pressed('esc'):
            for pos in self.tiles:
                if self._is_tile(pos, tile_rgb):
                    pyautogui.click(*pos)
                    break
        

if __name__ == '__main__':
    PianoTiles().run()