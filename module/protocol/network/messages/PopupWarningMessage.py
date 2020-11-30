from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6411
        self.lockDuration = {"type": "uint", "value": ""}
        self.author = {"type": "String", "value": ""}
        self.content = {"type": "String", "value": ""}
