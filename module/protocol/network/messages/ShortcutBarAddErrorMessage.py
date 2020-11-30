from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarAddErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 788
        self.error = {"type": "uint", "value": ""}
