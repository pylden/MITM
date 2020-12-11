from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2607
        self.salt = {"type": "String", "value": ""}
        self.key = {"type": "Vector.<int>", "value": ['test']}

    def deserialize(self):
        self.salt = self.buffer_reader.read_utf()
        key_length = self.buffer_reader.read_var_int()
        for i in range(key_length):
            self.key.append(self.buffer_reader.read_char())
