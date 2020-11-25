from module.protocol.network.message import Message


class FinishMoveListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6941
        self.finishMoves = {"type": "Vector.<FinishMoveInformations>", "value": ""}
