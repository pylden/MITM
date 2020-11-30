from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRemoveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 373
        self.barType = {"type": "uint", "value": ""}
        self.slot = {"type": "uint", "value": ""}
