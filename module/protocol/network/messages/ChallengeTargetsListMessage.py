from module.protocol.network.message import Message


class ChallengeTargetsListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7959
        self.targetIds = {"type": "Vector.<Number>", "value": ""}
        self.targetCells = {"type": "Vector.<int>", "value": ""}
