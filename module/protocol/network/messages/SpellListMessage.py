from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpellListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6326
        self.vars.append({"name": "spellPrevisualization", "type": "Boolean", "value": ""})
        self.vars.append({"name": "spells", "type": "Vector.<SpellItem>", "value": ""})
