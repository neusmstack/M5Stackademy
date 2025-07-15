
from m5stack import *
from m5ui import *
from uiflow import *
import unit

cardkb_0 = unit.get(unit.CARDKB, unit.PORTA)

def ask_input(prompt='Introdueix text:'):
    lcd.clear()
    lcd.setCursor(10, 10)
    lcd.print(prompt)
    user_input = ""
    lcd.setCursor(10, 40)
    while True:
        key = cardkb_0.get_key()
        if key:
            if key == '\r':  # Enter
                break
            user_input += key
            lcd.print(key)
    return user_input
