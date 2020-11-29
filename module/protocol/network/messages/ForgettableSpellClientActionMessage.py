from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6056
        self.vars.append({"name": "spellId", "type": "uint", "value": ""})
        self.vars.append({"name": "action", "type": "uint", "value": ""})
