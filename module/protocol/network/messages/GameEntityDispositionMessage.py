from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameEntityDispositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3301
        self.vars.append({"name": "disposition", "type": "IdentifiedEntityDispositionInformations", "value": ""})
