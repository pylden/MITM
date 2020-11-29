from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 666
        self.vars.append({"name": "casterId", "type": "Number", "value": ""})
        self.vars.append({"name": "targetCellId", "type": "uint", "value": ""})
        self.vars.append({"name": "spellId", "type": "uint", "value": ""})
        self.vars.append({"name": "spellLevel", "type": "int", "value": ""})
