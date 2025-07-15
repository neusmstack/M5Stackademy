from machine import Pin, PWM
import time

# Configura el motor (Port 1 = Pin 2)
motor_pwm = PWM(Pin(2), freq=1000, duty=0)

# Activa el motor
print("Activant motor...")
motor_pwm.duty(512)  # 50% de potència

# Manté el motor en marxa 5 segons
time.sleep(5)

# Atura el motor
print("Aturant motor...")
motor_pwm.duty(0)
