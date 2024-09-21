"""
Module used for holding down A, S and right click to build pyramid
"""
import pynput.keyboard
import pynput.mouse



class Builder:
    def __init__(self):
        self.B_key = pynput.keyboard.KeyCode.from_char('b')
        self.building = False

        self.build()


    def build(self):
        while True:
            with pynput.keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()


    def on_press(self, key):
        mouse = pynput.mouse.Controller()
        keyboard = pynput.keyboard.Controller()

        if key == self.B_key:
            if self.building:
                release_buttons(mouse, keyboard)
                self.building = False

            else:
                hold_buttons(mouse, keyboard)
                self.building = True


def hold_buttons(mouse: pynput.mouse.Controller, keyboard: pynput.keyboard.Controller):
    keyboard.press('a')
    keyboard.press('s')
    mouse.press(pynput.mouse.Button.right)
    

def release_buttons(mouse: pynput.mouse.Controller, keyboard: pynput.keyboard.Controller):
    keyboard.release('a')
    keyboard.release('s')
    mouse.release(pynput.mouse.Button.right)


if __name__ == '__main__':
    Builder()
