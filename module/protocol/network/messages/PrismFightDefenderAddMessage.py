from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightDefenderAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1666
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.defender = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
