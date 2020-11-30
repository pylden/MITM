from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobBookSubscribeRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7697
        self.jobIds = {"type": "Vector.<uint>", "value": ""}
