from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServerSelectionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1927
        self.serverId = {"type": "uint", "value": ""}

    def deserialize(self):
        self.serverId = self.buffer_reader.read_read_var_uh_short()
