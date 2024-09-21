"""
TO USE: open crafting table and search the exact item you want to mass craft
then run script, switch to Minecraft and unpause

Can change amount on line 20
"""

# First Craft item: (330, 300)
# Output: (1155, 300)

# Villager middle trade: (495, 445)
# Villager first trade: (480, 255)
# Villager Output: (1055, 307)
import time
import pynput.mouse
import pynput.keyboard

def craft(pos1: tuple = (330, 300), pos2: tuple = (1155, 300)):
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()

    with keyboard.pressed(pynput.keyboard.Key.shift):

        for _ in range(10):
            time.sleep(0.1)
            single_craft(mouse, pos1, pos2)
        
        time.sleep(0.1)
        left_click(mouse)


def single_craft(mouse, pos1, pos2):
    mouse.position = pos1
    left_click(mouse)

    time.sleep(0.1)

    mouse.position = pos2
    left_click(mouse)


def left_click(mouse):
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)


def query_mouse_location():
    mouse = pynput.mouse.Controller()
    print(f'Mouse Position: {mouse.position}')


def alt_tab():
    keyboard = pynput.keyboard.Controller()

    with keyboard.pressed(pynput.keyboard.Key.alt):
        keyboard.press(pynput.keyboard.Key.tab)
        keyboard.release(pynput.keyboard.Key.tab)


def trade(slot: int = 4):
    slot_coords = {1: (480, 255), 
                   4: (495, 445)}
    craft(slot_coords[slot], (1055, 307))


if __name__ == '__main__':
    alt_tab()
    time.sleep(0.1)
    craft()
    #trade(4)

