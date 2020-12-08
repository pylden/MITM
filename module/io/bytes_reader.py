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

    def write_byte(self, value):
        self.write(value)

    def read_ubyte(self):
        return self._unpack('!B')

    def write_ubyte(self, value):
        return self._pack('!B', value)

    def read_char(self):
        return self._unpack('!c')

    def write_char(self, value):
        self._pack('!c', value)

    def read_uchar(self):
        return self._unpack('!C')

    def write_uchar(self, value):
        self._pack('!C', value)

    def read_boolean(self):
        return self._unpack('!?')

    def write_bool(self, value):
        self._pack('!?', value)

    def read_short(self):
        return self._unpack('!h', 2)

    def write_short(self, value):
        return self._pack('!h', value)

    def read_ushort(self):
        return self._unpack('!H', 2)

    def write_ushort(self, value):
        return self._pack('!H', value)

    def read_int(self):
        return self._unpack('!i', 4)

    def write_int(self, value):
        return self._pack('!i', value)

    def read_uint(self):
        return self._unpack('!I', 4)

    def write_uint(self, value):
        return self._pack('!I', value)

    def read_float(self):
        return self._unpack('!f', 4)

    def write_float(self, value):
        return self._pack('!f', value)

    def read_double(self):
        return self._unpack('!d', 8)

    def write_double(self, value):
        return self._pack('!d', value)

    def read_utf(self):
        length = self.read_ushort()
        return self._unpack('!' + str(length) + 's', length).decode("utf")

    def write_utf(self, value):
        length = len(value)
        self.write_ushort(length)
        self._pack('!' + str(length) + 's', bytes(value, 'utf'))

    def read_var_int(self):
        val = 0
        for offset in range(0, INT_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_ubyte()
            val += (b & MASK_01111111) << offset
            if not b & MASK_10000000:
                return val

    def read_var_short(self):
        val = 0
        for offset in range(0, SHORT_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_ubyte()
            val += (b & MASK_01111111) << offset
            if not (b & MASK_10000000) == MASK_10000000:
                if val > SHORT_MAX_VALUE:
                    val -= UNSIGNED_SHORT_MAX_VALUE
                return val

    def read_var_long(self):
        val = 0
        for offset in range(0, LONG_SIZE, CHUNCK_BIT_SIZE):
            b = self.read_ubyte()
            val += (b & MASK_01111111) << offset
            if not b & MASK_10000000:
                return val

    def read_read_var_uh_short(self):
        return self.read_var_short()

    def _write_var(self, i):
        if not i:
            self.write_ubyte(0)
        while i:
            b = i & 0b01111111
            i >>= 7
            if i:
                b |= 0b10000000
            self.write_ubyte(b)

    def write_var_int(self, i):
        assert i.bit_length() <= 32
        self._write_var(i)

    def write_var_uh_int(self, i):
        self.write_var_int(i)

    def write_var_long(self, i):
        assert i.bit_length() <= 64
        self._write_var(i)

    def write_var_uh_long(self, i):
        self.write_var_long(i)

    def write_var_short(self, i):
        assert i.bit_length() <= 16
        self._write_var(i)

    def write_var_uh_short(self, i):
        self.write_var_short(i)

    def _unpack(self, fmt, length=1):
        return unpack(fmt, self.read(length))[0]

    def _pack(self, fmt, data):
        return self.write(pack(fmt, data))