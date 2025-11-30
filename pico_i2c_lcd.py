from lcd_api import LcdApi
from machine import I2C
from time import sleep_ms

LCD_CLR = 0x01
LCD_HOME = 0x02
LCD_ENTRY_MODE = 0x04
LCD_DISPLAY_CTRL = 0x08
LCD_FUNCTION_SET = 0x20

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        super().__init__(num_lines, num_columns)
        self.i2c = i2c
        self.addr = i2c_addr

    def clear(self):
        print("[LCD] CLEAR")

    def putstr(self, text):
        print("[LCD] " + text)
