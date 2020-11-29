from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpellVariantActivationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9900
        self.vars.append({"name": "spellId", "type": "uint", "value": ""})
