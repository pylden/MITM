from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpellListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6326
        self.spellPrevisualization = {"type": "Boolean", "value": ""}
        self.spells = {"type": "Vector.<SpellItem>", "value": ""}
