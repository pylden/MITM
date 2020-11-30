from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4331
        self.owner = {"type": "CharacterMinimalInformations", "value": ""}
        self.bonuses = {"type": "Vector.<ObjectEffectInteger>", "value": ""}
        self.bugdet = {"type": "uint", "value": ""}
        self.saved = {"type": "Boolean", "value": ""}
