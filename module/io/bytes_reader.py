from io import BytesIO
import re
from struct import *
from module.io.constant import *


class BytesReader(BytesIO):
    def __init__(self, buffer = b''):
        super().__init__(buffer)

    def get_current_buffer(self):
        return self.getbuffer()[self.tell():]

    def read_byte(self):
        return self.read(1)

    def read_ubyte(self):
        return self.read_byte()

    def read_char(self):
        return self.unpack('!b')

    def read_uchar(self):
        return self.unpack('!B')

    def read_boolean(self):
        return self.unpack('!?')

    def read_short(self):
        return self.unpack('!h', 2)

    def read_ushort(self):
        return self.unpack('!H', 2)

    def read_int(self):
        return self.unpack('!i', 4)

    def read_uint(self):
        return self.unpack('!I', 4)

    def read_float(self):
        return self.unpack('!f', 4)

    def read_double(self):
        return self.unpack('!d', 8)

    def read_utf(self):
        length = self.read_ushort()
        return self.unpack(str(length) + 's', length).decode("utf")

    def read_var_int(self):
        val = 0
        for offset in range(0, INT_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_uchar()
            val += (b & MASK_01111111) << offset
            if not b & MASK_10000000:
                return val

    def read_var_short(self):
        val = 0
        for offset in range(0, SHORT_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_uchar()
            val += (b & MASK_01111111) << offset
            if not (b & MASK_10000000) == MASK_10000000:
                if val > SHORT_MAX_VALUE:
                    val -= UNSIGNED_SHORT_MAX_VALUE
                return val

    def read_var_long(self):
        val = 0
        for offset in range(0, LONG_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_uchar()
            val += (b & MASK_01111111) << offset
            if not b & MASK_10000000:
                return val

    def read_read_var_uh_short(self):
        return self.read_var_short()

    def unpack(self, fmt, length=1):
        return unpack(fmt, self.read(length))[0]

    def pack(self, fmt, data):
        return self.write(pack(fmt, data))