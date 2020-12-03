from io import BytesIO
import re
from struct import *
from module.io.constant import *


class BytesReader(BytesIO):
    def __init__(self, buffer):
        super().__init__(buffer)
        self._current_buffer = buffer

    def get_current_buffer(self):
        return self.getbuffer()[self.tell():]

    def read_byte(self):
        return self.read(1)

    def read_char(self):
        return self.unpack('b')

    def read_uchar(self):
        return self.unpack('B')

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

    def read_int64(self):
        return self.unpack('!q', 8)

    def read_uint64(self):
        return self.unpack('!Q', 8)

    def read_float(self):
        return self.unpack('!f', 4)

    def read_double(self):
        return self.unpack('!d', 8)

    def read_utf(self):
        length = self.read_ushort()
        return self.unpack(str(length) + 's', length).decode("utf")

    def read_var_int(self):
        b = value = offset = 0
        has_next = False
        i = 0
        while offset < INT_SIZE:
            i += 1
            b = self.read_byte()
            has_next = (int.from_bytes(b, 'big') & MASK_10000000) == MASK_10000000
            if offset > 0:
                value = value + ((int.from_bytes(b, 'big') & MASK_01111111) << offset)
            else:
                value = value + (int.from_bytes(b, 'big') & MASK_01111111)
            offset += CHUNCK_BIT_SIZE
            if not has_next:
                return value

    def read_var_short(self):
        value = offset = 0
        while offset < SHORT_SIZE:
            b = self.buffer_reader.read_byte()
            has_next = (int.from_bytes(b, 'big') & MASK_10000000) == MASK_10000000;
            if offset > 0:
                value = value + ((int.from_bytes(b, 'big') & MASK_01111111) << offset)
            else:
                value = value + (int.from_bytes(b, 'big') & MASK_01111111)
            offset += CHUNCK_BIT_SIZE
            if not has_next:
                if value > SHORT_MAX_VALUE:
                    value = value - UNSIGNED_SHORT_MAX_VALUE
                return value

    def read_read_var_uh_short(self):
        return self.read_var_short()

    def unpack(self, fmt, length=1):
        return unpack(fmt, self.read(length))[0]