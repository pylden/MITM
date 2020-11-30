from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightOptionToggleMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5741
        self.option = {"type": "uint", "value": ""}
