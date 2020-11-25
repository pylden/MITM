from module.protocol.network.message import Message


class MapNpcsQuestStatusUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1168
        self.mapId = {"type": "Number", "value": ""}
        self.npcsIdsWithQuest = {"type": "Vector.<int>", "value": ""}
        self.questFlags = {"type": "Vector.<GameRolePlayNpcQuestFlag>", "value": ""}
        self.npcsIdsWithoutQuest = {"type": "Vector.<int>", "value": ""}
