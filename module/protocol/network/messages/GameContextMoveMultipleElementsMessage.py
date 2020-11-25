from module.protocol.network.message import Message


class GameContextMoveMultipleElementsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3748
        self.movements = {"type": "Vector.<EntityMovementInformations>", "value": ""}
