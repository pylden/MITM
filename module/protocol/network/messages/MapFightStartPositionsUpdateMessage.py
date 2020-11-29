from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapFightStartPositionsUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6209
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "fightStartPositions", "type": "FightStartingPositions", "value": ""})
