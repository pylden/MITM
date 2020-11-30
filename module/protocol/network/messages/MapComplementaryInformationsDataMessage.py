from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapComplementaryInformationsDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9732
        self.subAreaId = {"type": "uint", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
        self.houses = {"type": "Vector.<HouseInformations>", "value": ""}
        self.actors = {"type": "Vector.<GameRolePlayActorInformations>", "value": ""}
        self.interactiveElements = {"type": "Vector.<InteractiveElement>", "value": ""}
        self.statedElements = {"type": "Vector.<StatedElement>", "value": ""}
        self.obstacles = {"type": "Vector.<MapObstacle>", "value": ""}
        self.fights = {"type": "Vector.<FightCommonInformations>", "value": ""}
        self.hasAggressiveMonsters = {"type": "Boolean", "value": ""}
        self.fightStartPositions = {"type": "FightStartingPositions", "value": ""}
