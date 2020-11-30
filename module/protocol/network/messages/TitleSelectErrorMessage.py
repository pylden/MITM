from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TitleSelectErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7192
        self.reason = {"type": "uint", "value": ""}
