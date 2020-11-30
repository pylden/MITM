from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapNpcsQuestStatusUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1168
        self.mapId = {"type": "Number", "value": ""}
        self.npcsIdsWithQuest = {"type": "Vector.<int>", "value": ""}
        self.questFlags = {"type": "Vector.<GameRolePlayNpcQuestFlag>", "value": ""}
        self.npcsIdsWithoutQuest = {"type": "Vector.<int>", "value": ""}
