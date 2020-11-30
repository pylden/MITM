from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRunningFightListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3292
        self.fights = {"type": "Vector.<FightExternalInformations>", "value": ""}
