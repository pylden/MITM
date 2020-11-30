from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 666
        self.casterId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "uint", "value": ""}
        self.spellId = {"type": "uint", "value": ""}
        self.spellLevel = {"type": "int", "value": ""}
