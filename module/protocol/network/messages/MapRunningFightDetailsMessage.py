from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRunningFightDetailsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2688
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "attackers", "type": "Vector.<GameFightFighterLightInformations>", "value": ""})
        self.vars.append({"name": "defenders", "type": "Vector.<GameFightFighterLightInformations>", "value": ""})
