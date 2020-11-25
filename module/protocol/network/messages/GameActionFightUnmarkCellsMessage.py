from module.protocol.network.message import Message


class GameActionFightUnmarkCellsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3826
        self.markId = {"type": "int", "value": ""}
