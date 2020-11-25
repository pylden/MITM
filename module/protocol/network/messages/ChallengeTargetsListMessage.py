from module.protocol.network.message import Message


class ChallengeTargetsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7959
        self.targetIds = {"type": "Vector.<Number>", "value": ""}
        self.targetCells = {"type": "Vector.<int>", "value": ""}
