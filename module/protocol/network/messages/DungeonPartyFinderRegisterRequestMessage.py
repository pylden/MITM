from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 919
        self.vars.append({"name": "dungeonIds", "type": "Vector.<uint>", "value": ""})
