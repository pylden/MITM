from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.io.bytes_reader import BytesReader


class CheckIntegrityMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8606
        self.data = {"type": "Vector.<int>", "value": []}

    def deserialize(self):
        length = self.buffer_reader.read_var_int()
        for i in range(length):
            self.data["value"].append(self.buffer_reader.read_byte())

    def serialize(self):
        br = BytesReader()
        if len(self.data["value"]):
            br.write_var_int(len(self.data["value"]))
            for data in self.data["value"]:
                br.write_byte(data)
        self.buffer_reader = br
