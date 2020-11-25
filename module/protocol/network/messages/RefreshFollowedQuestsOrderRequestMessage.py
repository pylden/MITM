from module.protocol.network.message import Message


class RefreshFollowedQuestsOrderRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8535
        self.quests = {"type": "Vector.<uint>", "value": ""}
