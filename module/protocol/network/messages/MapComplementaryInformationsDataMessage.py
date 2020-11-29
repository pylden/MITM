from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapComplementaryInformationsDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9732
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "houses", "type": "Vector.<HouseInformations>", "value": ""})
        self.vars.append({"name": "actors", "type": "Vector.<GameRolePlayActorInformations>", "value": ""})
        self.vars.append({"name": "interactiveElements", "type": "Vector.<InteractiveElement>", "value": ""})
        self.vars.append({"name": "statedElements", "type": "Vector.<StatedElement>", "value": ""})
        self.vars.append({"name": "obstacles", "type": "Vector.<MapObstacle>", "value": ""})
        self.vars.append({"name": "fights", "type": "Vector.<FightCommonInformations>", "value": ""})
        self.vars.append({"name": "hasAggressiveMonsters", "type": "Boolean", "value": ""})
        self.vars.append({"name": "fightStartPositions", "type": "FightStartingPositions", "value": ""})
