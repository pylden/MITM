from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpouseInformationsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7590
        self.spouse = {"type": "FriendSpouseInformations", "value": ""}
