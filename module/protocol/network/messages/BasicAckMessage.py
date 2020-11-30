from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicAckMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4378
        self.seq = {"type": "uint", "value": ""}
        self.lastPacketId = {"type": "uint", "value": ""}
