from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellDeleteMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8765
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
        self.vars.append({"name": "spells", "type": "Vector.<uint>", "value": ""})
