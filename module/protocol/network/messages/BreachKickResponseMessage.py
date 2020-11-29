from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachKickResponseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4542
        self.vars.append({"name": "target", "type": "CharacterMinimalInformations", "value": ""})
        self.vars.append({"name": "kicked", "type": "Boolean", "value": ""})
