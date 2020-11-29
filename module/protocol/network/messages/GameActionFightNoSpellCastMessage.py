from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameActionFightNoSpellCastMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2733
        self.vars.append({"name": "spellLevelId", "type": "uint", "value": ""})
