from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpellVariantActivationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8938
        self.spellId = {"type": "uint", "value": ""}
        self.result = {"type": "Boolean", "value": ""}
