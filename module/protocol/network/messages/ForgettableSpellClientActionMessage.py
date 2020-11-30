from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6056
        self.spellId = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
