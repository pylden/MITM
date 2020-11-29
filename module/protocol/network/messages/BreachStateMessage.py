from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4331
        self.vars.append({"name": "owner", "type": "CharacterMinimalInformations", "value": ""})
        self.vars.append({"name": "bonuses", "type": "Vector.<ObjectEffectInteger>", "value": ""})
        self.vars.append({"name": "bugdet", "type": "uint", "value": ""})
        self.vars.append({"name": "saved", "type": "Boolean", "value": ""})
