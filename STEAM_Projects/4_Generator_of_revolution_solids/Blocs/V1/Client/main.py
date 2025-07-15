from Llibreria.TCPClient_MINIMAL import TCPClient
import network
import time
import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import RFIDUnit
from base import Motion

# Configura connexió WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MIWIFI_6hhP', 'T9A5XSDf')

while not wlan.isconnected():
    time.sleep(0.5)

print('Client IP:', wlan.ifconfig()[0])

# Inicialitza pantalla i RFID
M5.begin()
Widgets.fillScreen(0x000000)
label0 = Widgets.Label("Waiting UID...", 0, 5, 1.2, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)

i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
rfid_0 = RFIDUnit(i2c0)

# Inicialitza base Motion
i2c1 = I2C(1, scl=Pin(39), sda=Pin(38), freq=100000)
motion = Motion(i2c1, 0x38)

# UID d'activació del motor
motor_uid = 'F8A091D6'

# Bucle principal
while True:
    M5.update()
    print("Esperant targeta...")

    if rfid_0.is_new_card_present():
        print("Targeta detectada!")

        uid = rfid_0.read_card_uid()
        uid_str = ''.join('{:02X}'.format(b) for b in uid)
        uid_short = uid_str[:8]

        print('UID llegida:', uid_str)

        # Envia UID al servidor
        client = None
        try:
            client = TCPClient(host='192.168.1.151', port=5000)
            client.send_message(uid_str)
            print("Missatge enviat al servidor.")
        except Exception as e:
            print("Error enviant el missatge:", e)
        finally:
            if client:
                client.close()

        # Mostra UID a la pantalla
        label0.setText("UID:\n" + uid_short)

        # Activa motor si la targeta és la d'activació
        if uid_short == motor_uid:
            print("Activant motor des del client!")
            motion.set_motor_speed(1, 127)
            time.sleep(5)
            motion.set_motor_speed(1, 0)
            print("Motor aturat.")

        time.sleep(0.5)
