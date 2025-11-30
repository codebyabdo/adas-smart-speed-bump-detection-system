from machine import I2C

MPU6050_ADDR = 0x68

class accel:
    def __init__(self, i2c, addr=MPU6050_ADDR):
        self.i2c = i2c
        self.addr = addr
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')  # Wake up
        self.i2c.writeto_mem(self.addr, 0x1C, b'\x00')  # ±2g range
        self.i2c.writeto_mem(self.addr, 0x1B, b'\x00')  # ±250 deg/s range

    def read_raw(self, reg):
        high = self.i2c.readfrom_mem(self.addr, reg, 1)[0]
        low = self.i2c.readfrom_mem(self.addr, reg + 1, 1)[0]
        value = (high << 8) | low
        return value - 65536 if value > 32767 else value

    def get_values(self):
        ax = self.read_raw(0x3B) / 16384.0
        ay = self.read_raw(0x3D) / 16384.0
        az = self.read_raw(0x3F) / 16384.0

        gx = self.read_raw(0x43) / 131.0
        gy = self.read_raw(0x45) / 131.0
        gz = self.read_raw(0x47) / 131.0

        return {
            "Ax": ax,
            "Ay": ay,
            "Az": az,
            "Gx": gx,
            "Gy": gy,
            "Gz": gz
        }
