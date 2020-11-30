from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellListUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1059
        self.action = {"type": "uint", "value": ""}
        self.spells = {"type": "Vector.<ForgettableSpellItem>", "value": ""}
