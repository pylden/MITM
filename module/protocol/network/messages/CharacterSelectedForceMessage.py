from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterSelectedForceMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6332
        self.vars.append({"name": "id", "type": "int", "value": ""})
