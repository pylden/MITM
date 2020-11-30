from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRunningFightDetailsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2688
        self.fightId = {"type": "uint", "value": ""}
        self.attackers = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
        self.defenders = {"type": "Vector.<GameFightFighterLightInformations>", "value": ""}
