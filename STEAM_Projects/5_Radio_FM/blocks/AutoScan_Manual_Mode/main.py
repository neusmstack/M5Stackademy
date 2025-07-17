import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import PAHUBUnit, ByteButtonUnit, AngleUnit
import time

# Inicialització M5 i pantalla
M5.begin()
Widgets.setRotation(1)
Widgets.fillScreen(0xFFFFFF)

# Etiquetes
label_title = Widgets.Label("label_title", 10, 10, 1.5, 0xFF0000, 0xFFFFFF, Widgets.FONTS.DejaVu18)
label_info = Widgets.Label("label_info", 10, 40, 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu12)
label_freq = Widgets.Label("label_freq", 40, 80, 2.2, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu24)

label_mem = []
for i in range(5):
    label = Widgets.Label("label_mem_{}".format(i), 10, 140 + (i * 20), 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu12)
    label_mem.append(label)

# I2C i PaHUB
i2c0 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
pahub_0 = PAHUBUnit(i2c=i2c0)

# ByteButton i AngleUnit
pahub_0.select_channel(5)
bytebutton_0 = ByteButtonUnit(pahub_0, 0x47)
pahub_0.release_channel(5)

angle_0 = AngleUnit((36, 26))

# Variables
freq_actual = 87.5
step = 0.05
mode = 'menu'
emissores_guardades = []

# Funcions
def mostrar_menu():
    Widgets.fillScreen(0xFFFFFF)
    label_title.setText("Select Mode")
    label_info.setText("Btn 0 = Manual / Btn 7 = AutoScan")
    pahub_0.select_channel(5)
    bytebutton_0.set_indicator_color(0x000000)
    pahub_0.release_channel(5)

def mostrar_freq():
    label_freq.setText('{:.2f} MHz'.format(freq_actual))

def escriure_frequencia():
    pll = int(((freq_actual + 0.225) * 1_000_000) / 8192)
    freq_bytes = bytearray(5)
    freq_bytes[0] = pll >> 8
    freq_bytes[1] = pll & 255
    freq_bytes[2] = 0b10110000
    freq_bytes[3] = 0b00010000
    freq_bytes[4] = 0
    pahub_0.select_channel(0)
    i2c0.writeto(96, freq_bytes, True)
    pahub_0.release_channel(0)

def actualitzar_led():
    pahub_0.select_channel(5)
    if mode == 'manual':
        bytebutton_0.set_indicator_color(0xFF0000)  # Vermell
    elif mode == 'autoscan':
        bytebutton_0.set_indicator_color(0x0000FF)  # Blau
    else:
        bytebutton_0.set_indicator_color(0x000000)
    pahub_0.release_channel(5)

def mostrar_emissores_guardades():
    for idx in range(5):
        if idx < len(emissores_guardades):
            label_mem[idx].setText("Btn {}: {:.2f} MHz".format(idx + 2, emissores_guardades[idx]))
        else:
            label_mem[idx].setText("Btn {}: Empty".format(idx + 2))

# Programa principal
mostrar_menu()

tic_tac_counter = 0

while True:
    M5.update()

    pahub_0.select_channel(5)
    status = bytebutton_0.get_byte_button_status()
    pahub_0.release_channel(5)

    boto_premut = None
    for boto in range(8):
        if (status & (1 << boto)) == 0:
            boto_premut = boto
            break

    if mode == 'menu':
        if boto_premut == 0:
            mode = 'manual'
            Widgets.fillScreen(0xFFFFFF)
            label_title.setText("Mode: Manual")
            actualitzar_led()
        elif boto_premut == 7:
            mode = 'autoscan'
            Widgets.fillScreen(0xFFFFFF)
            label_title.setText("Mode: AutoScan")
            actualitzar_led()

    elif mode == 'manual':
        angle_value = angle_0.get_value()
        freq_actual = 87.5 + (angle_value / 65535) * (108.0 - 87.5)
        mostrar_freq()
        escriure_frequencia()
        mostrar_emissores_guardades()

    elif mode == 'autoscan':
        if boto_premut == 0:
            freq_actual = min(freq_actual + step, 108.0)
        elif boto_premut == 7:
            freq_actual = max(freq_actual - step, 87.5)
        elif boto_premut == 1:
            if freq_actual not in emissores_guardades and len(emissores_guardades) < 5:
                emissores_guardades.append(freq_actual)
        # Recuperació de memòria:
        for idx in range(5):
            if boto_premut == idx + 2 and idx < len(emissores_guardades):
                freq_actual = emissores_guardades[idx]

        mostrar_freq()
        tic_tac_counter = (tic_tac_counter + 1) % 4  # Ralentitza el "tic-tac"
        if tic_tac_counter == 0:
            escriure_frequencia()
        mostrar_emissores_guardades()

    time.sleep(0.05)
