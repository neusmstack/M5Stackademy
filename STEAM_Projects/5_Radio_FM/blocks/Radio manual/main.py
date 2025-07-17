import M5
from M5 import Widgets
from hardware import I2C, Pin
from unit import PAHUBUnit, ByteButtonUnit, AngleUnit
import time

# Inicialització M5 i pantalla
M5.begin()
Widgets.setRotation(1)
Widgets.fillScreen(0x000000)

label0 = Widgets.Label("label0", 10, 30, 1.0, 0x00FF00, 0x000000, Widgets.FONTS.DejaVu18)

# Inicialització I2C i PaHUB
i2c0 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
pahub_0 = PAHUBUnit(i2c=i2c0)

# Dispositius
pahub_0.select_channel(5)
bytebutton_0 = ByteButtonUnit(pahub_0, 0x47)
pahub_0.release_channel(5)

angle_0 = AngleUnit((36, 26))  # AngleUnit connectat a Port B

freq_actual_anterior = 0

# Bucle principal
while True:
    M5.update()

    angle_value = angle_0.get_value()
    freq_MHZ = 87.5 + (angle_value / 65535) * (108.0 - 87.5)

    if abs(freq_MHZ - freq_actual_anterior) >= 0.05:
        pll = int(((freq_MHZ + 0.225) * 1_000_000) / 8192)
        freq = bytearray(5)
        freq[0] = pll >> 8
        freq[1] = pll & 255
        freq[2] = 0xB0
        freq[3] = 0x10
        freq[4] = 0x00

        pahub_0.select_channel(0)
        i2c0.writeto(96, freq, True)
        pahub_0.release_channel(0)

        label0.setText('Tuning: {:.1f} MHz'.format(freq_MHZ))

        freq_actual_anterior = freq_MHZ

    time.sleep(0.1)
