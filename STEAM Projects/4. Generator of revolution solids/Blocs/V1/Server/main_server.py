import network
import time
import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import GlassUnit
from Llibreria.TCPServer_MINIMAL import TCPServer

# UID dictionaries
shape_dict = {
    '181511D7': 'Circle',
    'DA7B39C3': 'Right Triangle',
    '186D52D7': 'Rectangle',
    'BACAB6C3': 'Trapezoid',
    'F8A091D6': 'Start Motor'
}

solid_dict = {
    '181511D7': 'Sphere',
    'DA7B39C3': 'Cone',
    '186D52D7': 'Cylinder',
    'BACAB6C3': 'Frustum',
    'F8A091D6': 'Motor ON'
}

# WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# 🔶 Change here:
wlan.connect('YOUR_WIFI_NAME', 'YOUR_WIFI_PASSWORD')

while not wlan.isconnected():
    time.sleep(0.5)

print('Server IP:', wlan.ifconfig()[0])

# Initialize Glass screen
M5.begin()
i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
glass_0 = GlassUnit(i2c0, 0x3d)
Widgets.fillScreen(0x000000, glass_0)

label_uid = Widgets.Label("Waiting UID...", 0, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)
label_shape = Widgets.Label("", 0, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)
label_solid = Widgets.Label("", 0, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)

server = TCPServer(port=5000)

# Main loop
while True:
    conn, addr = server.sock.accept()
    try:
        data = conn.recv(1024)
        if data:
            uid_received = data.decode()
            uid_short = uid_received[:8]
            shape = shape_dict.get(uid_short, 'Unknown Shape')
            solid = solid_dict.get(uid_short, 'Unknown Solid')

            label_uid.setText("UID: " + uid_short)
            label_shape.setText("Shape: " + shape)
            label_solid.setText("Solid: " + solid)

    except Exception as e:
        print("Error receiving message:", e)

    conn.close()
