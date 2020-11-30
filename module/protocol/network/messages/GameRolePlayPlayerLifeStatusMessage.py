from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2514
        self.state = {"type": "uint", "value": ""}
        self.phenixMapId = {"type": "Number", "value": ""}
