from Llibreria.TCPClient_MINIMAL import TCPClient
import network
import time
import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import RFIDUnit
from base import Motion

# WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# 🔶 Change here:
wlan.connect('YOUR_WIFI_NAME', 'YOUR_WIFI_PASSWORD')

while not wlan.isconnected():
    time.sleep(0.5)

print('Client IP:', wlan.ifconfig()[0])

# Initialize screen and RFID reader
M5.begin()
Widgets.fillScreen(0x000000)
label0 = Widgets.Label("Waiting UID...", 0, 5, 1.2, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)

i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
rfid_0 = RFIDUnit(i2c0)

# Initialize Motion base
i2c1 = I2C(1, scl=Pin(39), sda=Pin(38), freq=100000)
motion = Motion(i2c1, 0x38)

# 🔶 Change here:
SERVER_IP = '192.168.1.XXX'

# UID to activate motor
motor_uid = 'F8A091D6'

# Main loop
while True:
    M5.update()

    if rfid_0.is_new_card_present():
        uid = rfid_0.read_card_uid()
        uid_str = ''.join('{:02X}'.format(b) for b in uid)
        uid_short = uid_str[:8]

        client = None
        try:
            client = TCPClient(host=SERVER_IP, port=5000)
            client.send_message(uid_str)
        except Exception as e:
            print("Error sending message:", e)
        finally:
            if client:
                client.close()

        label0.setText("UID:\n" + uid_short)

        if uid_short == motor_uid:
            motion.set_motor_speed(1, 127)
            time.sleep(5)
            motion.set_motor_speed(1, 0)

        time.sleep(0.5)
