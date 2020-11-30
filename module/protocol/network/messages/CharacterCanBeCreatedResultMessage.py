from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterCanBeCreatedResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9514
        self.yesYouCan = {"type": "Boolean", "value": ""}
