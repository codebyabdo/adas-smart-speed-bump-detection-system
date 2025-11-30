import time

# -------------- HARDWARE MOCKS --------------- #
USE_PICO = False  # Change to True when running on Pico

if USE_PICO:
    from machine import Pin, I2C
    import mpu6050
    from lcd_api import LcdApi
    from pico_i2c_lcd import I2cLcd
else:
    # Mock classes for PC testing
    class Pin:
        OUT = 0
        IN = 1
        PULL_UP = 1
        def __init__(self, pin, mode=None, pull=None): pass
        def value(self, val=None): return 1

    class I2C:
        def __init__(self, id, scl, sda, freq=100000): pass
        def scan(self): return [0x27]

    class mpu6050:
        class accel:
            def __init__(self, i2c): pass
            def get_values(self):
                import random
                return {"Az": random.uniform(0, 20)}  # Simulate bump

    class I2cLcd:
        def __init__(self, i2c, addr, rows, cols): pass
        def clear(self): pass
        def putstr(self, s): print("[LCD]", s)

# -------- CONFIGURATION -------- #
USE_BUTTON_SIM = True
BUMP_THRESHOLD = 14
FAKE_GPS = (30.112233, 31.445566)

# -------- INITIALIZE DEVICES -------- #
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd_addr = i2c.scan()[0]
lcd = I2cLcd(i2c, lcd_addr, 2, 16)
mpu = mpu6050.accel(i2c)

buzzer = Pin(15, Pin.OUT)
led = Pin(14, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

def alert_bump():
    lcd.clear()
    lcd.putstr("  BUMP ALERT!\nSaving GPS...")
    led.value(1)
    buzzer.value(1)

    print("BUMP -> GPS:", FAKE_GPS)
    time.sleep(1)

    led.value(0)
    buzzer.value(0)
    lcd.clear()
    lcd.putstr("System Ready")

lcd.putstr("ADAS Simulation\nRaspberry Pi")
time.sleep(2)
lcd.clear()
lcd.putstr("System Ready")

# -------- MAIN LOOP -------- #
while True:
    if USE_BUTTON_SIM:
        # Simulate button press randomly on PC
        import random
        if random.random() < 0.1:  # 10% chance per loop
            alert_bump()
    else:
        data = mpu.get_values()
        az = data["Az"]
        print("AZ:", az)
        if az > BUMP_THRESHOLD:
            alert_bump()

    time.sleep(0.1)
