from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterSuccessMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9170
        self.vars.append({"name": "dungeonIds", "type": "Vector.<uint>", "value": ""})
