from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StartupActionsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1192
        self.actions = {"type": "Vector.<StartupActionAddObject>", "value": ""}
