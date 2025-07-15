import network
import time
import M5
from M5 import Widgets
from hardware import I2C, Pin, PWM
from unit import GlassUnit
from Llibreria.TCPServer_MINIMAL import TCPServer

# Diccionaris UID -> Shape i Solid
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

# Connexió WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MIWIFI_6hhP', 'T9A5XSDf')

while not wlan.isconnected():
    time.sleep(0.5)

print('Server IP:', wlan.ifconfig()[0])

# Inicialitza pantalla Glass
M5.begin()
i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
glass_0 = GlassUnit(i2c0, 0x3d)
Widgets.fillScreen(0x000000, glass_0)

label_uid = Widgets.Label("Waiting UID...", 0, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)
label_shape = Widgets.Label("", 0, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)
label_solid = Widgets.Label("", 0, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9, glass_0)

# Configura motor DC a la base Motion (PWM)
motor_pwm = PWM(Pin(2), freq=1000, duty=0)  # Pin 2 és el motor A de la Motion Base

def start_motor(duration=5):
    print("Motor activat!")
    motor_pwm.duty(512)  # 50% de potència
    time.sleep(duration)
    motor_pwm.duty(0)
    print("Motor aturat.")

# Servidor TCP
server = TCPServer(port=5000)

# Bucle principal del servidor
while True:
    print("Esperant connexió entrant...")
    conn, addr = server.sock.accept()
    print("Connexió acceptada des de", addr)

    try:
        data = conn.recv(1024)
        if data:
            uid_received = data.decode()
            print("Missatge rebut:", uid_received)

            uid_short = uid_received[:8]
            shape = shape_dict.get(uid_short, 'Unknown Shape')
            solid = solid_dict.get(uid_short, 'Unknown Solid')

            label_uid.setText("UID: " + uid_short)
            label_shape.setText("Shape: " + shape)
            label_solid.setText("Solid: " + solid)

            # Control del motor
            if uid_short == 'F8A091D6':
                start_motor(5)  # Motor activat 5 segons (pots ajustar)

    except Exception as e:
        print("Error en rebre:", e)

    print("Tancant connexió")
    conn.close()
