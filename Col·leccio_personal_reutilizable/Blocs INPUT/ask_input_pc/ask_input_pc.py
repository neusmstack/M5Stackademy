import m5stack

# Funció per mostrar un prompt i capturar l'entrada del teclat
def ask_input(prompt):
    m5stack.lcd.clear()  # Esborrar la pantalla
    m5stack.lcd.print(prompt, 10, 10)  # Mostrar el prompt a la pantalla
    response = input()  # Esperar l'entrada de l'usuari
    return response

# Cridar la funció per fer una pregunta
result = ask_input("Quin és el teu nom?")

# Mostrar la resposta
m5stack.lcd.clear()
m5stack.lcd.print("La teva resposta és:", 10, 20)
m5stack.lcd.print(result, 10, 40)
