from module.protocol.network.message import Message


class RefreshFollowedQuestsOrderRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8535
        self.quests = {"type": "Vector.<uint>", "value": ""}
