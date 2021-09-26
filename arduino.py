from pyfirmata import Arduino, util
import time

board = Arduino('COM6')
it = util.Iterator(board)
it.start()

button_right = board.get_pin('d:3:i')
button_left = board.get_pin('d:4:i')


def check_button():
    return button_left.read(), button_right.read()

