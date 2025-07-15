from m5core2 import lcd  # Mòdul correcte per al M5Core2
import time

# Funció per mostrar text a la pantalla
def mostrar_text(text):
    lcd.clear()  # Neteja la pantalla abans de mostrar el text
    lcd.text(20, 40, text, lcd.WHITE)  # Mostra el text a les coordenades (20, 40)

# Prova del bloc amb un missatge
mostrar_text("Hola, Neus!")
time.sleep(5)  # Manté el missatge durant 5 segons
