from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ArenaFighterLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8113
        self.vars.append({"name": "leaver", "type": "CharacterBasicMinimalInformations", "value": ""})
