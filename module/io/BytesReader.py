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

    def find_type(self, value):
        if "Vector." in value:
            return re.findall(r"Vector.<(.*)>", value)[0], True
        return value, False

    # def read_Boolean(self):
    #     boolean = self.read(1)
    #     assert boolean[0] in [0, 1]
    #     return bool(boolean[0]), 1

    def read_int(self):
        return int.from_bytes(self.read(4), "big", signed=True), 4

    def read_uint(self):
        return int.from_bytes(self.read(4), "big"), 4

    def read_short(self):
        return int.from_bytes(self.read(2), "big", signed=True), 2

    def read_ushort(self):
        return int.from_bytes(self.read(2), "big"), 2

    def read_varint(self):
        value = 0
        offset = 0
        size = 0
        while offset < INT_SIZE:
            b = self.read_byte()[0]
            size += 1
            if offset > 0:
                value += (int.from_bytes(b, 'big') & MASK_01111111) << offset
            else:
                value += int.from_bytes(b, 'big') & MASK_01111111
            offset += CHUNCK_BIT_SIZE
            if not (int.from_bytes(b, 'big') & MASK_10000000) == MASK_10000000:
                return value, size

    def read_byte(self):
        return self.read(1), 1

    def read_double(self):
        return unpack("!d", self.read(8))[0], 8

    def read_float(self):
        return unpack("!f", self.read(4))[0], 4

    def read_vector(self, type):
        size, len = self.read_varint()
        vector = []
        while size > 0:
            vector.append(self.read_byte()[0])
            size -= 1
        return vector, size

    def read_String(self):
        size, len = self.read_ushort()
        return self.read(size).decode("utf"), size

    def read_Version(self):
        return {
            "protocolId": 7207,
            "major": int.from_bytes(self.read_byte()[0], "big"),
            "minor": int.from_bytes(self.read_byte()[0], "big"),
            "code": int.from_bytes(self.read_byte()[0], "big"),
            "build": self.read_int()[0],
            "buildType": int.from_bytes(self.read_byte()[0], "big")
        }, 8

    def read_value(self, var):
        type, is_vector = self.find_type(var["type"])
        if is_vector:
            return self.read_vector(type)[0]
        return getattr(self, 'read_%s' % type)()[0]