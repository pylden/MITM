from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonPartyFinderListenErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4426
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
