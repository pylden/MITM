from module.io.bytes_reader import BytesReader

class NetworkMessage:
    def __init__(self, buffer_reader, len_type, length, count=None):
        self.buffer_reader = buffer_reader
        self.len_type = len_type
        self.length = length
        self.count = count

    def get_hi_header(self):
        br = BytesReader()
        s = self.length
        ssz = 0 if s == 0 else 1 if s  < 256 else 2 if s < 65535 else 3 if s < 16777215 else 4294967295
        br.write_ushort(self.id << 2 | ssz)
        if self.count:
            br.write_int(self.count)
        if ssz == 1:
            br.write_ubyte(s)
        elif ssz == 2:
            br.write_ushort(s)
        else:
            br.write_uint(s)
        return br.getbuffer().hex()

    def get_data(self):
        return bytes.fromhex(self.get_hi_header() + self.buffer_reader.getbuffer().hex())

    def get_message_size(self):
        return 2 + self.len_type + self.length + (0 if self.count is None else 4)

    def __repr__(self):
        return "{0} : {1} => {2}\n{3}".format(
            self.id,
            type(self).__name__,
            self.length,
            [{key: self.__dict__[key]} for x, key in enumerate(self.__dict__) if
             key not in ['buffer_reader', 'len_type', 'length', 'count', 'id']]
       )

    def deserialize(self):
        print("Not implemented yet for {0} => {1}".format(self.id, type(self).__name__))

    def serialize(self):
        print("Not implemented yet for {0} => {1}".format(self.id, type(self).__name__))