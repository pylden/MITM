from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightDefenderAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1666
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "defender", "type": "CharacterMinimalPlusLookInformations", "value": ""})
