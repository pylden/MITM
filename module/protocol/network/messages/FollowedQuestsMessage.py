from module.protocol.network.message import Message


class FollowedQuestsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9768
        self.quests = {"type": "Vector.<QuestActiveDetailedInformations>", "value": ""}
