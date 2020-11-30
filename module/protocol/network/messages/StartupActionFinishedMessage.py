from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3256
        self.success = {"type": "Boolean", "value": ""}
        self.actionId = {"type": "uint", "value": ""}
        self.automaticAction = {"type": "Boolean", "value": ""}
