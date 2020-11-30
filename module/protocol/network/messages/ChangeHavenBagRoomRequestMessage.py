from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChangeHavenBagRoomRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9569
        self.roomId = {"type": "uint", "value": ""}
