from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3972
        self.actionId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
