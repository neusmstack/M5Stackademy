import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import PAHUBUnit, ByteButtonUnit
import time

# Inicialització M5 i pantalla
M5.begin()
Widgets.setRotation(1)
Widgets.fillScreen(0x000000)
label_mode = Widgets.Label("label_mode", 10, 20, 1.0, 0x00FF00, 0x000000, Widgets.FONTS.DejaVu12)
label_mode.setText("Mode Digital (Control per ByteButton)")


# Etiqueta única (mida reduïda)
label_freq = Widgets.Label("label_freq", 10, 60, 1.8, 0x00FF00, 0x000000, Widgets.FONTS.DejaVu24)

# I2C i PaHUB
i2c0 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
pahub_0 = PAHUBUnit(i2c=i2c0)

# ByteButton
pahub_0.select_channel(5)
bytebutton_0 = ByteButtonUnit(pahub_0, 0x47)
bytebutton_0.set_indicator_color(0x00FF00)  # Verd: mode autoscan actiu
pahub_0.release_channel(5)

# Variables
freq_actual = 87.50
freq_anterior = freq_actual
pas = 0.05

# Funcions
def mostrar_frequencia():
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

# Inicialització
mostrar_frequencia()
escriure_frequencia()

# Bucle principal
while True:
    M5.update()

    pahub_0.select_channel(5)
    status = bytebutton_0.get_byte_button_status()
    pahub_0.release_channel(5)

    boto_premut = None
    for boto in range(8):
        if (status & (1 << boto)) == 0:
            boto_premut = boto

    if boto_premut == 0:
        freq_actual = min(freq_actual + pas, 108.0)
    elif boto_premut == 7:
        freq_actual = max(freq_actual - pas, 87.5)

    if abs(freq_actual - freq_anterior) >= pas:
        escriure_frequencia()
        freq_anterior = freq_actual

    mostrar_frequencia()
    time.sleep(0.2)
